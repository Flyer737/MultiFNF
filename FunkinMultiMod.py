#Friday Night Funkin mod manager :D
#Author: Flyer737
#I know this will become obsolete someday, but here we are anyway.
#For linux, uses wine. Easily portable to Windows.
#make the directory name the same as the .exe name

#Check if there is a file containing the directorys and executable names
#I'm pretty sure there is better way to do this.

import os

try:
    registers = open("registered_mods.txt","r")
    registers.close()
except FileNotFoundError:
    registers = open("registered_mods.txt","w")

    registers.close()

def cls():
    os.system("clear")

#MAIN LOGIC
cls()
running = True
while running:
    print("Funkin Multi Mod\n================\n")
    #Load directorys and exe names into memory
    file = open("registered_mods.txt","r")
    dirs_and_names = file.readlines()
    file.close()
    if len(dirs_and_names) < 2:
        print("Nothing has been registered!")
    else:
        for i in range(int(len(dirs_and_names)/2)):
            print(dirs_and_names[i*2])
    do = input("\n>").strip().lower()
    if do=="":
        cls()
    elif do=="exit" or do=="e":
        exit()
    else:
        os.system("cd "+do+" && wine "+do)
