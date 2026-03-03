import requests
import matplotlib.pyplot as plt

# 🔹 Replace with your API key
API_KEY = "YOUR_API_KEY_HERE"

# 🔹 City name
city = "Hyderabad"

# 🔹 API URL
url = f"http://api.openweathermap.org/data/2.5/forecast?q=Hyderabad&appid=8c3fdd0c333c50d280e2442829d25f8f&units=metric"

response = requests.get(url)
data = response.json()

# Lists to store data
dates = []
temperatures = []

# Get first 8 time intervals (approx 24 hours)
for item in data["list"][:8]:
    dates.append(item["dt_txt"])
    temperatures.append(item["main"]["temp"])

# Plot graph
plt.figure(figsize=(10,5))

plt.plot(dates, temperatures, marker='o', linestyle='-', linewidth=2)

plt.title("24 Hour Temperature Forecast for Hyderabad", fontsize=14)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")

plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

# Save graph as image
plt.savefig("weather_forecast.png")
plt.show()