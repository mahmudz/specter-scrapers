
import requests
from DataHandler import insert_all_products


### Gender: [Women, Men]
def get_products(gender = 'Men'):
    url = "https://www.farfetch.com/plpslice/listing-api/products-facets?page=2&view=180&scale=280&pagetype=Set&gender="+ gender +"&pricetype=FullPrice&setId=9644"
    allProductsRequest = requests.get(url)
    rows = []

    if allProductsRequest.status_code == 200:
        data = allProductsRequest.json()

        if data['listingItems']['items']:
            products = data['listingItems']['items']
        else:
            products = []

        for product in products:
            row = {
                'product_id': product['id'],
                'name': product['shortDescription'],
                'description': product['shortDescription'],
                'brand': {
                    'name': product['brand']['name'],
                },
                'retailer': {

                },
                'thumb': product['images']['model'],
                'tags': 'female',
                'original_currency': product['priceInfo']['currencyCode'],
                'prices': product['priceInfo']['finalPrice'],
                'usd_price': product['priceInfo']['finalPrice'],
                'retailer_link': '',
                'affiliate_link': product['url'],
            }

            rows.append(row)
        return rows

insert_all_products(get_products('Men'))
insert_all_products(get_products('Women'))


