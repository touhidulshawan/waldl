from collpy import cprint

print(
    """
==================================
🄳🄾🅆🄽🄻🄾🄰🄳 🅆🄰🄻🄻🄿🄰🄿🄴🅁 🄵🅁🄾🄼 🅆🄰🄻🄻🄷🄰🅅🄴🄽
=================================="""
)

example_keyword = ["digital art", "anime", "nature", "landscape", "4k", "artwork"]
sorting_options = ["relevance", "hot", "toplist", "views", "random", "date_added"]
cprint(txt=f"Some tags {example_keyword}", color="blue")
tag_choice = input("[?] Enter wallpaper search keyword: ")
cprint(txt=f"Sorting options: {sorting_options}", color="green")
sorting_choice = input("[?] Sort image by (default -> relevance): ") or "relevance"
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
purity_choice = int(input("Enter you choice: ")) or 1

resulation_width = 1920
resulation_height = 1080
print("\nDefault resulation: 1920x1080")
resulation_choice = input("Custom resulation: (y/n): ") or "n"

if resulation_choice.lower() == "y":
    resulation_width = int(input("Width: "))
    resulation_height = int(input("Height: "))
elif resulation_choice.lower() == "n":
    print("Selecting default(1920x1080) resulation...")
else:
    print("Selecting default(1920x1080) resulation...")
