#!/usr/bin/env python3

import requests
import shutil
from random import choices
from string import ascii_lowercase, digits
from collpy import cprint
from tqdm import tqdm
import os

# change this location according to your preference
home_directory = os.path.expanduser("~")
image_save_path = f"{home_directory}/Pictures/Wallhaven/"

# search wallpaper


def search_wallpaper(query: dict, page_number=1):
    url = f"https://wallhaven.cc/api/v1/search?q={query.get('q')}&resolutions=1920x1080&ratios=16x9&sorting={query.get('sort')}&order=desc&page={page_number}"
    res = requests.get(url)
    json_data = res.json()

    last_page_number = json_data["meta"].get("last_page")
    download_path = []

    if len(json_data["data"]) > 0:
        for wallpaper in json_data["data"]:
            download_path.append(wallpaper["path"])

    data = {"wallpaper_urls": download_path, "last_page": last_page_number}

    return data


# generate random name


def wallpaper_name():
    return "".join(choices(ascii_lowercase + digits, k=8))


# download wallpaper


def download_wallpaper(wallpaper_url):
    res = requests.get(url=wallpaper_url, stream=True)
    # show error on IDE but no error on running
    total_length = int(res.headers.get("Content-Length"))
    extension = os.path.splitext(wallpaper_url)[1]
    save_path = f"{image_save_path}{wallpaper_name()}{extension}"
    with tqdm.wrapattr(
        res.raw, "read", total=total_length, ascii=" C-", desc=""
    ) as raw:
        with open(save_path, "wb") as output:
            shutil.copyfileobj(raw, output)


def total_pages(query):
    data = search_wallpaper(query, page_number=1)
    last_page_number = data["last_page"]
    return last_page_number


example_tags = ["digital art", "anime", "nature", "landscape", "4k", "artwork"]
sorting_options = ["hot", "toplist", "views", "random", "date_added"]
cprint(txt=f"Some tags {example_tags}", color="blue")
tag_choice = input("Enter wallpaper tag: ")
cprint(txt=f"Sorting options: {sorting_options}", color="green")
sorting_choice = input("Sort image by: ")
query_options = {"q": tag_choice, "sort": sorting_choice}
last_page_number = total_pages(query_options)
cprint(txt=f"Total page found: {last_page_number}", color="blue")

# check wallhaven folder exist not
isExist = os.path.exists(image_save_path)

if isExist:
    cprint(txt="Wallhaven directory found", color="green")
    pass
else:
    os.mkdir(f"{home_directory}/Pictures/Wallhaven")
    cprint(txt="Wallhaven directory created successfully", color="green")

try:
    page_range = input("How many pages [ex: 1-4]: ")
    first_number, second_number = page_range.split("-")

    for page_number in range(int(first_number), int(second_number) + 1):
        data = search_wallpaper(query_options, page_number)
        wallpaper_urls = data["wallpaper_urls"]

        if len(wallpaper_urls) > 0 and page_number <= last_page_number:
            cprint(
                txt=f"[+] Downloading wallpapers of page: {page_number}", color="purple"
            )
            for url in wallpaper_urls:
                download_wallpaper(url)
        elif page_number > last_page_number:
            cprint(txt=f"Total Page found : {last_page_number}", color="orange")
            break
        else:
            cprint(txt=f"404:: No image found for : {query_options}", color="red")
            break
        cprint(txt=f"\nImages saved on {image_save_path}", color="green")

except ValueError:
    cprint(txt="Invalid page number. Please type like [1-10]", color="red")
