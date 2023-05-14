import requests

API_KEY = "92b0bdec87fdfcd85313136488eceac9"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature_celcius = round(data['main']['temp']-273.15,2)
    temperature_F = round((temperature_celcius*9/5)+32)
    print("Weather:", weather)
    print("Temperature:", temperature_F, "Degrees Fahrenheit")

else:
    print("Error Occured")
 