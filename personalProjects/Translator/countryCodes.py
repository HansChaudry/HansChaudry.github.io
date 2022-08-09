import json, urllib.request as urllib2
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

print(findCountries('en'))