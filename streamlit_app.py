
import streamlit;
import pandas;
import requests;
import snowflake.connector;
from urllib.error import URLError;

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
 
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding " + new_fruit
    
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

streamlit.header("Fruityvice Fruit Advice!")

try:
  
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    
    back_from_function = get_fruityvice_data(fruit_choice)
    
    #streamlit.write('The user entered ', fruit_choice)
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    #streamlit.text(fruityvice_response.json())

    # write your own comment -what does the next line do? 
    #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # write your own comment - what does this do?
    streamlit.dataframe(back_from_function)

except URLError as e:
  
  streamlit.error()

#streamlit.stop()

if streamlit.button("Get Fruit Load List"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    #my_cur = my_cnx.cursor()

    #my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
    #my_data_row = my_cur.fetchone()
    #streamlit.text("Hello from Snowflake:")
    #streamlit.text(my_data_row)

    #my_cur.execute("select * from fruit_load_list")
    #my_data_rows = my_cur.fetchone()
    my_data_rows = get_fruit_load_list()

    #streamlit.text("The fruit load list contains:")
    #streamlit.text(my_data_rows)

    streamlit.header("The fruit load list contains:")
    streamlit.dataframe(my_data_rows)

#streamlit.stop()

add_my_fruit = streamlit.text_input('What fruit would you like to add?')

if streamlit.button("Add a Fruit to the List"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
    
    #streamlit.write('Thank you for adding ', fruit_to_add)
    #my_cur.execute("insert into fruit_load_list values('from streamlit')")



