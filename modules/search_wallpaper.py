from modules.wallpaper_data import wallpaper_data


def search_wallpaper(query: dict, page_number=1):
    search_keyword = query.get("q")
    width = query.get("width")
    height = query.get("height")
    sort = query.get("sort")
    apikey = query.get("api_key")

    if query.get("purity_choice") == 1:
        url = f"https://wallhaven.cc/api/v1/search?q={search_keyword}&resolutions={width}x{height}&purity=100&sorting={sort}&order=desc&page={page_number}"
        return wallpaper_data(url)
    elif query.get("purity_choice") == 2:
        url = f"https://wallhaven.cc/api/v1/search?q={search_keyword}&resolutions={width}x{height}&purity=010&sorting={sort}&order=desc&page={page_number}&apikey={apikey}"
        return wallpaper_data(url)
    elif query.get("purity_choice") == 3:
        url = f"https://wallhaven.cc/api/v1/search?q={search_keyword}&resolutions={width}x{height}&purity=001&sorting={sort}&order=desc&page={page_number}&apikey={apikey}"
        return wallpaper_data(url)
    elif query.get("purity_choice") == 4:
        url = f"https://wallhaven.cc/api/v1/search?q={search_keyword}&resolutions={width}x{height}&purity=111&sorting={sort}&order=desc&page={page_number}&apikey={apikey}"
        return wallpaper_data(url)
    else:
        print("Incorrect choice!! Try again.")
