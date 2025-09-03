import acrcloud
from acrcloud.recognizer import ACRCloudRecognizer
from config import ACRCLOUD_ACCESS_KEY, ACRCLOUD_ACCESS_SECRET

acr_config = {
    'host': 'identify-eu-west-1.acrcloud.com',
    'access_key': ACRCLOUD_ACCESS_KEY,
    'access_secret': ACRCLOUD_ACCESS_SECRET,
    'timeout': 10
}

recognizer = ACRCloudRecognizer(acr_config)

def recognize_audio(file_path):
    try:
        result = recognizer.recognize_by_file(file_path, 0)
        return result
    except Exception as e:
        print(f"ACRCloud Error: {str(e)}")
        return None