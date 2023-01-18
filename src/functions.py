from datetime import date
import json

def date_to_iso8601(input_date: date) -> str:
  return input_date.isoformat()

def load_config(dir: str) -> dict:
  with open(dir) as file:
    return json.load(file)