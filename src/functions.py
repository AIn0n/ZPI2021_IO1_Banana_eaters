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
    rates: list = get_rates(data, currency)
    prev: float = rates[0]
    result: dict = {"increase": 0, "same": 0, "decrease": 0}
    for rate in rates[1:]:
        if rate > prev:
            result["increase"] += 1
        elif rate == prev:
            result["same"] += 1
        else:
            result["decrease"] += 1
        prev = rate
    return result