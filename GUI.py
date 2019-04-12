from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Hardware
led = LED(14)
led2 = LED(15)

# GUI definittionds
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

#Event
def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"] = "Turn LED on"
    else:
        led.on()
        ledButton["text"] = "Turn LED off"

def ledToggle2():
    if led2.is_lit:
        led2.off()
        ledButton["text"] = "Turn LED on"
    else:
        led2.on()
        ledButton["text"] = "Turn LED off"

#def close():
  #  RPi.GPIO.cleanup()
        

# Widgets
ledButton = Button(win, text = 'Turn LED on', font = myFont, command = ledToggle, bg = 'red', height = 1, width = 24)
ledButton.grid(row=0, column=1)

ledButton2 = Button(win, text = 'Turn LED on', font = myFont, command = ledToggle2, bg = 'green', height = 1, width = 24)
ledButton2.grid(row=1, column=1)


