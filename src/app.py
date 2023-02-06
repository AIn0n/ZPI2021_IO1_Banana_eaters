import streamlit as st
import json, statistics, requests, datetime
import plotly.express as px
import pandas as pd
from functions import *

config = load_config("src/config.json")


def gather_data(start_date: datetime.datetime):
    next_90_days = start_date + datetime.timedelta(days=90)
    response = requests.get(
        config["URL"]
        + f"/exchangerates/tables/A/{date_to_iso8601(start_date)}/{date_to_iso8601(next_90_days)}",
        headers=config["headers"],
    )
    return response.json()


def test_loading_data():
    with open("tests/2022-12-20-to-2023-02-07.json", "rt") as file:
        return json.load(file)


def prep_hist(collection):
    df = pd.DataFrame.from_dict(collection, orient="index", columns=["number of days"])
    return px.bar(df, x=df.index, y="number of days")


def prepare_stats_table(rates):
    mean = statistics.mean(rates)
    stdev = statistics.stdev(rates)
    stats = [
        ["average", mean],
        ["median", statistics.median(rates)],
        ["standard deviation", stdev],
        ["coefficient of variation", stdev / mean * 100],
    ]
    stats_df = pd.DataFrame(stats, columns=["function", "value"])
    stats_df = stats_df.set_index("function").T
    stats_df.columns = list(map(lambda x: x[0], stats))
    return stats_df


st.title(":currency_exchange: exchange rates app")

min_date = datetime.date(2002, 1, 2)
max_date = datetime.datetime.today() - datetime.timedelta(days=90)
start_date = st.date_input(
    "Choose starting data", min_date, min_value=min_date, max_value=max_date
)

# this part of code is related to loading data from API
data_load_state = st.text("loading data")
data = gather_data(start_date) if config["production"] else test_loading_data()
data_load_state.text("data successfully fetched from API")

with st.expander("single currency analysis"):
    currencies = get_all_currencies_codes(data)
    selected = st.selectbox("select currency", currencies, key=0)

    # get days period
    st.subheader(":bar_chart: Histogram of changes")
    hist_time_dict = {"week": 7, "two weeks": 14, "month": 30, "quarter": 90}
    selected_time = st.selectbox("select time period", hist_time_dict.keys())

    # prepare data and add chart
    collection = count_tendency_hist(data, selected, hist_time_dict[selected_time])
    st.plotly_chart(prep_hist(collection))

    st.subheader(":clipboard: statistics table")

    rates = get_rates(data, selected, hist_time_dict[selected_time])
    st.table(prepare_stats_table(rates))

with st.expander("two currencies comparison"):
    left_col, mid_col, right_col = st.columns(3)
    first_curr = second_curr = days = None
    comp_time_dict = {"month": 30, "quarter": 90}

    with left_col:
        first_curr = st.selectbox("select first currency", currencies)

    with mid_col:
        second_curr = st.selectbox("select second currency", currencies)

    with right_col:
        days = st.selectbox("choose time range", comp_time_dict.keys())

    if first_curr is second_curr:
        st.error("please choose two different currencies to compare")
    else:
        first_rates = get_rates(data, first_curr, comp_time_dict[days])
        second_rates = get_rates(data, second_curr, comp_time_dict[days])
        diff = [a / b for a, b in zip(first_rates, second_rates)]
        comp = prep_data_dist_of_changes(diff, 9)
        st.plotly_chart(prep_hist(comp))
