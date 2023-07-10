from collpy import cprint
from progressbar import (
    ProgressBar,
    Percentage,
    FileTransferSpeed,
    ReverseBar,
    DataSize,
    AnimatedMarker)
import os
import requests

import modules.query_action as query
import modules.search_wallpaper as sw
import modules.checkpoint as checkpoint
from modules.random_wallpaper_name import wallpaper_name


# download wallpaper


def download_wallpaper(wallpaper_url):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    extension = os.path.splitext(wallpaper_url)[1]
    save_path = f"{checkpoint.image_save_path}{wallpaper_name()}{extension}"

    widgets = ['[ ', AnimatedMarker(), ' ]', FileTransferSpeed(), ' ', ReverseBar(),
               '< ', Percentage(), ' >  ', DataSize()]

    progress_bar = ProgressBar(widgets=widgets, maxval=total_size).start()
    downloaded_size = 0

    with open(save_path, 'wb') as file:
        for data in response.iter_content(block_size):
            downloaded_size += len(data)
            file.write(data)
            progress_bar.update(downloaded_size)

    progress_bar.finish()


try:
    page_range = input("How many pages [ex: 1-4]: ")
    first_number, second_number = page_range.split("-")

    cprint(
        txt=f"Wallpaper will save on {checkpoint.image_save_path}", color="blue")

    for page_number in range(int(first_number), int(second_number) + 1):
        data = sw.search_wallpaper(query.query_options, page_number)
        wallpaper_urls = data["wallpaper_urls"]

        if len(wallpaper_urls) > 0 and page_number <= query.last_page_number:
            cprint(
                txt=f"[+] Downloading wallpapers of page: {page_number}", color="purple"
            )
            for url in wallpaper_urls:
                download_wallpaper(url)
        elif page_number > query.last_page_number:
            cprint(
                txt=f"Total Page found : {query.last_page_number}", color="orange")
            break
        else:
            cprint(
                txt=f"404:: No image found for : {query.query_options}", color="red")
            break

except ValueError:
    cprint(txt="Invalid page number. Please type like [1-10]", color="red")
