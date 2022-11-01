import requests
from bs4 import BeautifulSoup

reponse = requests.get("https://www.udemy.com")
#print(reponse.text)

soup = BeautifulSoup(reponse.text, "html.parser")
titre_h1 = soup.find("title")
#div1_image = soup.find("div", class_="main-content-wrapper")
print(titre_h1.text)
#image = div1_image.find("img")
#print(image["src"])
