from importlib.resources import contents
import random, requests, os, json, urllib.request as urllib2
def findVoice(langCode: str, gender:str='Female', country:str=None)->str:
    target_url = 'https://hanschaudry.github.io/personalProjects/Translator/voiceList.json'
    response = urllib2.urlopen(target_url)
    voices = json.loads(response.read())

    def lang_check(voice):
        return (langCode) in voice['Locale'] and voice['Gender'] == gender

    rlist = list(filter(lang_check, voices))
    
    return random.choice(rlist)['Voice name']

print(findVoice('fr', 'Male'))