import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocketsmoothie')
streamlit.text('Hard-boiled Free-range Egg')
streamlit.text('Avacado Toast')
streamlit.header('Build Your Own Fruit Smootie')

import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list= my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_selected=streamlit.multiselect("Pick some fruit: ", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_show)

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


import streamlit as st
import snowflake.connector
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from fruit_load_list;")
streamlit.dataframe(rows)

