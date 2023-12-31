import streamlit
import pandas

streamlit.title('Título')
streamlit.header('Subtítulo')

lista_de_fruta = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(lista_de_fruta)

fruits_selected = streamlit.multiselect("Pick some fruits:",list(lista_de_fruta.index),['Avocado','Apple'])
fruits_to_show = lista_de_fruta.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
