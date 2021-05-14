
from urllib import request
import json
from Joke import Joke
import pyttsx3

url = "http://official-joke-api.appspot.com/jokes/ten"
req = request.urlopen(url)

print(req.getcode())

data = req.read()
json_data = json.loads(data)

#print(json_data)

jokes = []

for j in json_data:
  setup = j["setup"]
  punchline = j["punchline"]
  joke = Joke(setup, punchline)
  jokes.append(joke)
  print(joke)
  pyttsx3.speak("setup")
  pyttsx3.speak(joke.setup)
  pyttsx3.speak("punchline")
  pyttsx3.speak(joke.punchline)

