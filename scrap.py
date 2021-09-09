import requests
import bs4


res = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")

soup = bs4.BeautifulSoup(res.text , 'lxml')

#extracting thumbnails 
thumbs = soup.find_all('div' , class_='thumbnail')

#Making space in Memory
price = []
item_name = []
description = []
reviews = []

#extracting Data data from soup object
for thumb in thumbs:
    price.append(thumb.h4.text)
    item_name.append(thumb.a.text)
    description.append(thumb.p.text)
    reviews.append(thumb.find('div' , class_= 'ratings').text.replace("\n",""))

#time to save data into CSV or Show
for i , j , k ,l in zip(item_name , price , description , reviews):
    print(f'''
        Item_Name = {i}
        Price = {j}
        Description = {k}
        Reviews = {l}
    ''')   