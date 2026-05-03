import os
from collpy import cprint
import modules.user_choice as uc

api_key = ""

# need api_key when user only search by keyword and NSFW images

if uc.search_by == "k":
    # check if api key exist or not

    if os.path.exists("./api_key"):
        with open("./api_key", "r") as file:
            api_key = file.read()
            file.close()
    else:
        if uc.purity_choice == 3:
            cprint(
                txt="WARNING!! To download NSFW wallpapers you need an api key. You can find your key at your account on wallhaven.cc",
                color="red",
            )
            api_key = input("Enter your api key: ")
            save_api_choice = input("Save your api key on file: (y/n) ")
            # save api key to file
            if save_api_choice.lower() == "y":
                with open("api_key", "w") as file:
                    file.write(api_key)
                    cprint(txt="Api key saved on file", color="green")
                    file.close()
