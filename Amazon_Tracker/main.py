import requests
from bs4 import BeautifulSoup

amazon_url = "https://www.amazon.com/dp/B095QN9WHH?tag=camelweb-20&linkCode=ogi&th=1&language=en_US"
User_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"
Accept_language = "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"

response = requests.get(amazon_url, headers= {
    "User-Agent" : User_agent,
    "Accept_Language" : Accept_language
})


soup = BeautifulSoup(response.text , "html.parser")
print(soup.prettify())
