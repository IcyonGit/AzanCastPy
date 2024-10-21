import pychromecast
import time

# Function to discover all available Chromecast devices
def discover_devices():
    chromecasts, browser = pychromecast.get_chromecasts()
    return chromecasts

# Function to display the list of discovered devices
def list_devices(chromecasts):
    print("Available devices:")
    for i, cast in enumerate(chromecasts):
        print(f"{i+1}. {cast.device.friendly_name}")

# Function to select a device from the list
def select_device(chromecasts):
    while True:
        try:
            choice = int(input("Select the device number to cast to: ")) - 1
            if choice < 0 or choice >= len(chromecasts):
                print("Invalid choice. Please try again.")
            else:
                return chromecasts[choice]
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to play media on the selected device
def play_media_on_device(cast):
    # Wait for the device to be ready
    cast.wait()
    
    # Load media (test media URL)
    media_url = "The Adhan - Omar Hisham Al Arabi  الأذان بصوت عمر هشام العربي  The Call to Prayer.mp3"
    media_type = "audio/mp3"
    print(f"Playing test media on {cast.device.friendly_name}...")

    # Start media playback
    cast.media_controller.play_media(media_url, media_type)
    cast.media_controller.block_until_active()
    print("Media is playing...")

    # Wait for a few seconds to allow the media to play
    time.sleep(10)
    
    # Stop the media
    cast.media_controller.stop()
    print("Media playback stopped.")

# Main function
def main():
    print("Discovering devices...")
    
    # Discover devices
    chromecasts = discover_devices()
    
    if not chromecasts:
        print("No devices found.")
        return
    
    # List devices and allow user to choose
    list_devices(chromecasts)
    selected_device = select_device(chromecasts)
    
    # Play media on the selected device
    play_media_on_device(selected_device)

if __name__ == "__main__":
    main()
