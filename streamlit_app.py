import streamlit
import pandas as pd

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list.set_index('Fruit', inplace = True)

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Burberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')


streamlit.header('Build Your Own Smoothie')
# Create multiselector
streamlit.multiselect('Pick Some Fruits:',list(my_fruit_list.index))

# Display the table on the page
streamlit.dataframe(my_fruit_list)
