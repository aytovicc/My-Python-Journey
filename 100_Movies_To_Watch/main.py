import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movie_list = []

for movie in movies:
    movie_list.append(movie.getText())


movie_list.reverse()


with open("100_Movies_To_Watch/top100_movie.txt", "w", encoding="utf8") as file:
    for movie in movie_list:
        file.write(movie+"\n")
    file.close()
