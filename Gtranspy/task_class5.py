import streamlit as st

import json,requests
from pprint import pprint

from googletrans import Translator

translator=Translator()

word = st.text_input(" Gimme a word you want to translate to italian: ")

trans_it= translator.translate (word, dest= "it")

st.write(trans_it)



