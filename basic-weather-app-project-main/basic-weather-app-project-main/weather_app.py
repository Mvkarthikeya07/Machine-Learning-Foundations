import requests
from tkinter import *

def get_weather():
    city = city_entry.get().strip()  # removes extra spaces
    api_key = "95f4d0be74718b96410c9e1877959eb9"  # Your real API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            weather_result.config(text="City not found. Please enter a valid city name.")
            return

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = (
            f"City: {city.title()}\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {condition}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s"
        )

        weather_result.config(text=result)

    except Exception as e:
        weather_result.config(text="Error fetching data. Check your internet or try again.")

# GUI Setup
app = Tk()
app.title("Weather App")
app.geometry("350x300")
app.configure(bg="#E8F0F2")

title = Label(app, text="Enter City Name", font=("Arial", 14), bg="#E8F0F2")
title.pack(pady=10)

city_entry = Entry(app, font=("Arial", 12), width=30)
city_entry.pack()

btn = Button(app, text="Get Weather", command=get_weather, font=("Arial", 12), bg="#4CAF50", fg="white")
btn.pack(pady=10)

weather_result = Label(app, text="", font=("Arial", 12), bg="#E8F0F2", justify=LEFT)
weather_result.pack(pady=10)

app.mainloop()

