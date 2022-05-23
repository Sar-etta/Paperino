import streamlit as st

with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.write("surprise")
    st.balloons

st.write("This is outside the container")
