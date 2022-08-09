from operator import contains
from textwrap import indent
import requests
import random

base_url = "https://eastus.tts.speech.microsoft.com/cognitiveservices/voices/list"

# currencyType1 = input("Convert from: ")
# currencyType2 = input("Convert to: ")
# amount = input("Amount: ")

payload = {}
headers = {
  'Ocp-Apim-Subscription-Key': "597fd50f663c485b95d7af4d1ac4a63b",
}

# convert_url = base_url + "/convert?to=" + currencyType2 + "&from=" + currencyType1 +"&amount=" + amount

response = requests.request("GET", base_url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
def lang_check(voice):
  return ('English') in voice['LocaleName'] and voice['Gender'] == 'Female'
rlist = list(filter(lang_check, response.json()))

# print(rlist)
# print('\n'.join('{}: {}'.format(*k) for k in enumerate(rlist)))
print(random.choice(rlist)['ShortName'])