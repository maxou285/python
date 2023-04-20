from bs4 import BeautifulSoup

# Lecture des données HTML
f = open("site_recette/recette.html", "r")
html_content = f.read()
f.close()
 

soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1")
list_div_centre = soup.find_all("div", class_="centre")
if list_div_centre and len(list_div_centre) >= 2:
    paragraphe_description = list_div_centre[1].find("p",class_="description")
div_source_image = soup.find("div", class_="info")
source_image = div_source_image.find("img")



print("Titre de la page HTML : " + titre_h1.text)
print("Source de l'image  : " + source_image["src"])
if paragraphe_description:
    print("Description : " + paragraphe_description.text)