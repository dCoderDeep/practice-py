# This code works in Jupyter Notebook

import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_names = []

for page in range(1, 6):  # Scraping the first 5 pages for demonstration
    url = f"https://www.flipkart.com/search?q=mobile+under+15000+rs&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_11_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+under+15000+rs%7CMobiles&requestId=76f6dd91-ebb7-4733-a5be-eea0f93fe610&as-backfill=on&page={page}"
    r = requests.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        name_div = soup.find_all("div", class_="_4rR01T")
        names = [name.text for name in name_div]
        Product_names.extend(names)   # Extend the list instead of reassigning it
    else:
        print(f"Failed to retrieve page {page}")

print(names)
print("\n")
print(f"This data is of page number: {page}")
print("\n")
print(Product_names)