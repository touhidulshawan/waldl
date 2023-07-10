from collpy import cprint
import modules.user_choice as uc
import modules.api_action as api
from modules.search_wallpaper import search_wallpaper


def total_pages(query):
    data = search_wallpaper(query, page_number=1)
    last_page_number = data["last_page"]
    return last_page_number


query_options = {
    "q": uc.tag_choice,
    "sort": uc.sorting_choice,
    "nsfw": uc.is_nsfw,
    "api_key": api.api_key,
}

last_page_number = total_pages(query_options)
cprint(txt=f"Total page found: {last_page_number}", color="blue")
