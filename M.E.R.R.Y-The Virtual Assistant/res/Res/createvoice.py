from gtts import gTTS
from playsound import playsound

def cr(txt,flname):
	tts = gTTS(txt, lang='en')
	tts.save(flname)
	playsound(flname)


# cr("It's feeling boring!","Boring.mp3")
