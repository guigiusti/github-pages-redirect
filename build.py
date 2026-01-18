import json
import os

with open("redirects.json", "r") as file:
    redirects = json.load(file)

with open("base.html", "r") as file:
    base_html = file.read()

os.makedirs("public", exist_ok=True)

for redirect in redirects["redirects"]:
    location = (
        "index" if "/" == redirect["location"] else redirect["location"].lstrip("/")
    )
    file_path = os.path.join("public", location.lower() + ".html")
    page_name = location.split("/")[-1].capitalize()
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        file.write(
            base_html.format(
                url=redirect["redirect"],
                title=redirects["title"].format(page=page_name),
            )
        )
