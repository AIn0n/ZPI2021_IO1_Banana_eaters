import unittest, json, random
from datetime import date
from src.functions import *

TEST_JSON = "tests/2022-12-31-to-2023-01-18.json"
test_days_range = range(1, 12)


class TestApp(unittest.TestCase):
    def setUp(self):
        with open(TEST_JSON, "rt") as file:
            self.data = json.load(file)

    def test_convert_data(self):
        input_date = date(1996, 6, 11)
        self.assertEqual(date_to_iso8601(input_date), "1996-06-11")

    def test_load_config(self):
        self.assertEqual("http://api.nbp.pl/api", load_config("src/config.json")["URL"])

    def test_count_tendency_hist_returns_three_categories(self):
        currency = random.choice(get_all_currencies_codes(self.data))
        n = random.choice(test_days_range)
        hist = count_tendency_hist(self.data, currency, n)
        for elem in ("increase", "same", "decrease"):
            self.assertTrue(elem in hist.keys())

    def test_count_hist_sums_to_n(self):
        currency = random.choice(get_all_currencies_codes(self.data))
        n = random.choice(test_days_range)
        hist = count_tendency_hist(self.data, currency, n)
        self.assertEqual(sum(val for _, val in hist.items()), n - 1)

    def test_get_rates_returns_N_non_negative_float(self):
        currency = random.choice(get_all_currencies_codes(self.data))
        n = random.choice(test_days_range)
        rates = get_rates(self.data, currency, n)
        self.assertEqual(len(rates), n)
        for elem in rates:
            self.assertGreater(elem, 0.0)

    def test_get_rates_two_different_currencies_have_different_courses(self):
        currencies = random.choices(get_all_currencies_codes(self.data), k=2)
        n = random.choice(test_days_range)
        r1, r2 = [get_rates(self.data, currency, n) for currency in currencies]
        self.assertNotEqual(r1, r2)

    def test_count_tendency_hist_given_zero_days_return_empty_dict(self):
        currency = random.choice(get_all_currencies_codes(self.data))
        hist = count_tendency_hist(self.data, currency, 0)
        self.assertEqual(hist, {})

    def test_get_diff_between_items_returns_n_minus_one_list_for_n_input(self):
        n = random.choice(range(1, 100))
        input_list = [0.0] * n
        self.assertEqual(n - 1, len(get_diff_between_each_item(input_list)))


if __name__ == "__main__":
    unittest.main()
