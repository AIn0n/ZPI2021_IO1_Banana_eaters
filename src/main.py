import requests
from datetime import date

def date_to_iso8601(input_date: date) -> str:
  return input_date.isoformat()

headers = {
  "Accept": "application/json"
}

URL = "http://api.nbp.pl/api"

START_DATE = "2002-01-02"

response = requests.get(URL + f'/exchangerates/tables/A/{START_DATE}', headers=headers)

print(response.json())
