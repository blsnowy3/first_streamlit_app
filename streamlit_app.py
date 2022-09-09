
import streamlit;
import pandas;

streamlit.title("hello world")

streamlit.header("Breakfast Menu")

streamlit.text("🥣 Blueberry")
streamlit.text("🥗 Kale")
streamlit.text("🐔 Egg")
streamlit.text("🥑 Avocado")
streamlit.text("🍞 Cheese")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

