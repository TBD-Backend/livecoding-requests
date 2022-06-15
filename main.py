import requests

url = "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2"


class NetworkRequestError(Exception):
    pass


try:
    response = requests.get(url)

    response_json = response.json()
except requests.ConnectionError:
    raise NetworkRequestError("Could not connect to API")

# def map_response(fact):
#     return fact["text"]


# mapped = (map(map_response, response_json))

mapped = (map(lambda fact: {"text": fact["text"]}, response_json))

print(*mapped)
