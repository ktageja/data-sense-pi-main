import machine
import utime

# Setup ADC
adc = machine.ADC(26) # GPIO 26, Pin 31

while True:
    # lower voltage = higher moisture
    moisture_value = adc.read_u16()  # Read ADC value (0-65535)
    voltage = moisture_value * 3.3 / 65535  # Convert ADC value to voltage
    print(f"Moisture Level: {moisture_value}, Voltage: {voltage:.2f}V")
    utime.sleep(1) 