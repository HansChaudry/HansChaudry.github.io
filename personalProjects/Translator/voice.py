import random,json, urllib.request as urllib2
def findVoice(langCode: str, gender:str, country:str)->str:
    target_url = 'https://hanschaudry.github.io/personalProjects/Translator/voiceList.json'
    response = urllib2.urlopen(target_url)
    voices = json.loads(response.read())
    
    if gender == 'Select':
        gender = 'Female'

    def lang_check(voice):
        if country != 'Select':
            return (langCode) in voice['Locale'] and voice['Gender'] == gender and country in voice['Language']
        else:
            return (langCode) in voice['Locale'] and voice['Gender'] == gender

    rlist = list(filter(lang_check, voices))
    
    return random.choice(rlist)['Voice name']

def findCountries(langcode:str)->list:
    target_url = 'https://hanschaudry.github.io/personalProjects/Translator/voiceList.json'
    response = urllib2.urlopen(target_url)
    voices = json.loads(response.read())

    values = []

    for voice in voices:
        if langcode in voice['Locale']:
            country = voice['Language'].split(' ')[1:]
            country = ' '.join(country)
            if country not in values:
                values.append(country)

    values.sort()
    return values
