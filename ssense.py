# https://www.ssense.com/en-bd/men.json?page=2
# https://www.ssense.com/en-bd/women.json?page=2

import requests
import json

from models.Product import Product
from models.Brand import Brand
from models.Retailer import Retailer
s = requests.Session() 


def saveMaleProducts():
	allProductsRequest = requests.get('https://www.ssense.com/en-bd/men.json', headers={"content-type":"text"})
	url = "https://www.ssense.com/en-bd/men.json"
	headers = {
	  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1 RuxitSynthetic/1.0 v5749668456 t1099441676816697146'
	}
	url = 'https://www.ssense.com/en-bd/men.json?page=2'
	r = s.get(url, headers = headers)
	print(r.text.encode('utf8'))

saveMaleProducts()