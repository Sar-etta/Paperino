st.header(Task about Googletrans for Python)

import streamlit as st

from googletrans import Translator

translator=Translator()

word = st.text_input(" Gimme a word you want to translate to italian: ", "...")
targetl = st.text_input(" write the two letter of the destination language: ", "it")

trans= translator.translate (word, dest= targetl)

st.write(trans.text)

