import requests


def wallpaper_data(url):
    res = requests.get(url)
    json_data = res.json()

    last_page_number = json_data["meta"].get("last_page")
    download_path = []

    if len(json_data["data"]) > 0:
        for wallpaper in json_data["data"]:
            download_path.append(wallpaper["path"])

    data = {"wallpaper_urls": download_path, "last_page": last_page_number}

    return data
