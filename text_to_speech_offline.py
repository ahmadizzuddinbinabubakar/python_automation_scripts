import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init()

# convert this text to speech
text = "I’m going to make him an offer he can’t refuse"
engine.say(text)

# play the speech
engine.runAndWait()