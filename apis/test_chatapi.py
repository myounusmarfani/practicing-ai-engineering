import requests

url = "http://localhost:8000/chat"

message = "Explain Quantum Computing in one short sentence."

response = requests.post(f"{url}/{message}")
print(response.json())