
import os
try:
    import audioread
    have_audioread = True
except ImportError:
    have_audioread = False
try:
    import chromaprint
    have_chromaprint = True
except ImportError:
    have_chromaprint = False

import subprocess
import sys

MAX_AUDIO_LENGTH = 120 # Seconds.    
FPCALC_COMMAND = 'fpcalc'
FPCALC_ENVVAR = 'FPCALC'

def _fingerprint_file_fpcalc(path, maxlength):
    """Fingerprint a file by calling the fpcalc application."""
    fpcalc = os.environ.get(FPCALC_ENVVAR, FPCALC_COMMAND)
    command = [fpcalc, "-length", str(maxlength), path]
    try:
        with open(os.devnull, 'wb') as devnull:
            proc = subprocess.Popen(command, stdout=subprocess.PIPE,
                                    stderr=devnull)
            output, _ = proc.communicate()
    except OSError as exc:
        if exc.errno == errno.ENOENT:
            raise NoBackendError("fpcalc not found")
        else:
            raise FingerprintGenerationError("fpcalc invocation failed: %s" %
                                             str(exc))
    except UnicodeEncodeError:
        # Due to a bug in Python 2's subprocess on Windows, Unicode
        # filenames can fail to encode on that platform. See:
        # http://bugs.python.org/issue1759845
        raise FingerprintGenerationError("argument encoding failed")
    retcode = proc.poll()
    if retcode:
        raise FingerprintGenerationError("fpcalc exited with status %i" %
                                         retcode)

    duration = fp = None
    for line in output.splitlines():
        try:
            parts = line.split(b'=', 1)
        except ValueError:
            raise FingerprintGenerationError("malformed fpcalc output")
        if parts[0] == b'DURATION':
            try:
                duration = float(parts[1])
            except ValueError:
                raise FingerprintGenerationError("fpcalc duration not numeric")
        elif parts[0] == b'FINGERPRINT':
            fp = parts[1]

    if duration is None or fp is None:
        raise FingerprintGenerationError("missing fpcalc output")
    return duration, fp

def fingerprint(samplerate, channels, pcmiter, maxlength=MAX_AUDIO_LENGTH):
    """Fingerprint audio data given its sample rate and number of
    channels.  pcmiter should be an iterable containing blocks of PCM
    data as byte strings. Raises a FingerprintGenerationError if
    anything goes wrong.
    """
    # Maximum number of samples to decode.
    endposition = samplerate * channels * maxlength

    try:
        fper = chromaprint.Fingerprinter()
        fper.start(samplerate, channels)

        position = 0 # Samples of audio fed to the fingerprinter.
        for block in pcmiter:
            fper.feed(block)
            position += len(block) // 2 # 2 bytes/sample.
            if position >= endposition:
                break

        return fper.finish()
    except chromaprint.FingerprintError:
        raise FingerprintGenerationError("fingerprint calculation failed")

def _fingerprint_file_audioread(path, maxlength=MAX_AUDIO_LENGTH):
    """Fingerprint a file by using audioread and chromaprint."""
    try:
        with audioread.audio_open(path) as f:
            duration = f.duration
            fp = fingerprint(f.samplerate, f.channels, iter(f), maxlength)
    except audioread.DecodeError:
        raise FingerprintGenerationError("audio could not be decoded")
    return duration, fp        

def fingerprint_file(path, maxlength=MAX_AUDIO_LENGTH):
    """Fingerprint a file either using the Chromaprint dynamic library
    or the fpcalc command-line tool, whichever is available. Returns the
    duration and the fingerprint.
    """
    path = os.path.abspath(os.path.expanduser(path))
    if have_audioread and have_chromaprint:
        return _fingerprint_file_audioread(path, maxlength)
    else:
        return _fingerprint_file_fpcalc(path, maxlength)

if __name__ == '__main__':
    duration, fp =  fingerprint_file(sys.argv[1])  
    print(fp)