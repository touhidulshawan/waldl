from collpy import cprint
import os

# change this location according to your preference
home_directory = os.path.expanduser("~")
image_save_path = f"{home_directory}/Pictures/Wallhaven/"
# check wallhaven folder exist not
isExist = os.path.exists(image_save_path)

if isExist:
    cprint(txt="Wallhaven directory found", color="green")
    pass
else:
    os.mkdir(f"{home_directory}/Pictures/Wallhaven")
    cprint(txt="Wallhaven directory created successfully", color="green")
