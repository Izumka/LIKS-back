import json


class Pill:
    def __init__(self, drug):
        self.dz_url = drug.dz_url
        self.name = drug.name
        self.manufacturer = drug.manufacturer
        self.composition = drug.composition
        self.popular_name = drug.popular_name
        self.prescription = drug.prescription
        self.expiration_date = drug.expiration_date
        self.release_type = drug.release_type

    def __repr__(self):
        return 'name:{},dz_url:{},manufacturer:{},composition:{},popular_name:{},expiration_date:{},prescription{},' \
               'release_type:{}'.format(
            self.name,
            self.dz_url,
            self.manufacturer,
            self.composition,
            self.popular_name,
            self.expiration_date,
            self.prescription,
            self.release_type)

    def toJSON(self):
        return {"name": self.name,
                "url": self.dz_url,
                "manufacturer": self.manufacturer,
                "composition": self.composition,
                "popular_name": self.popular_name,
                "expiration_date": self.expiration_date,
                "prescription": self.prescription,
                "type": self.release_type}
