import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

# I didn't register for an API key on Yelp, because I know how HTTP works and how to hit an endpoint in other languages.

headers = {
    "Authorization": "Bearer " + config.api_key
}

params = {
    "term": "Barber",
    "location": "NYC"
}

response = requests.get(url, headers=headers, params=params)
print(response.json()["businesses"])
