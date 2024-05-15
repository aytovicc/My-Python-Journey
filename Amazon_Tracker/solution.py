import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B095QN9WHH?tag=camelweb-20&linkCode=ogi&th=1&language=en_US"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
output = print(soup.prettify())

import pyperclip
pyperclip.copy(output)

# price = soup.find(class_="a-offscreen").get_text()
# price_without_currency = price.split("$")[1]
# price_as_float = float(price_without_currency)
# print(price_as_float)