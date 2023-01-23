import unittest, json, random
from datetime import date
from src.functions import *

TEST_JSON = "tests/2022-12-31-to-2023-01-18.json"

class TestApp(unittest.TestCase):
    def test_convert_data(self):
        input_date = date(1996, 6, 11)
        self.assertEqual(date_to_iso8601(input_date), "1996-06-11")

    def test_load_config(self):
        self.assertEqual("http://api.nbp.pl/api", load_config("src/config.json")["URL"])

    def test_count_tendency_hist_should_return_three_categories(self):
        with open(TEST_JSON, "rt") as file:
            data = json.load(file)
            currency = random.choice(get_all_currencies_codes(data))
            hist = count_tendency_hist(data, currency)
            for elem in ("increase", "same", "decrease"):
                self.assertTrue(elem in hist.keys())