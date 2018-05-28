from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Izumka:1234@localhost/liks_db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'medication'
    med_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    med_url = db.Column(db.String, unique=True, nullable=False)
    med_name = db.Column(db.String, nullable=False)
    med_man_country = db.Column(db.String)
    med_composition = db.Column(db.String, nullable=False)
    med_release_type = db.Column(db.String, nullable=False)

    def __init__(self, med_url, med_name, med_man_country, med_composition,
                 med_release_type):
        self.med_url = med_url
        self.med_name = med_name
        self.med_man_country = med_man_country
        self.med_composition = med_composition
        self.med_release_type = med_release_type

    def __repr__(self):
        return '{},{},{},{},{},{}'.format(
            self.med_id,
            self.med_url,
            self.med_name,
            self.med_man_country,
            self.med_composition,
            self.med_release_type)


db.create_all()
print(User.query.all())

# if __name__ == '__main__':
#     test = 'med_id:{},med_ur:{},med_name:{},med_man_country:{},med_composition:{},med_release_type:{}'
#     test.split(',')
#     # print(test.split(',').split(':'))