from bs4 import BeautifulSoup
import requests
from createdb import Soumary,db

#test
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

urls=["https://www.soumari.com/categorie-produit/smartphones-haut-de-gamme/iphone/",
    "https://www.soumari.com/categorie-produit/smartphones-haut-de-gamme/iphone/page/2/"]

for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    produits = soup.find_all(class_="product-inner")
    for produit in produits:
        image = produit.find("img")["src"]
        namee = produit.find(class_="woo-loop-product__title").find("a").getText().lower()
        prix = produit.find("bdi").getText()
        donnee_soumary = Soumary(soumary_name=namee,soumary_prix=prix,soumary__image=image)
        db.session.add(donnee_soumary)
        db.session.commit()
    
