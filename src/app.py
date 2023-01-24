import streamlit as st
import json
import plotly.express as px
import pandas as pd
from functions import *


def test_loading_data():
    with open("tests/2022-12-31-to-2023-01-18.json", "rt") as file:
        return json.load(file)


st.title("exchange rates")

# this part of code is related to loading data from API
data_load_state = st.text("loading data")
data = test_loading_data()
data_load_state.text("data successfully fetched from API")

currencies = get_all_currencies_codes(data)
selected = st.selectbox("select currency", currencies)
if selected != None:
    # get days period
    st.subheader("Histogram of changes")
    hist_time_dict = {"week": 7, "two weeks": 14, "month": 30, "quarter": 90}
    selected_time = st.selectbox("select time period", hist_time_dict.keys())

    # prepare data and add chart
    collection = count_tendency_hist(data, selected, hist_time_dict[selected_time])
    df = pd.DataFrame.from_dict(collection, orient="index", columns=["number of days"])
    fig = px.bar(df, x=df.index, y="number of days")
    st.plotly_chart(fig)
