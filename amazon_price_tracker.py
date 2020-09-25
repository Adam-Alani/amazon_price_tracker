import requests
import pandas as pd
import re
from bs4 import BeautifulSoup


def product():
    url = ""
    headers = {
        "User-Agent": ""
        }
    details = {'Title': "", "Price": 0, "Deal": True, "Budget": "" , "url": ""}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html5lib")
    title = soup.find(id="productTitle")
    title = title.get_text().strip()
    price = soup.find(id="priceblock_dealprice")
    budget = 1000

    if price is None:
        price = soup.find(id="priceblock_ourprice")
        details["deal"] = False
    if title is not None and price is not None:
        details["Title"] = ''.join(title.split()[:3])
        details["Price"] = price_converter(price.get_text())
        details["url"] = url
        details["budget"] = budget

    datasheet = pd.DataFrame([details])
    datasheet.to_csv(r"C:\Users\xatom\Desktop\AmazonTracker\Datasheet.csv", mode='a' , index=False , header=False)
    print(datasheet)

    return details

def price_converter(price):
    price = re.sub("\D","", price)
    return price
    

product()



