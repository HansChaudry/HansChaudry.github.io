from flask import Flask, redirect, url_for, request, render_template, session
import requests, os, uuid, json
from dotenv import load_dotenv
load_dotenv()
import azure.cognitiveservices.speech as speechsdk
from voice import findVoice, findCountries

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/translation', methods=['POST'])
def index_post():
    global original_text, target_language, translated_text, countries
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']

    # Load the values from .env
    key = os.environ['TranslatorKEY']
    endpoint = os.environ['TranslatorENDPOINT']
    location = os.environ['LOCATION']

    # Indicate that we want to translate and the API version (3.0) and the target language
    path = '/translate?api-version=3.0'
    # Add the target language parameter
    target_language_parameter = '&to=' + target_language
    # Create the full URL
    constructed_url = endpoint + path + target_language_parameter

    # Set up the header information, which includes our subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Create the body of the request with the text to be translated
    body = [{ 'text': original_text }]

    # Make the call using post
    translator_request = requests.post(constructed_url, headers=headers, json=body)
    # Retrieve the JSON response
    translator_response = translator_request.json()
    # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

    # Call render template, passing the translated text,
    # original text, and target language to the template

    countries = findCountries(target_language)

    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language,
        countries=countries
    )

@app.route('/speech', methods=['POST'])
def speak():
    target_country = request.form.get('country')
    target_gender = request.form.get('gender')
    key = os.environ['TTSKEY']
    # endpoint = os.environ['TTSENDPOINT']
    location = os.environ['LOCATION']
    speech_config = speechsdk.SpeechConfig(subscription=key, region=location)
    speech_config.speech_synthesis_voice_name=findVoice(target_language, target_gender, target_country)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    text = translated_text
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language,
        countries=countries
    )