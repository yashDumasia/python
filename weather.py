import requests
city_name = input("City Name : ")
API_key = "c82fe4c2e0f0219c38c8805c373b9861"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

respones = requests.get(url)

if respones.status_code == 200:
   data = respones.json()
   print("Weather is : ",data['weather'][0]['description'].title())
   print("Current Temperature is : ",data['main']['temp'], "°C")
   print("Current Temperature Feels Like is :", data['main']['feels_like'], "°C")
   print("Current Humidity is : ",data['main']['humidity'])
    