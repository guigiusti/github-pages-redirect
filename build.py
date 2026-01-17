import json
import os

with open('redirects.json', 'r') as file:
    redirects = json.load(file)

with open('base.html', 'r') as file:
    base_html = file.read()

os.makedirs('public', exist_ok=True)

for redirect in redirects['redirects']:
    file_name = str("index" if "/" == redirect['location'] else redirect['location']).replace("/", "")
    with open(f'public/{file_name}.html', 'w') as file:
        file.write(base_html.format(url=redirect['redirect'], title=redirects['title'].format(page=file_name.capitalize())))