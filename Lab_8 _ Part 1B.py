# Lab 8 Part 1B
# Corey Biluk
# February 22, 2021

from guizero import App, Slider
from gpiozero import AngularServo
from time import sleep

# Servo calibration
maxPulseW = 2.4/1000
minPulseW = .4/1000

# Function to control Servo with fader
def servo_control1(s1_value):
    angle = float(s1_value)
    s1 = AngularServo(17, min_pulse_width = minPulseW, max_pulse_width = maxPulseW)
    s1.angle = angle
    sleep(0.5)
    
def servo_control2(s2_value):
    angle = float(s2_value)
    s2 = AngularServo(27, min_pulse_width = minPulseW, max_pulse_width = maxPulseW)
    s2.angle = angle
    sleep(0.5)
    
# Main Program    
if __name__ == '__main__':
    
    app = App(title = "Servo Control Faders")
    slider1 = Slider(app, start=-90, end=90, width=400, command=servo_control1)
    slider2 = Slider(app, start=-90, end=90, width=400, command=servo_control2)
    app.display()