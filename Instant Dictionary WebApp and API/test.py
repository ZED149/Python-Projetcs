

import requests

reponse = requests.get("http://127.0.0.1:8000/api?w=moon")
print(reponse.text)