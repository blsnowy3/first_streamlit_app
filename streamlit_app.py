
import streamlit;
import pandas;
import requests;

streamlit.title("hello world")

streamlit.header("Breakfast Menu")

streamlit.text("🥣 Blueberry")
streamlit.text("🥗 Kale")
streamlit.text("🐔 Egg")
streamlit.text("🥑 Avocado")
streamlit.text("🍞 Cheese")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

streamlit.header("Fruityvice Fruit Advice!")




