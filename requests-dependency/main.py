
import requests
from Joke import Joke

url = "http://official-joke-api.appspot.com/jokes/ten"

response = requests.get(url)
print(response.status_code)

json_data = response.text

#print(json_data)

jokes = []

for j in json_data:
  setup = j["setup"]
  punchline = j["punchline"]
  joke = Joke(setup, punchline)
  jokes.append(joke)
  print(joke)



