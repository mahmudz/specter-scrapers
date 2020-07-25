url = "https://www.farfetch.com/plpslice/listing-api/products-facets?page=2&view=180&scale=280&pagetype=Set&gender=Women&pricetype=FullPrice&setId=9644"

import requests


def save_male_products():
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
                'brand': {
                    'name': product['brand']['name'],
                },
                'retailer': {

                },
                'thumb': product['images']['model'],
                'tags': 'female',
                'original_currency': product['attributes']['original_currency'],
                'prices': product['priceInfo']['finalPrice'],
                'usd_price': product['priceInfo']['finalPrice'],
                'retailer_website': product['attributes']['retailer_website'],
                'retailer_link': product['attributes']['retailer_link'],
                'affiliate_link': product['attributes']['affiliate_link'],
            }

            rows.append(row)
            print(rows)

            break


save_male_products()
