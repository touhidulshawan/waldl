import os
from collpy import cprint

api_key = ""

# check if api key exist or not

if os.path.exists("./api_key"):
    with open("./api_key", "r") as file:
        api_key = file.read()
        file.close()
else:
    api_key = input("Enter your api key: ")
    save_api_choice = input("Save your api key on file: (y/n) ")
    # save api key to file
    if save_api_choice.lower() == "y":
        with open("api_key", "w") as file:
            file.write(api_key)
            cprint(txt="Api key saved on file", color="green")
            file.close
