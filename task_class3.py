import streamlit as st



# ! python3
import json, requests 

# add your own APIkey
APIkey = '9d5143a6d6866b4cfcde6299838c91aa'
#location = input(' insert location ')

#genre = st.radio("Select a city",('Bozen', 'Milan', 'Rome'), help='click one of the option')
#if genre == 'Bozen':
#     location = 'Bozen'
#elif genre == 'Milan':
#     location = 'Milan'
#else:
#     location = 'Rome'

location = st.radio("Select a city",('London', 'Milan', 'Rome'), help='click one of the option')

#location = st.text_input('Gimme a location', ' rome ')
#st.write('The current location title is', location)

# check API documentation to see what structure of URL is needed to access the data
# http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
# print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
# print(response.text)  


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
#st.text(weatherData) 
# from pprint import pprint 
# pprint(weatherData) 

print(weatherData['main']['temp_max']) 
# more???????????
st.write(weatherData['main']['temp_max'])
st.write(weatherData)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", weatherData['main']['temp'])
col2.metric("Wind", weatherData['wind']['speed'])
col3.metric("Humidity", weatherData['main']['humidity'])
