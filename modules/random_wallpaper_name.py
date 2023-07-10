from random import choices
from string import ascii_lowercase, digits


def wallpaper_name():
    return "".join(choices(ascii_lowercase + digits, k=8))
