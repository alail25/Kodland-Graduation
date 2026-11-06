import speech_recognition as speech_recog#+ Yu # type: ignore
from googletrans import Translator # type: ignore
# https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages
# country code
# python -m pip install -U httpx
# python -m pip install speechrecognition
# language="id" for Indonesian
# pip install googletrans==4.0.0-rc1
#### V1 - function
# def suara():
#     """Convert speech to text using Google Speech Recognition."""
#     mic = speech_recog.Microphone()
#     recog = speech_recog.Recognizer()

#     with mic as audio_file:
#         recog.adjust_for_ambient_noise(audio_file)
#         phrase_time_limit = 10  # Set the phrase time limit in seconds
#         audio = recog.listen(audio_file, phrase_time_limit=phrase_time_limit, timeout=3) # timeout tells the recognizer to wait up to 3 seconds for speech to start
#         # audio = recog.listen(audio_file)
#         return recog.recognize_google(audio, language="en") # type: ignore


# def recognize_wav_file(path: str) -> str:
#     """Recognize speech from a WAV file at `path` using Google Speech API."""
#     recog = speech_recog.Recognizer()
#     with speech_recog.AudioFile(path) as source:
#         audio = recog.record(source)
#     return recog.recognize_google(audio, language="en") # type: ignore


# def recognize_wav_bytes(wav_bytes: bytes) -> str:
#     """Recognize speech from WAV bytes (writes to a temp file)."""
#     import tempfile
#     tmp = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
#     try:
#         tmp.write(wav_bytes)
#         tmp.flush()
#         tmp.close()
#         return recognize_wav_file(tmp.name)
#     finally:
#         try:
#             import os
#             os.unlink(tmp.name)
#         except Exception:
#             pass
#### V2 - script special for local testing
mic = speech_recog.Microphone() # device_index=2 dalam tanda kurung jika perlu spesifik mikrofon
recog = speech_recog.Recognizer()

with mic as audio_file:
    print("Speak in English...")

    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)

    print("Converting to text...")
    print("You said: " + recog.recognize_google(audio, language="en")) # type: ignore

# 📋 Bagaimana cara menggunakannya?
# Setelah kita menerima transkripsi dari pesan pengguna, kita ingin menerjemahkan teks ini ke bahasa lain.

text = recog.recognize_google(audio, language="en") #type: ignore
translator = Translator()
tanya = input("choose one it/fr/en/es/ja/ko/zh-CN/pl/id/zh-HK/zh-TW/ca-ES: ").lower()

translated = translator.translate(text, dest=tanya)  # Kode 'id' adalah kode untuk bahasa Indonesia
print("🌍 Terjemahan ke Bahasa " + tanya + ":", translated.text)

#### V3 - multiple languages
# Language options dictionary
LANGUAGES = {
    '1': {'code': 'id', 'name': 'Indonesian'},
    '2': {'code': 'en-GB', 'name': 'English'},
    '3': {'code': 'ja', 'name': 'Japanese'},
    '4': {'code': 'ko', 'name': 'Korean'},
    '5': {'code': 'zh-CN', 'name': 'Chinese (Simplified)'},
    '6': {'code': 'pl', 'name': 'Polish'},
    '7': {'code': 'zh-HK', 'name': 'Chinese (Traditional Hong Kong)'},
    '8': {'code': 'zh-TW', 'name': 'Chinese, Mandarin (Traditional, Taiwan)'},
    '9': {'code': 'ca-ES', 'name': 'Catalan (Spain)'}
}

def select_language():
    """Prompt user to select a language for speech recognition."""
    print("\nAvailable languages:")
    for key, lang in LANGUAGES.items():
        print(f"{key}. {lang['name']}")
    
    while True:
        choice = input("\nSelect language number: ")
        if choice in LANGUAGES:
            return LANGUAGES[choice]
        print("Invalid choice, please try again")

mic = speech_recog.Microphone()
recog = speech_recog.Recognizer()

try:
    with mic as audio_file:
        selected_lang = select_language()
        print(f"\nPlease speak in {selected_lang['name']}")

        recog.adjust_for_ambient_noise(audio_file)
        phrase_time_limit = 10  # Set the phrase time limit in seconds
        audio = recog.listen(audio_file, phrase_time_limit=phrase_time_limit, timeout=3) # timeout tells the recognizer to wait up to 3 seconds for speech to start
        print("Converting speech to text...")
        text = recog.recognize_google(audio, language=selected_lang['code']) # type: ignore
        print(f"You said: {text}")

except speech_recog.UnknownValueError:
    print("Sorry, could not understand audio")
except speech_recog.RequestError as e:
    print(f"Could not request results; {e}")
except Exception as e:
    print(f"Error occurred: {e}")