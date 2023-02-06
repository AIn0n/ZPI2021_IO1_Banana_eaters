from datetime import date
import json
import numpy as np
from collections import defaultdict


def date_to_iso8601(input_date: date) -> str:
    return input_date.isoformat()


def load_config(dir: str) -> dict:
    with open(dir) as file:
        return json.load(file)


def get_all_currencies_codes(data: dict) -> list:
    return list(map(lambda x: x["code"], data[0]["rates"]))


def get_rates(data: dict, currency: str, days: int) -> list[float]:
    rates = [x["rates"] for x in data]
    result = reversed(
        [list(filter(lambda x: x["code"] == currency, r))[0]["mid"] for r in rates]
    )
    return list(result)[:days]


def get_diff_between_each_item(l: list) -> list:
    results = []
    for i in range(0, len(l) - 1):
        results.append(l[i] - l[i + 1])
    return results


def count_tendency_hist(data: dict, currency: str, days: int) -> dict:
    if days < 1:
        return {}
    rates: list = get_rates(data, currency, days)
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


def prep_data_dist_of_changes(nums: list, steps: int) -> dict:
    changes = get_diff_between_each_item(nums)
    start = min(changes)
    end = max(changes)
    parts = np.linspace(start, end, steps + 1)
    results = defaultdict(int)
    for n in changes:
        index = np.searchsorted(parts, n, side="right") - 1
        if index == len(parts) - 1:
            index -= 1
        results[f"[{parts[index]:.3f} - {parts[index + 1]:.3f}]"] += 1
    return dict(results)
