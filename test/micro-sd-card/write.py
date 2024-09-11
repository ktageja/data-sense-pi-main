from machine import SPI, Pin
import uos
# import sdcard # Note: add util to extraPaths
from sdcard import SDCard

# Initialize SPI interface for the SD card
spi = SPI(0, 
          sck=Pin(18), # pin 24 
          mosi=Pin(19),  # pin 25
          miso=Pin(16) # pin 21
          )
cs = Pin(22)

# Initialize the SD card
sd = SDCard(spi, cs)

# Try to mount the SD card
try:
    uos.mount(sd, '/')
    print("SD card mounted successfully.")
except Exception as e:
    print("Failed to mount SD card:", e)
    # Exit if SD card cannot mount
    raise

# Test write path
file_path = '/hello_world.txt'

# Write "Hello, World!" to the text file on the SD card
try:
    with open(file_path, 'w') as file:
        file.write('Hello, World!')
    print("Text written to hello_world.txt successfully.")
except Exception as e:
    print("Failed to write to file:", e)
    # Exit if cannot write to SD card
    raise

# Unmount SD card
try:
    uos.umount('/')
    print("SD card unmounted successfully.")
except Exception as e:
    print("Failed to unmount SD card:", e)
    # Exit if cannot unmount SD card
    raise
