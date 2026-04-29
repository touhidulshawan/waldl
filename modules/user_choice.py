import sys
from collpy import cprint

print(
    """
==================================
🄳🄾🅆🄽🄻🄾🄰🄳 🅆🄰🄻🄻🄿🄰🄿🄴🅁 🄵🅁🄾🄼 🅆🄰🄻🄻🄷🄰🅅🄴🄽
=================================="""
)

cprint(txt="--> Search by Tag ID: [press t] -->", color="green")
cprint(txt="--> Search by Keyword: [press k] --> ", color="blue")

search_by = input("=> : ").lower()

if search_by == "t":
    # search by tag id 
    tag_id = input("Enter the tag id: ")
elif search_by == "k":
    example_keyword = ["digital art", "anime",
                       "nature", "landscape", "4k", "artwork"]
    sorting_options = ["relevance", "hot",
                       "toplist", "views", "random", "date_added"]
    cprint(txt=f"Some tags {example_keyword}", color="blue")
    tag_choice = input("[?] Enter wallpaper search keyword: ")
    cprint(txt=f"Sorting options: {sorting_options}", color="green")
    sorting_choice = input(
        "[?] Sort image by (default -> relevance): ") or "relevance"
    print(
        """
    -------------------------------------
    | Image purity options - Default SFW |
    -------------------------------------
    =====================================
    1. SFW [Safe For Work]
    2. Sketchy
    3. NSFW [Not Safe For Work]
    4. All of them
    =====================================
    """
    )
    purity_choice = int(input("Enter you choice: ") or 1)
    
    resolution_width = 1920
    resolution_height = 1080
    print("\nDefault resolution: 1920x1080")
    resolution_choice = input("Custom resolution: (y/n): ") or "n"
    
    if resolution_choice.lower() == "y":
        resolution_width = int(input("Width: "))
        resolution_height = int(input("Height: "))
    elif resolution_choice.lower() == "n":
        print("Selecting default(1920x1080) resolution...")
    else:
        print("Selecting default(1920x1080) resolution...")
else:
    cprint(txt="Invalid selection", color="red")
    sys.exit()

