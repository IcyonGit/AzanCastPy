import pychromecast

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
    print(f"Connecting to {cast.device.friendly_name}...")
    cast.wait()

    # Load the Azan MP3 from your provided URL
    media_url = "https://icyongit.github.io/AzanCastPy/azan.mp3"
    media_type = "audio/mp3"
    print(f"Playing Azan on {cast.device.friendly_name}...")

    # Start media playback
    cast.media_controller.play_media(media_url, media_type)
    
    # Wait for the media controller to become active
    cast.media_controller.block_until_active()

    # Check the status of the media controller
    status = cast.media_controller.status

    # Simplified output
    print(f"Media Status:")
    print(f" - Player State: {status.player_state}")
    print(f" - Current Time: {status.current_time} seconds")
    
    if status.duration is not None:
        print(f" - Duration: {status.duration} seconds")
    else:
        print(" - Duration: Not available")

    if status.player_state == "BUFFERING":
        print("Media is buffering...")
    elif status.player_state == "PLAYING":
        print("Media is playing.")
    elif status.player_state == "IDLE":
        print("Media failed to load or stopped unexpectedly.")
    else:
        print(f"Player state: {status.player_state}")

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
