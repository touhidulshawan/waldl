from collpy import cprint

example_tags = ["digital art", "anime", "nature", "landscape", "4k", "artwork"]
sorting_options = ["relevance", "hot", "toplist", "views", "random", "date_added"]
cprint(txt=f"Some tags {example_tags}", color="blue")
tag_choice = input("[?] Enter wallpaper tag: ")
cprint(txt=f"Sorting options: {sorting_options}", color="green")
sorting_choice = input("[?] Sort image by (default -> relevance): ") or "relevance"
print(
    """
      Image Purity Option: 
      1. SFW [Safe For Work]
      2. Sketchy
      3. NSFW [Not Safe For Work]
      4. All of them
      """
)
purity_choice = int(input("Enter you choice: "))
