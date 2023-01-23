import unittest, json, random
from datetime import date
from src.functions import *

TEST_JSON = "tests/2022-12-31-to-2023-01-18.json"


class TestApp(unittest.TestCase):
    def setUp(self):
        with open(TEST_JSON, "rt") as file:
            self.data = json.load(file)

    def test_convert_data(self):
        input_date = date(1996, 6, 11)
        self.assertEqual(date_to_iso8601(input_date), "1996-06-11")

    def test_load_config(self):
        self.assertEqual("http://api.nbp.pl/api", load_config("src/config.json")["URL"])

    def test_count_tendency_hist_should_return_three_categories(self):
        currency = random.choice(get_all_currencies_codes(self.data))
        hist = count_tendency_hist(self.data, currency)
        for elem in ("increase", "same", "decrease"):
            self.assertTrue(elem in hist.keys())

    def test_count_hist_should_sum_to_twenty(self):
        currency = random.choice(get_all_currencies_codes(self.data))
        hist = count_tendency_hist(self.data, currency)
        self.assertEqual(sum(len(val) for key, val in hist.items()), 12)

    def test_get_rates_should_return_twenty_non_negative_float(self):
        currency = random.choice(get_all_currencies_codes(self.data))
        rates = get_rates(self.data, currency)
        self.assertEqual(len(rates), 12)
        for elem in rates:
            self.assertGreater(elem, 0.0)

    def test_get_rates_two_different_currencies_should_have_different_courses(self):
        currencies = random.choices(get_all_currencies_codes(self.data), k=2)
        r1, r2 = [get_rates(self.data, currency) for currency in currencies]
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
