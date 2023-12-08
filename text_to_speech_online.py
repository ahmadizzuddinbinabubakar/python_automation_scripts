from gtts import gTTS
import os

# gTTS stands for Google Text To Speech; 
# it is a Python library that interfaces with Google Translate's text-to-speech API. 
# It requires an Internet connection

# make request to google to get synthesis
tts = gTTS("Hello world")

# save the audio file
tts.save("hello.mp3")

# play the audio file
os.system("afplay hello.mp3") 

# in spanish
tts = gTTS("Hola Mundo", lang="es")
tts.save("hola.mp3")
os.system("afplay hola.mp3") 