import unittest, json, random
from datetime import date
from src.functions import *
import numpy as np

TEST_JSON = "tests/2022-12-20-to-2023-02-07.json"
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

    def test_get_all_currencies_codes_returns_unique_values(self):
        currencies = get_all_currencies_codes(self.data)
        self.assertEqual(len(currencies), len(set(currencies)))

    def test_count_tendency_hist_given_zero_days_return_empty_dict(self):
        currency = random.choice(get_all_currencies_codes(self.data))
        hist = count_tendency_hist(self.data, currency, 0)
        self.assertEqual(hist, {})

    def test_get_diff_between_items_returns_n_minus_one_list_for_n_input(self):
        n = random.choice(range(1, 100))
        input_list = [0.0] * n
        self.assertEqual(n - 1, len(get_diff_between_each_item(input_list)))

    def test_get_diff_between_items_for_multiply_of_two_returns_list_of_twos(self):
        length = random.choice(range(1, 20))
        input_list = [x * 2 for x in range(0, length)]
        self.assertEqual([-2.0] * (length - 1), get_diff_between_each_item(input_list))

    def test_get_diff_between_items_for_two_numbers_returns_one_eq_to_subs(self):
        first_number = random.randint(0, 100)
        second_number = random.randint(0, 100)
        result = get_diff_between_each_item([first_number, second_number])[0]
        self.assertEqual(result, first_number - second_number)

    def test_prep_data_dist_of_changes_returns_same_amount_of_elements_as_steps(self):
        numbers = [0.5, 2, 3]
        steps = 3
        self.assertEqual(len(prep_data_dist_of_changes(numbers, steps)), steps - 1)

    def test_prep_data_dist_of_changes_returns_one_value_at_each_category(self):
        numbers = [1, 2, 3.5, 4]
        steps = 3
        for value in prep_data_dist_of_changes(numbers, steps).values():
            self.assertEqual(value, 1)


if __name__ == "__main__":
    unittest.main()
