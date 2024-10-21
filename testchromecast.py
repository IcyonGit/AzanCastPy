import pychromecast

# Test media file (change the URL to something else if needed)
TEST_MEDIA_URL = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"

# Discover Google Cast devices on the network
def get_cast_devices():
    chromecasts, _ = pychromecast.get_chromecasts()
    return chromecasts

# Play media on a selected device
def play_test_media_on_device(cast, media_url):
    cast.wait()  # Wait for the cast device to be ready
    mc = cast.media_controller
    mc.play_media(media_url, 'video/mp4')  # Change 'video/mp4' to 'audio/mp3' if testing with an audio file
    mc.block_until_active()  # Wait until the media starts playing
    print(f"Playing test media on {cast.device.friendly_name}")

if __name__ == "__main__":
    print("Discovering Google Cast devices...")
    chromecasts = get_cast_devices()

    if chromecasts:
        for cast in chromecasts:
            print(f"Found device: {cast.device.friendly_name}")
        # Play media on the first discovered device (you can modify this to select a specific one)
        print(f"Playing media on {chromecasts[0].device.friendly_name}")
        play_test_media_on_device(chromecasts[0], TEST_MEDIA_URL)
    else:
        print("No Google Cast devices found.")
