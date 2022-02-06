import keyboard
import time

first = True

# Main Loop which types the characters
while True:
    starttime = time.time()
    if first == False:
        time.sleep(45.0 - ((time.time() - starttime) % 60.0))
    elif first == True:
        time.sleep(3)
        first = False

    keyboard.write("pls beg")
    keyboard.press_and_release("enter")

    keyboard.write("pls fish")
    keyboard.press_and_release("enter")

    keyboard.write("pls hunt")
    keyboard.press_and_release("enter")

    keyboard.write("pls dig")
    keyboard.press_and_release("enter")