import os


if __name__ == "__main__":

    print("Welcome to the Champions League!")

    n = input("Input 1: ")
    if n == 1:
        os.system("cls") #clear


    print("so?")
    file = open("commands_list.txt", "w")
    file.write("test")
    file.close()