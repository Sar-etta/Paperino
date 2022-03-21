import streamlit as st
st.header("hello world")  
st.text("from Brixen")  

title = st.text_input('Gimme a movie title', 'lorem ipsum')
st.write('The current movie title is', title)
