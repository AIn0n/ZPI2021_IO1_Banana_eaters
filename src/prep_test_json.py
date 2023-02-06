import requests, datetime
from functions import *

config = load_config("config.json")

response = requests.get(
    config["URL"]
    + f'/exchangerates/tables/A/{"2022-12-20"}/{date_to_iso8601(datetime.date.today())}',
    headers=config["headers"],
)
with open("2022-12-20-to-2023-02-07.json", "w") as file:
    json.dump(response.json(), file, indent=2)
