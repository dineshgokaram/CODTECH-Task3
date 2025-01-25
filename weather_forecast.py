import requests
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Fetch weather data from OpenWeatherMap API
def fetch_weather_data(city, api_key):
    """
    Fetch weather data for the given city from OpenWeatherMap API.
    
    Parameters:
        city (str): Name of the city.
        api_key (str): API key for OpenWeatherMap.
    
    Returns:
        dict: Weather data in JSON format if successful, None otherwise.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data. Check the city name or API key.")
        return None

# Plot the data using Matplotlib and Seaborn
def visualize_weather_data(data, city):
    """
    Visualize weather data using a bar chart.
    
    Parameters:
        data (dict): Weather data in JSON format.
        city (str): Name of the city.
    """
    sns.set_theme(style="whitegrid")

    # Extract relevant data
    labels = ['Temperature (°C)', 'Feels Like (°C)', 'Humidity (%)']
    values = [
        data['main']['temp'],
        data['main']['feels_like'],
        data['main']['humidity']
    ]

    # Create a bar plot
    plt.figure(figsize=(8, 6))
    sns.barplot(x=labels, y=values, palette="viridis")
    plt.title(f"Current Weather Data for {city}", fontsize=16)
    plt.ylabel("Value")
    plt.xlabel("Parameters")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Retrieve API key from environment variables or use a placeholder
    API_KEY = os.getenv("OPENWEATHER_API_KEY", "4f348e7170d072b72c6b9dba3371192e")

    if API_KEY == "4f348e7170d072b72c6b9dba3371192e":
        print("Warning: Replace 'your_default_api_key_here' with your actual API key.")

    # Input the city name
    city = input("Enter the city name: ").strip()

    # Fetch and visualize data
    weather_data = fetch_weather_data(city, API_KEY)
    if weather_data:
        visualize_weather_data(weather_data, city)
