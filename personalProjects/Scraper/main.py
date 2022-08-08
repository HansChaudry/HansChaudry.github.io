from email.mime import base
import requests

base_url = "https://api.apilayer.com/exchangerates_data"

currencyType1 = input("Convert from: ")
currencyType2 = input("Convert to: ")
amount = input("Amount: ")

payload = {}
headers= {
  "apikey": "PHQ9OFzYQhFRjTqbjpQss8P0hhQc02Cp"
}

convert_url = base_url + "/convert?to=" + currencyType2 + "&from=" + currencyType1 +"&amount=" + amount

response = requests.request("GET", convert_url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(response.json()['result'])