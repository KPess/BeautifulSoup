""" 
    import requests
    from bs4 import BeautifulSoup

    # Make a request
    page = requests.get(
        "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Create all_h1_tags as empty list

    all_h1_tags = []
    # Set all_h1_tags to all h1 tags of the soup
    for h1 in soup.select('h1'):
        all_h1_tags.append(h1.text)
    # Create seventh_p_text and set it to 7th p element text of the page
    seventh_p_text = ''
    seventh_p_text = soup.select('p')[6].text

    print(all_h1_tags[0])
    print(all_h1_tags[1])
    print(all_h1_tags)
    print(seventh_p_text)

 """
""" 
import requests
from bs4 import BeautifulSoup
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as empty list
top_items = []

# Extract and store in top_items according to instructions on the left

products = soup.select('div.thumbnail')

for bacon in products:
    title = bacon.select('a.title')[0].text
    review = bacon.select('div.ratings > p.pull-right')[0].text
    top_items.append({
        "title": title.strip(),
        "review": review.strip()
    })

print(top_items) """
""" 
import requests
from bs4 import BeautifulSoup
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create all_links as empty list
all_links = []

# Extract and store in all_links according to instructions on the left
links = soup.select('a')
for a in links:
    href = a.get('href')
    href = href.strip() if href is not None else ''
    text = a.text
    text = text.strip() if text is not None else ''
    all_links.append({"href": href, "text": text})
print(all_links) """

import requests
from bs4 import BeautifulSoup
import csv
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

all_products = []

products = soup.select('div.thumbnail')
for product in products:
    title = product.select('a.title')[0].text.strip()
    price = product.select('h4.price')[0].text.strip()
    desc = product.select('p.description')[0].text.strip()
    reviews = product.select('p.pull-right')[0].text.strip()
    image = product.select('img')[0].get('src')
    print(title, price, desc, reviews, image)

    all_products.append({
        "Product Name": title,
        "Price": price,
        "Description": desc,
        "Reviews": reviews,
        "Product Image": image
    })
    print(all_products)
    print("Work on product here")
    print("Product Name")

keys = all_products[0].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)
