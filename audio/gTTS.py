import streamlit as st

click<=8.0.4

from gtts import gTTS
from googletrans import Translator

translator = Translator()

originaltext = st.text_input(" Gimme a word you want to translate to italian: ", "...")
targetl = st.text_input(" write the two letter of the destination language: ", "it")

trans= translator.translate (originaltext, dest= targetl)

st.write(trans.text)



firstaudio=gTTS(trans.text, targetl) 
firstaudio.save('audiof.mp3')

st.audio(

print('your audio: ')
ipd.display(ipd.Audio('audiof.mp3')) 


audio_file = open('myaudio.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')
