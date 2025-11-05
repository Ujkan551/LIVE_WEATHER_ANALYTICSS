import requests
import pandas as pd
from datetime import datetime
import time

# Configuration
API_KEY = "8e90df3e35fa6be5000c72cd12951ffb"
 # Get from openweathermap.org
CITY = "Varanasi"
COUNTRY_CODE = "IN"
CSV_FILE = "livo_weather_data.csv"

def fetch_weather_data():
    """Fetch current weather and forecast data from OpenWeatherMap API"""
    
    # API endpoint for current weather
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY_CODE}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status
        data = response.json()
        
        # Extract relevant weather information
        weather_info = {
            'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'City': data['name'],
            'Temperature': data['main']['temp'],
            'Feels_Like': data['main']['feels_like'],
            'Humidity': data['main']['humidity'],
            'Pressure': data['main']['pressure'],
            'Weather': data['weather'][0]['main'],
            'Description': data['weather'][0]['description'],
            'Wind_Speed': data['wind']['speed'],
            'Cloudiness': data['clouds']['all']
        }
        
        return weather_info
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_to_csv(weather_info, filename=CSV_FILE):
    """Save weather data to CSV file"""
    
    if weather_info is None:
        return
    
    # Convert to DataFrame
    df = pd.DataFrame([weather_info])
    
    try:
        # Check if file exists; if yes, append, if no, create new
        try:
            existing_df = pd.read_csv(filename)
            df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            pass  # File doesn't exist yet, just use new df
        
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
        print(df.tail())  # Print last few rows
    
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def run_continuous_fetch(interval_minutes=60):
    """Run the fetch continuously at specified intervals"""
    
    print(f"Starting weather data fetch every {interval_minutes} minutes...")
    print(f"Press Ctrl+C to stop\n")
    
    while True:
        print(f"Fetching data at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        weather_info = fetch_weather_data()
        save_to_csv(weather_info)
        
        # Wait for specified interval (in seconds)
        time.sleep(interval_minutes * 60)

# Run the script
if __name__ == "__main__":
    # Option 1: Fetch once
    print("Option 1: Fetch weather data once")
    weather = fetch_weather_data()
    if weather:
        save_to_csv(weather)
    
    # Option 2: Uncomment below to run continuously every 30 minutes
    run_continuous_fetch(interval_minutes=30)
