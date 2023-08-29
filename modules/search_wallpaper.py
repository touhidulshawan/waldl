from modules.wallpaper_data import wallpaper_data


def search_wallpaper(query: dict, page_number=1):
    if query.get("purity_choice") == 1:
        url = f"https://wallhaven.cc/api/v1/search?q={query.get('q')}&resolutions=1920x1080&ratios=16x9&purity=100&sorting={query.get('sort')}&order=desc&page={page_number}"
        return wallpaper_data(url)
    elif query.get("purity_choice") == 2:
        url = f"https://wallhaven.cc/api/v1/search?q={query.get('q')}&resolutions=1920x1080&ratios=16x9&purity=010&sorting={query.get('sort')}&order=desc&page={page_number}&apikey={query.get('api_key')}"
        return wallpaper_data(url)
    elif query.get("purity_choice") == 3:
        url = f"https://wallhaven.cc/api/v1/search?q={query.get('q')}&resolutions=1920x1080&ratios=16x9&purity=001&sorting={query.get('sort')}&order=desc&page={page_number}&apikey={query.get('api_key')}"
        return wallpaper_data(url)
    elif query.get("purity_choice") == 4:
        url = f"https://wallhaven.cc/api/v1/search?q={query.get('q')}&resolutions=1920x1080&ratios=16x9&purity=111&sorting={query.get('sort')}&order=desc&page={page_number}&apikey={query.get('api_key')}"
        return wallpaper_data(url)
    else:
        print("Incorrect choice!! Try again.")
