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
