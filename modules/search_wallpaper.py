import requests


def search_wallpaper(query: dict, page_number=1):
    if query.get("nsfw") is True:
        url = f"https://wallhaven.cc/api/v1/search?q={query.get('q')}&resolutions=1920x1080&ratios=16x9&purity=001&sorting={query.get('sort')}&order=desc&page={page_number}&apikey={query.get('api_key')}"
    else:
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
