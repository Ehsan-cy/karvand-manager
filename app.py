import json
import os

path = r"D:\Maktab_sharif\CW\karvand-manager\data\karvands.json"

# make folder if not exist
os.makedirs(os.path.dirname(path), exist_ok=True)

if not os.path.exists(path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump( {"karvands": []},file,ensure_ascii=False, indent=2)
           