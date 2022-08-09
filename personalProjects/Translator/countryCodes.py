from importlib.resources import contents
import random, requests, os, json, urllib.request as urllib2


target_url = 'https://hanschaudry.github.io/personalProjects/Translator/voiceList.json'
response = urllib2.urlopen(target_url)
voices = json.loads(response.read())

values = []

for voice in voices:
    country = list(voice['Language'][1:])
    if country not in values:
        values.append(country)

values.sort()
print(values)