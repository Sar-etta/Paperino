import streamlit as st

import json,requests
from pprint import pprint


option = st.selectbox('What do you want to do?', ('meaning', 'sound', 'spelling'))
st.write('You selected:', option)

keyword = st.text_input('Gimme a word', ' ... ')

if option == 'meaning':
  url= 'https://api.datamuse.com/words?ml=' + keyword + '&max=10' ############
elif option == 'sound':
    url= 'https://api.datamuse.com/words?sl=' + keyword + '&max=10'
else:
    url= 'https://api.datamuse.com/words?sp=' + keyword + '&max=10'


#Step3: Download the JSON data from the API.
response = requests.get(url)   
#Uncomment to see the raw JSON text:
#print(response.text)  


#Step4: Load JSON data into a Python variable and use it in your program.
dataFromDatamuse = json.loads(response.text) 
#Uncomment to see the raw JSON text loaded in a Python Variable:
#print(dataFromDatamuse) 
#Uncomment to see a better readable version:
#pprint(dataFromDatamuse) #dont forget to import the correct pprint library to make this work
#pprint(dataFromDatamuse[0]['word'])#nope-->if you just want to see the first 9 results
######)giusto anche###st.write(dataFromDatamuse[0]['word'])

for eachentry in dataFromDatamuse:
  st.write(dataDromDatamuse[0]['word'])
