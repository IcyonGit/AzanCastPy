import pychromecast
import requests
import schedule
import time

# URL to the Azan MP3 (replace with local file path or accessible URL if necessary)
AZAN_MP3_URL = "http://your-raspberry-pi.local/azan.mp3"  # Update this with the actual URL or file path

# Function to discover Google Cast devices
def get_cast_devices():
    chromecasts, _ = pychromecast.get_chromecasts()
    return chromecasts

# Function to fetch prayer times based on city and country
def get_prayer_times(city, country):
    url = f"http://api.aladhan.com/v1/timingsByCity?city=Kalamazoo&country=US&method=2"
    response = requests.get(url)
    data = response.json()
    return data['data']['timings']

# Function to play Azan on all cast devices
def play_azan_on_cast_devices(mp3_url):
    chromecasts = get_cast_devices()
    if chromecasts:
        for cast in chromecasts:
            cast.wait()  # Wait for the cast device to be ready
            mc = cast.media_controller
            mc.play_media(mp3_url, 'audio/mp3')
            mc.block_until_active()  # Wait until the media starts playing
            print(f"Playing Azan on {cast.device.friendly_name}")
    else:
        print("No Google Cast devices found.")

# Function to schedule Azan at the appropriate prayer times
def schedule_azan(prayer_times):
    schedule.every().day.at(prayer_times['Fajr']).do(play_azan_on_cast_devices, AZAN_MP3_URL)
    schedule.every().day.at(prayer_times['Dhuhr']).do(play_azan_on_cast_devices, AZAN_MP3_URL)
    schedule.every().day.at(prayer_times['Asr']).do(play_azan_on_cast_devices, AZAN_MP3_URL)
    schedule.every().day.at(prayer_times['Maghrib']).do(play_azan_on_cast_devices, AZAN_MP3_URL)
    schedule.every().day.at(prayer_times['Isha']).do(play_azan_on_cast_devices, AZAN_MP3_URL)

# Function to start the scheduling loop
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for 1 minute before checking again

if __name__ == "__main__":
    # Example city and country (replace with your actual location)
    city = "YourCity"
    country = "YourCountry"

    # Fetch prayer times
    print("Fetching prayer times...")
    prayer_times = get_prayer_times(city, country)
    print("Prayer times fetched:", prayer_times)

    # Schedule the Azan for the day
    print("Scheduling Azan...")
    schedule_azan(prayer_times)

    # Start the schedule loop
    print("Running schedule...")
    run_schedule()
