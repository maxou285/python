from bs4 import BeautifulSoup
import requests


#reponse = requests.get("https://codeavecjonathan.com/res/exemple.html")
#reponse = requests.get("https://www.codingforentrepreneurs.com/courses/")
reponse = requests.get("https://projecteuler.net/thread=824")
print(reponse.text)
soup = BeautifulSoup(reponse.text, "html.parser")

titre_h1 = soup.find("h1")
print("Titre : " + titre_h1.text) 