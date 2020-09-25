import requests
import pandas as pd
import re
from bs4 import BeautifulSoup


def product():
    url = "https://www.amazon.fr/ASUS-ZEPHYRUS-G14-GA401IH-007T-Portable-R7-4800HS-NVIDIA-GeForce-GTX-1650/dp/B08BG8DV51/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=asus%2Bzephyrus%2Bg14&qid=1601059241&sr=8-1&th=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        }
    details = {'Title': "", "Price": 0, "Deal": True, "Budget": "" , "url": ""}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html5lib")
    title = soup.find(id="productTitle")
    title = title.get_text().strip()
    price = soup.find(id="priceblock_dealprice")
    budget = 1100

    if price is None:
        price = soup.find(id="priceblock_ourprice")
        details["deal"] = False
    if title is not None and price is not None:
        details["Title"] = ''.join(title.split()[:3])
        details["Price"] = price_converter(price.get_text())
        details["url"] = url
        details["budget"] = budget

    datasheet = pd.DataFrame([details])
    datasheet.to_csv(r"C:\Users\xatom\Desktop\AmazonTracker\AsusZephyrusG14.csv", mode='a' , index=False , header=False)
    print(datasheet)

    return details

def price_converter(price):
    price = re.sub("\D","", price)
    return price
    

product()



