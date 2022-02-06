# Uses Pynput for the input
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
iters = 0
first = True

while True:
    starttime = time.time()
    if first == False:
        time.sleep(45.0 - ((time.time() - starttime) % 60.0))
    elif first == True:
        time.sleep(3)
        first = False

    iters = iters + 1
    keyboard.press("p")
    keyboard.press("l")
    keyboard.press("s")
    keyboard.press(Key.space)
    keyboard.press("b")
    keyboard.press("e")
    keyboard.press("g")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # Dig
    keyboard.press("p")
    keyboard.press("l")
    keyboard.press("s")
    keyboard.press(Key.space)
    keyboard.press("d")
    keyboard.press("i")
    keyboard.press("g")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # Hunt
    keyboard.press("p")
    keyboard.press("l")
    keyboard.press("s")
    keyboard.press(Key.space)
    keyboard.press("h")
    keyboard.press("u")
    keyboard.press("n")
    keyboard.press("t")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # Fish
    keyboard.press("p")
    keyboard.press("l")
    keyboard.press("s")
    keyboard.press(Key.space)
    keyboard.press("f")
    keyboard.press("i")
    keyboard.press("s")
    keyboard.press("h")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # Iters
    keyboard.press("b")
    keyboard.press("o")
    keyboard.press("t")
    keyboard.press(Key.space)
    keyboard.press("i")
    keyboard.press("t")
    keyboard.press("e")
    keyboard.press("r")
    keyboard.press(Key.space)

    act: str = str(iters)
    for i in act:
        keyboard.press(i)
        keyboard.release(i)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)