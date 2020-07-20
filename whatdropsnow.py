import requests
import json
from orator import DatabaseManager, Model
config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'specter',
        'user': 'root',
        'password': '',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)

class Product(Model):
    __table__ = 'products'
    __fillable__ = ['source_product_id','brand_id','retailer_id','name','description','thumb','affiliate_link','source','tags','price']

class Brand(Model):
    __table__ = 'brands'
    __timestamps__ = False
    __fillable__ = ['name']

class Retailer(Model):
    __table__ = 'retailers'
    __timestamps__ = False
    __fillable__ = ['name', 'slug', 'website']


ROOT_URL = 'https://www.whatdropsnow.com'

# API V1 also works
API_URL = {
	"all_products" : "https://www.whatdropsnow.com/api/v2/products.json?include=featured_brand%2Cbest_offer%2Ccategories&page=4&page_size=50&stream=latest",
	"product_search" : "https://www.whatdropsnow.com/api/v2/searches/product_search.json?include=featured_brand%2Cbest_offer%2Ccategories&page=1&page_size=72&q=adidas%20Originals",
	"brand_search" : "https://www.whatdropsnow.com/api/v2/searches/brand_search.json?page=1&page_size=72&q=adidas%20Originals",
	"user_search" : "https://www.whatdropsnow.com/api/v2/searches/user_search.json?page=1&page_size=1&q=adidas%20Originals"
}

allProductsRequest = requests.get(API_URL['all_products'])

if(allProductsRequest.status_code == 200):
	data = allProductsRequest.json()
	products = []
	retailer_products = []

	for product in data['data']:
		for item in data['included']:
			if(item['type'] == 'retailer_products'):
				if (item['attributes']['product_id'] == int(product['id'])):
					p = {
						'id' : product['id'],
						'name' : product['attributes']['name'],
						'release_at' : product['attributes']['release_at'],
						'thumb' : product['attributes']['product_images'][0]['original']['url'],
						'brand_names' : ' '.join(map(str, product['attributes']['brand_names'])),
						'product_id' : item['attributes']['product_id'],
						'original_currency' : item['attributes']['original_currency'],
						'prices' : item['attributes']['prices'],
						'usd_price' : item['attributes']['prices']['USD'],
						'retailer_website' : item['attributes']['retailer_website'],
						'retailer_link' : item['attributes']['retailer_link'],
						'affiliate_link' : item['attributes']['affiliate_link'],
						'release_at' : item['attributes']['release_at']
					} 
					b = Brand.first_or_create(
							name=p['brand_names'].strip()
						)

					r = Retailer.first_or_create(
							name=item['attributes']['retailer_name'].strip(),
							slug=item['attributes']['retailer_slug'].strip(),
							website=item['attributes']['retailer_website'].strip()
						)

					if(Product.where('source_product_id', p['product_id']).count() == 0):
						Product.create(
								source_product_id=p['product_id'],
								brand_id=b.id,
								retailer_id=r.id,
								name=p['name'],
								description='',
								thumb=p['thumb'],
								affiliate_link=p['affiliate_link'],
								source=p['retailer_link'],
								tags='',
								price=p['usd_price'],
							)
