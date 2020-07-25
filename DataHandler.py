from models.Product import Product
from models.Brand import Brand
from models.Retailer import Retailer


def create_product(row):
    brand_id = None
    retailer_id = None

    if len(row['brand']) > 0:
        b = Brand.first_or_create(
            name=row['brand']['name'].strip()
        )
        brand_id = b.id

    if len(row['retailer']) > 0:
        r = Retailer.first_or_create(
            name=row['retailer']['name'].strip(),
            slug=row['retailer']['slug'].strip(),
            website=row['retailer']['website'].strip()
        )
        retailer_id = r.id

    if Product.where('source_product_id', row['product_id']).count() == 0:
        Product.create(
            source_product_id=row['product_id'],
            brand_id=brand_id,
            retailer_id=retailer_id,
            name=row['name'],
            description=row['description'],
            thumb=row['thumb'],
            affiliate_link=row['affiliate_link'],
            source=row['retailer_link'],
            tags=row['tags'],
            price=row['usd_price'],
        )


def insert_all_products(rows):
    for row in rows:
        create_product(row)
