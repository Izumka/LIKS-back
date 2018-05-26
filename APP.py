from flask import Flask

class APP:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://Izumka:1234@localhost/liks_db"

