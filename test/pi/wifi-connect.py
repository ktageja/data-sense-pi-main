
# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Performs a GET request (loads a webpage)
# - Queries the current time from a server

import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Fill in your network name (ssid) and password here:
ssid = ''
password = ''
wlan.connect(ssid, password)


# Example 1. Make a GET request for Postman and print HTML
# Print the html content from Postman
print("1. Querying https://www.postman-echo.com/get: ")
r = urequests.get("https://www.postman-echo.com/get")
print(r.content)
r.close()

# Example 2. urequests can also handle basic json support! Let's get the current time from a server
print("\n\n2. Querying the current GMT+0 time:")
r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
print(r.json())