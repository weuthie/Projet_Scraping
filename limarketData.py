
from bs4 import BeautifulSoup
import requests
from createdb import Limarket,db



headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
urls=['https://limarketsn.net/Fournisseur/fayeabdoulaye45gmail-com/section/334/',
    'https://limarketsn.net/Fournisseur/fayeabdoulaye45gmail-com/section/334/page/2/',
    'https://limarketsn.net/Fournisseur/fayeabdoulaye45gmail-com/section/334/page/3/']

for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    produits = soup.find_all(class_="product-inner")
    for produit in produits:
        image= produit.find(class_="product-image").find("a").find(class_="inner").find("img")["src"]
        namee=produit.find(class_="woocommerce-loop-product__title").getText().lower()
        prix = produit.find("bdi").getText()
        donnee_limarket = Limarket(li_name=namee,li_prix=prix,li_image=image)
        db.session.add(donnee_limarket)
        db.session.commit()


