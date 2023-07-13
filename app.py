from flask import Flask
import logging as logger
from flask_sqlalchemy import SQLAlchemy




logger.basicConfig(level="DEBUG")
app = Flask(__name__)
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3306/E-commerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


if __name__ == '__main__':
    from api import *
    app.run(debug=True,port=5000)