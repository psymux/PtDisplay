from machine import Pin
# import display
import time

# tft = display.TFT()
# tft.init(tft.ST7789, bgr = False, rot = tft.PORTRAIT_FLIP, miso = 17, 
#         backl_pin = 4, backl_on = 1, mosi = 19, clk = 18, cs = 5, dc = 16)

# tft.setwin(52, 40, 240, 320) #40, 52, 320, 240)

# tft.set_bg(0x000000)
# tft.clear()


tft.font(tft.FONT_DejaVu24)

def say(s):
    s = str(s)
    tft.text(5, 70, s, tft.BLACK)

def show_p(p):
    pressure = p
    pres_str = str(pressure)
    for i in range(4-len(pres_str)):
        pres_str = "0" + pres_str
    pres_str += " raw"
    tft.text(5, 40, pres_str, tft.BLACK)

def plot(x, y):
    tft.line(0,100,120,100)
    tft.line(0,160,120,160)
    tft.pixel(x, (60 - int(y/100)) + 100)
    tft.text(10, 200, str(x))

def get_adc():
    raw = -1*adc.read(2,0,1)
    return raw

def raw_to_p(raw):
    voltage = raw/get_config_value("ADC_counts_per_volt") 
    current = voltage/get_config_value("R_shunt_ohms")*1000 # mA
    pressure = current*get_config_value("s1_scaling_kPa_per_mA") + get_config_value("s1_offset_kPa")
    return pressure



i = 0
while True:
    if i < 120:
        i += 1
    else:
        tft.clear()
        i = 1
    raw = get_adc()
    p = raw_to_p(raw)
    say(p)
    show_p(p)
    plot(i, p)

    # if left_button.value() == 0:
    #     break
    time.sleep(0.05)



