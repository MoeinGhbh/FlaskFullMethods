from flask import Flask

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////c//Users//Rose//Desktop//Flask Python//Restful API Python
# Flask//database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///c:\\Users\\Rose\\Desktop\\Flask Python\\Restful API Python " \
                                        "Flask\\database.db "

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

