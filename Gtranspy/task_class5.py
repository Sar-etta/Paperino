import streamlit as st

from googletrans import Translator

translator=Translator()

word = st.text_input(" Gimme a word you want to translate to italian: ")

trans_it= translator.translate (word, dest= "it")

st.write(trans_it)



