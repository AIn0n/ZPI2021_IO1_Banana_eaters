import unittest
from datetime import date
from src.main import date_to_iso8601

class TestApp(unittest.TestCase):
  def test_convert_data(self):
    input_date = date(1996, 6, 11)
    self.assertEqual(date_to_iso8601(input_date), "1996-06-11")