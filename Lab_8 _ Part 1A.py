# Lab 8 Part 1A
# Corey Biluk
# February 22, 2021

from guizero import App, Slider, TextBox

# Main Program    
if __name__ == '__main__':
    
    app = App(title = "RC Servo ControlPOS")
    slider1 = Slider(app, start=-90, end = 90, width=400)
    slider2 = Slider(app, start=-90, end = 90, width=400)
    app.display()

