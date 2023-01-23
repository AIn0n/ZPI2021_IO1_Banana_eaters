from datetime import date
import json


def date_to_iso8601(input_date: date) -> str:
    return input_date.isoformat()


def load_config(dir: str) -> dict:
    with open(dir) as file:
        return json.load(file)


def get_all_currencies_codes(data: dict) -> list:
    return list(map(lambda x: x["code"], data[0]["rates"]))


def get_rates(data: dict, currency: str) -> list[float]:
    rates = [x["rates"] for x in data]
    return [list(filter(lambda x: x["code"] == currency, r))[0]["mid"] for r in rates]


def count_tendency_hist(data: dict, currency: str) -> dict:
    prev = data[0]
    for elem in data[1:]:
        pass
