from acrcloud.recognizer import ACRCloudRecognizeType

config = {
    'host':'host',
    'access_key':'access_key',
    'access_secret':'access_secret',
    'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO, # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
    'debug':False,
    'timeout':10 # seconds
}