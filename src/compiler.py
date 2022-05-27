# make a new folder called "scripts"
import time
import os

def setup():
    # make a new folder called "scripts"
    os.mkdir("scripts")
    time.sleep(1)
    print("Scripts folder created!")
    time.sleep(1)
    print("Adding example files...")
    # add a example .2lang file
    with open("scripts/example.2lang", "w") as f: