import requests

response = requests.get(URL + f'/exchangerates/tables/A/{START_DATE}', headers=headers)

print(response.json())
