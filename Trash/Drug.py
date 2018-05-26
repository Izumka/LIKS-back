from flask_sqlalchemy import SQLAlchemy
from APP import APP


class DB:
    def __init__(self, app):
        self.db = SQLAlchemy(app)


idb = DB(APP().app)

class Drug(idb.db.Model):
    __tablename__ = 'drugs'
    id = idb.db.Column('id', idb.db.Integer, primary_key=True)
    dz_url = idb.db.Column(idb.db.String)
    name = idb.db.Column(idb.db.String)
    manufacturer = idb.db.Column(idb.db.String)
    composition = idb.db.Column(idb.db.String)
    popular_name = idb.db.Column(idb.db.String)
    expiration_date = idb.db.Column(idb.db.String)
    prescription = idb.db.Column(idb.db.Integer)
    release_type = idb.db.Column(idb.db.String)

    def __init__(self, dz_url, name, manufacturer, composition,
                 popular_name, prescription, expiration_date, release_type):
        self.dz_url = dz_url
        self.name = name
        self.manufacturer = manufacturer
        self.composition = composition
        self.popular_name = popular_name
        self.prescription = prescription
        self.expiration_date = expiration_date
        self.release_type = release_type



    def __repr__(self):
        return '{},{},{},{},{},{},{},{},{}'.format(
            self.id,
            self.dz_url,
            self.name,
            self.manufacturer,
            self.composition,
            self.popular_name,
            self.expiration_date,
            self.prescription,
            self.release_type)




