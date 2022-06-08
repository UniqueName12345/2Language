# make a new folder called "scripts"
import time
import os

def setup():
    try:
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
    except FileExistsError:
        pass # we know the file already exists, so we can just call the compiler

def compiler(file_path):
    # if boilerplate is not present in the file, throw an error
    with open(file_path, "r") as f:
        contents = f.read()
        if "public prog" not in contents:
            print("Error: boilerplate not present in file!")
            return
    # if boilerplate is present, move onto the next step
    # check each line of the file
    with open(file_path, "r") as f:
        # if the line contains a comment, skip it
        if "&&" in f.readline():
            return
        # else if the line is a public prog, skip it
        elif "public prog" in f.readline():
            return
        # else if the line is "terminal.print", print the stuff inside the brackets
        elif "terminal.print" in f.readline():
            print(f.readline()[16:-2])
        # else if the line is "readInt()", ask the user for an integer
        # example:
        # readInt("Enter an integer: ")
        # Output:
        # 2LANGUAGE: Enter an integer: 5
        elif "readInt" in f.readline():
            # input() returns a string, so we need to convert it to an int
            print(f.readline()[11:-2])
            print(int(input()))
        # NOTE: The code is starting to get messy, but it works!

def main():
    setup()
    # ask the user for a file name
    file_path = input("Enter the file name: ")
    # search everywhere for a file with that exact name
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == file_path:
                file_path = f"{root}/{file}"
                break
    # if the file is not found, throw an error
    if not os.path.isfile(file_path):
        print("Error: file not found!")
        return
    # if the file exists, call the compiler
    compiler(file_path)

if __name__ == "__main__":
    main()