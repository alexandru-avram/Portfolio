# ---------------------------- IMPORT SECTION ------------------------------- #
import json
import pandas as pd

# Add current PATH
from pathlib import Path
HERE = Path(__file__).resolve().parent

# Clear Screen
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Opening .json file
with open(HERE/"morse.json", "r") as morse_file:
     morse_code = json.load(morse_file)

is_on = True

logo =(r"""
.___  ___.   ______   .______          _______. _______      ______   ______    _______   _______      ______   ______   .__   __. ____    ____  _______ .______     .___________.  ______   .______      
|   \/   |  /  __  \  |   _  \        /       ||   ____|    /      | /  __  \  |       \ |   ____|    /      | /  __  \  |  \ |  | \   \  /   / |   ____||   _  \    |           | /  __  \  |   _  \     
|  \  /  | |  |  |  | |  |_)  |      |   (----`|  |__      |  ,----'|  |  |  | |  .--.  ||  |__      |  ,----'|  |  |  | |   \|  |  \   \/   /  |  |__   |  |_)  |   `---|  |----`|  |  |  | |  |_)  |    
|  |\/|  | |  |  |  | |      /        \   \    |   __|     |  |     |  |  |  | |  |  |  ||   __|     |  |     |  |  |  | |  . `  |   \      /   |   __|  |      /        |  |     |  |  |  | |      /     
|  |  |  | |  `--'  | |  |\  \----.----)   |   |  |____    |  `----.|  `--'  | |  '--'  ||  |____    |  `----.|  `--'  | |  |\   |    \    /    |  |____ |  |\  \----.   |  |     |  `--'  | |  |\  \----.
|__|  |__|  \______/  | _| `._____|_______/    |_______|    \______| \______/  |_______/ |_______|    \______| \______/  |__| \__|     \__/     |_______|| _| `._____|   |__|      \______/  | _| `._____|                                                                                                                                                                                                                                                                                                                                                                                                 
""")

# ---------------------------- RUN LOOP ------------------------------- #
while is_on:
    # Clear screen and logo
    clear()
    print(logo)
    print("\n")

    # Empty message and list
    message = ""
    message_list = []
    repeat = ""

    # Create new message
    message = input("Write your message bellow\n").upper()

    # Split message into a new list
    for character in message:
        message_list.append(character)

    # Create new dataFrame with new list
    message_df = pd.DataFrame(message_list, columns = ["MESSAGE CHARACTER"])
    message_df["MORSE CODE"] = message_df["MESSAGE CHARACTER"].map(morse_code).fillna("#ERROR: Invalid character.")  

    print("\n")
    print(message_df)

    print("\n\n")

    # Repeat or no loop
    while repeat not in ["Y","N"]:
        repeat = input("Do you want another message? Type 'Y' for 'YES', 'N' for 'NO'\n").upper()

    if repeat == "N":
        is_on = False
    else:
        pass

# ---------------------------- EXIT MESSAGE ------------------------------- #
clear()
print(logo)
print("\n\n")
input("Thank you. Press ENTER to exit...")