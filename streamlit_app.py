import streamlit

import pandas

lista_de_fruta = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(lista_de_fruta)
