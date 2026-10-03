import requests

base_url = "https://www.youtube.com/results?search_query={query}"

def search_youtube(query):
    """Search YouTube for a given query and return the search results page HTML."""
    url = base_url.format(query=query)
    response = requests.get(url)
    if response.status_code == 200:
        return response.text  # Use response.text instead of response.json()
    else:
        return f"Error: {response.status_code}"

# search_results = search_youtube("Python")
# print(search_results)


def get_open_meteo_weather(city_name):
    # 1. Geocode city name to Latitude/Longitude using Open-Meteo's geocoding API
    geo_url = f"https://open-meteo.com{city_name}&count=1&language=en&format=json"
    
    try:
        geo_resp = requests.get(geo_url).json()
        if not geo_resp.get('results'):
            print(f"Location '{city_name}' not found.")
            return
        
        location = geo_resp['results'][0]
        lat, lon = location['latitude'], location['longitude']
        
        # 2. Fetch current weather conditions using coordinates
        weather_url = f"https://open-meteo.com{lat}&longitude={lon}&current_weather=true"
        weather_resp = requests.get(weather_url).json()
        
        current = weather_resp['current_weather']
        
        print(f"\n--- Weather for {location['name']}, {location.get('country', '')} ---")
        print(f"Temperature: {current['temperature']}°C")
        print(f"Wind Speed:  {current['windspeed']} km/h")
        
    except Exception as e:
        print("An error occurred while fetching the data:", e)

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    if city:
        get_open_meteo_weather(city)
