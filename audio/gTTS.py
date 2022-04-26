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
my_audio=open('audiof.mp3', 'rb')
st.audio(my_audio, format='audio/mp3')
