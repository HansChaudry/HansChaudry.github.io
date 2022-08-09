import random, requests, os, json
def findVoice(langCode: str)->str:
    # base_url = "https://eastus.tts.speech.microsoft.com/cognitiveservices/voices/list"

    # # key = os.environ['TTSKEY']

    # payload = {}
    # headers = {
    # 'Ocp-Apim-Subscription-Key': '597fd50f663c485b95d7af4d1ac4a63b',
    # }

    # response = requests.request("GET", base_url, headers=headers, data = payload)

    def lang_check(voice):
        return (langCode) in voice['Locale'] and voice['Gender'] == 'Female'
    json_file_path = "voiceList.json"

    with open(json_file_path, 'r') as j:
        contents = list(json.loads(j.read()))

    rlist = list(filter(lang_check, contents))
    
    return random.choice(rlist)['Voice name']
