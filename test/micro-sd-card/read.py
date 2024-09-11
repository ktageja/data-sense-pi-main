from machine import SPI, Pin
import uos
import sdcard # Note: add util to extraPaths

# Initialize SPI interface for the SD card
spi = SPI(0, 
          sck=Pin(18), # pin 24 
          mosi=Pin(19),  # pin 25
          miso=Pin(16) # pin 21
          )
cs = Pin(22)

# Initialize the SD card
sd = sdcard.SDCard(spi, cs)

# Try to mount the SD card
try:
    uos.mount(sd, '/')
    print("SD card mounted successfully.")
except Exception as e:
    print("Failed to mount SD card:", e)
    # Exit if SD card cannot mount
    raise

# List the contents of the SD card root directory
try:
    print("Contents of /", uos.listdir('/'))
except Exception as e:
    print("Failed to list directory contents:", e)
    # Exit if cannot read SD card contents
    raise

# Print file contents
file_path = '/hello_world.txt'  # Path to the file

# Read file content
try:
    with open(file_path, 'r') as file:
        contents = file.read()  # Read the contents of the file
        print("Contents of", file_path + ":")
        print(contents)  # Print the contents of the file
except Exception as e:
    print("Failed to read file:", e)



# Unmount SD card
try:
    uos.umount('/')
    print("SD card unmounted successfully.")
except Exception as e:
    print("Failed to unmount SD card:", e)
    # Exit if cannot unmount SD card
    raise
