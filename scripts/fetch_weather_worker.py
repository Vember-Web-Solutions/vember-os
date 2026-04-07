import subprocess
import json
from data_hub import DataHub

def fetch_weather():
    hub = DataHub()
    
    # The exact URL that worked in your terminal
    url = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current=temperature_2m,weather_code&daily=temperature_2m_max,temperature_2m_min&temperature_unit=fahrenheit&timezone=auto"
    
    print(f"📡 Vember-OS: Initiating fetch via System Curl...")
    
    try:
        # We call the system's curl directly to bypass Python's SSL/Gateway issues
        result = subprocess.run(
            ['curl', '-s', url],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse the string output into a JSON object
        weather_data = json.loads(result.stdout)
        
        # Write to the DataHub
        if hub.write("weather", weather_data):
            print("✅ Success: weather.json updated in /data")
        else:
            print("❌ Error: DataHub could not write to disk.")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ System Error: Curl failed to reach the server. {e}")
    except json.JSONDecodeError:
        print("❌ Data Error: Received invalid response from server.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    fetch_weather()