from bs4 import BeautifulSoup
import requests

reponse = requests.get("https://codeavecjonathan.com/res/exemple.html")
print(reponse.text)
soup = BeautifulSoup(reponse.text, "html.parser")

titre_h1 = soup.find("h1")
print("Titre : " + titre_h1.text) 