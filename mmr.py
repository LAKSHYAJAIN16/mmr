from random import random
from default_human_phrases import get_hp
import keyboard
import math
import time

# The Commands you want to run (NOTE : don't use commands like search or pm as they require user interaction)
COMMANDS = [
    "beg",
    "hunt",
    "fish",
    "dig"
]

# The Command interval (set to 45 seconds as default to allow for beg)
COMMAND_INTERVAL = 45.0

# The Amount you want to gamble (make it zero to not gamble)
GAMBLE_AMMOUNT = "1k"

# If you want to write human phrases to make it look natural
WRITE_HUMAN_PHRASES = True

# If you want to include the default phrases included with MMR
USE_DEFAULT_HUMAN_PHRASES = True

# Any other Phrases
OTHER_HUMAN_PHRASES = [
    "yo guys wanna vc?",
    "bruh",
    "why am i so lucky",
    "wanna play stumble guys?",
    "stumble",
    "anyone want a banknote?"
]

first = True
while True:
    starttime = time.time()
    if first == False:
        time.sleep(45.0 - ((time.time() - starttime) % 60.0))
    elif first == True:
        time.sleep(3)
        first = False 

    dr = random() >= 0.5
    ri = math.floor(random() * 3 + 1) 
    phrases = get_hp() and OTHER_HUMAN_PHRASES
    keyboard.write("pls beg")
    keyboard.press_and_release("enter")
    if(dr and ri == 1 and WRITE_HUMAN_PHRASES == True):
        time.sleep(3)
        keyboard.write(phrases[math.floor(random() * len(OTHER_HUMAN_PHRASES))])
        keyboard.press_and_release("enter")

    time.sleep(2)
    keyboard.write("pls fish")
    keyboard.press_and_release("enter")

    if(dr and ri == 2 and WRITE_HUMAN_PHRASES == True):
        time.sleep(3)
        keyboard.write(phrases[math.floor(random() * len(OTHER_HUMAN_PHRASES))])
        keyboard.press_and_release("enter")

    time.sleep(2)
    keyboard.write("pls hunt")
    keyboard.press_and_release("enter")

    if(dr and ri == 3 and WRITE_HUMAN_PHRASES == True):
        time.sleep(3)
        keyboard.write(phrases[math.floor(random() * len(OTHER_HUMAN_PHRASES))])
        keyboard.press_and_release("enter")


    time.sleep(2)
    keyboard.write("pls dig")
    keyboard.press_and_release("enter")
