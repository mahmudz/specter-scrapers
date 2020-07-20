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

class Brand(Model):
    __table__ = 'brands'
    __timestamps__ = False
    __fillable__ = ['name']