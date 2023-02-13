# This file is executed on every boot (including wake-boot from deepsleep)

import sys
from machine import I2C, ADC, Pin, Timer
import display
import time
import ads1x15
from array import array
import ujson

# Set up config file
config_name = "config.json"
try:
        with open(config_name, "r") as f:
                config = ujson.loads(f.read())
except:
        print("No existing config file found. Loading default values")
        config = {
                "R_shunt_ohms": 119,
                "ADC_counts_per_volt": 1000,
                "s1_name":"Sensor 1",
                "s1_scaling_kPa_per_mA": 172.36875,
                "s1_offset_kPa": -689.475
        }

def write_config():
        with open(config_name, "w") as f:
                f.write(ujson.dumps(config))

def update_config(key, value):
        config[key] = value
        write_config()

def get_config_value(key):
        return config.get(key)

write_config()

# Set up display
sys.path[1] = '/flash/lib'

tft = display.TFT()
tft.init(tft.ST7789, bgr = False, rot = tft.LANDSCAPE_FLIP, miso = 17, 
        backl_pin = 4, backl_on = 1, mosi = 19, clk = 18, cs = 5, dc = 16)

tft.setwin(52, 40, 240, 320) # landscape: 40, 52, 320, 240)

tft.set_bg(0xFFFFFF - tft.BLACK)
tft.clear()
print(tft.fontSize())

# Set up ADC
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)

gain = 0
address = 72

adc = ads1x15.ADS1115(i2c, address, gain)

# For internal ADC
# adc = ADC(36)

# Set up buttons

left_button = Pin(0, Pin.IN)
right_button = Pin(35, Pin.IN)

