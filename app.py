from flask import Flask
from flask_restful import Api

from config import config
from db import db
from resources.family_mart import FamilyMart

params = config()
DB_FULL_URL = f"postgresql+psycopg2://{params['user']}:{params['password']}@{params['host']}/{params['database']}"


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_FULL_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'apple'

api = Api(app)


api.add_resource(FamilyMart, '/familymart/<string:name>')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
