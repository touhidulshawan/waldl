#!/usr/bin/env python3

import threading
import requests
from random import choices
from string import ascii_lowercase, digits
import os
import time


# search wallpaper


def search_wallpaper(query, page_number):
    url = f"https://wallhaven.cc/api/v1/search?q={query}&atleast=1920x1080&ratios=16x9&sorting=views&order=desc&page={page_number}"
    res = requests.get(url)
    json_data = res.json()

    download_path = []

    for wallpaper in json_data["data"]:
        download_path.append(wallpaper["path"])

    return download_path


# generate random name


def wallpaper_name():
    return "".join(choices(ascii_lowercase + digits, k=8))


# download wallpaper


def download_wallpaper(wallpaper_url):
    res = requests.get(url=wallpaper_url)
    extension = os.path.splitext(wallpaper_url)[1]
    save_path = f"/home/shawan/Pictures/wallhaven/{wallpaper_name()}{extension}"
    open(save_path, "wb").write(res.content)


query = input("Enter wallpaper name keyword: ")
page_number = input("Enter page number: ")
wallpaper_urls = search_wallpaper(query, page_number)


if len(wallpaper_urls) != 0:
    for url in wallpaper_urls:
        print(f"Downloading wallpaper: [{url}]")
        t = threading.Thread(target=download_wallpaper, args=(url,))
        t.start()

else:
    print("Invalid wallpaper name or page number!! Try again.")
