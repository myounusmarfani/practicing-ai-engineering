
## Testing using requests library
import requests

# Test the API endpoints
url = "http://localhost:8000"

# Test the greeting endpoint
response = requests.get(f"{url}/")
print(response.json())

# Test the buildings endpoint
response = requests.get(f"{url}/buildings")
print(response.json())

# Test the specific building endpoint
response = requests.get(f"{url}/buildings/1")
print(response.json())

# Test the username endpoint
response = requests.post(f"{url}/?username=Muhammad")
print(response.json())

# Test the greet endpoint
response = requests.get(f"{url}/greet/Muhammad")
print(response.json())