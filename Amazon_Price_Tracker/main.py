import requests
from bs4 import BeautifulSoup
import smtplib


amazon_url = "https://www.amazon.com/dp/B095QN9WHH?tag=camelweb-20&linkCode=ogi&th=1&language=en_US"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    "Accept_Language" : "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
}

wanted_price = 36

response = requests.get(amazon_url, headers = headers)

soup = BeautifulSoup(response.text, "html.parser")

item_id = soup.find(name= "h1" , class_ = "a-spacing-none").get_text()

price_tag = soup.find(class_ = "a-offscreen")
price = float(price_tag.get_text().split("$")[1])


if price < wanted_price:

    my_email = "aytacpythontest@gmail.com"
    password = "lpdhqzjbbnomutox"

    contents = f"""The item you looking in Amazon is below the price you want.
     The item = {item_id} 
     Now its = {price}, The price you want = {wanted_price}"""

    with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="a.dursunoksuzoglu@hotmail.com",
            msg=f"Subject: Amazon Price Alert!\n\n {contents}"
        )