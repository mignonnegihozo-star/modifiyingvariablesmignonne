from microbit import *

# Initialize the variable
hungryness = 0

while True:
    if button_a.is_pressed():
        # Increase hungryness by 1
        hungryness += 1
        display.show(hungryness)
        # Optional: add a small sleep to prevent rapid counting
        sleep(200) 
        
    elif button_b.is_pressed():
        # Reset hungryness to 0
        hungryness = 0
        display.show(hungryness)
