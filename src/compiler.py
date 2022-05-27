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
        # contents:
        # public prog HelloWorld() {
        #   terminal.print("Hello, world!");
        # }
        f.write("public prog HelloWorld() {\n")
        f.write("  terminal.print(\"Hello, world!\");\n")
        f.write("}\n")

def compiler(file_path):
    # if boilerplate is not present in the file, throw an error
    with open(file_path, "r") as f:
        contents = f.read()
        if "public prog" not in contents:
            print("Error: boilerplate not present in file!")
            return
        