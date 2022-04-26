from gtts import gTTS
from googletrans import Translator

translator = Translator()

text=input('please type some text: ') #original text
destlang= input('tell me a two etter code for the det lang: ')
abc = translator.translate(text, dest=destlang) #translated text

print(abc.text) #-->translated text

firsta=gTTS(abc.text, destlang) #i need translated text
firsta.save('audiof.mp3')


print('your audio: ')
ipd.display(ipd.Audio('audiof.mp3')) #it's a string
