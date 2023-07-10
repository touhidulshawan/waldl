from collpy import cprint

example_tags = ["digital art", "anime", "nature", "landscape", "4k", "artwork"]
sorting_options = ["relevance", "hot",
                   "toplist", "views", "random", "date_added"]
cprint(txt=f"Some tags {example_tags}", color="blue")
tag_choice = input("[?] Enter wallpaper tag: ")
cprint(txt=f"Sorting options: {sorting_options}", color="green")
sorting_choice = input(
    "[?] Sort image by (default -> relevance): ") or "relevance"
nsfw_choice = input(
    "[?] Do you want to download NSFW [not safe for work]: (y/n): ") or "n"


# NSFW = not safe for work
is_nsfw = False
if nsfw_choice.lower() == "y":
    is_nsfw = True
elif nsfw_choice.lower() == "n":
    is_nsfw = False
else:
    cprint(txt="Incorrect choice!! Try agian.", color="red")
    exit(0)
