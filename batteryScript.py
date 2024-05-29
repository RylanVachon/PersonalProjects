from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

from adafruit_lc709203f import LC709203F
red = Pin(27, Pin.OUT)
blue = Pin(26, Pin.OUT)
Dis=I2C(1,sda=Pin(18), scl=Pin(19), freq=400000)
display = SSD1306_I2C(128, 64, Dis)



battPer = 10
x = 0
while x == 0:
    while x == 0:
        battPer=str(battPer)
        display.text('Current %:  '+battPer+'%', 0, 38, 1)
        battPer=int(battPer)
        progBar = battPer*1.24
        progBar = int(progBar)
        display.hline(2,53,progBar,1)
        display.hline(2,54,progBar,1)
        display.hline(2,55,progBar,1)
        display.hline(2,56,progBar,1)
        display.hline(2,57,progBar,1)
        display.hline(2,58,progBar,1)
        display.hline(2,59,progBar,1)
        display.hline(2,60,progBar,1)
        display.hline(2,61,progBar,1)
        display.hline(0,63,128,1)
        display.hline(0,51,128,1)
        display.vline(0,52,12,1)
        display.vline(127,52,12,1)
        display.text('Current V: 3.12V', 0, 24, 1)
        if battPer < 50:
            display.text('SLEEPING', 32,6,1)
            display.hline(27,0,74,1)
            display.hline(31,3,66,1)
            display.hline(31,15,66,1)
            display.hline(27,18,74,1)
        else:
            display.text('RUNNING', 36,6,1)
            display.hline(31,0,66,1)
            display.hline(27,3,74,1)
            display.hline(27,15,74,1)
            display.hline(31,18,66,1)
        display.show()
        if battPer < 30:
            red.value(1)
            blue.value(0)
        elif battPer > 30:
            red.value(0)
            blue.value(1)
        time.sleep(1)
        display.fill(0)
    

