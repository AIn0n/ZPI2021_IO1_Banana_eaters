import streamlit as st
import json
import plotly.express as px
import pandas as pd
from functions import *

data = None
with open("tests/2022-12-31-to-2023-01-18.json", "rt") as file:
    data = json.load(file)

st.title("My first app")

currencies = get_all_currencies_codes(data)

selected = st.selectbox("select currency", currencies)

if selected != None:
    collection = count_tendency_hist(data, selected, 12)
    df = pd.DataFrame.from_dict(collection, orient="index", columns=["number of days"])
    fig = px.bar(df, x=df.index, y="number of days")
    st.plotly_chart(fig)
