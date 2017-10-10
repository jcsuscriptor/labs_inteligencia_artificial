from acrcloud.recognizer import ACRCloudRecognizeType

config = {
    'host':'identify-us-west-2.acrcloud.com',
    'access_key':'0dedd9a1788af206f5e1ff0cea80acfe',
    'access_secret':'8C1YAClYZc8is0z90qFPyNMJIegkmNEtLz98bDzx',
    'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO, # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
    'debug':False,
    'timeout':10 # seconds
}  