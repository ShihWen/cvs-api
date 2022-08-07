from flask import Flask
from flask_restful import Api
import os


# from config import config
from db import db
from resources.family_mart import FamilyMartByName
from resources.family_mart import FamilyMartByCity
from resources.family_mart import FamilyMartStoreNumByCity
from resources.family_mart import FamilyMartStoreNumByGivenCity

#params = config()
#DB_FULL_URL = f"postgresql+psycopg2://{params['user']}:{params['password']}@{params['host']}/{params['database']}"


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_CUSTOM_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'apple'

api = Api(app)


api.add_resource(FamilyMartByName, '/fm_byname/<string:name>')
api.add_resource(FamilyMartByCity, '/fm_bycity/<string:city>')
api.add_resource(FamilyMartStoreNumByCity, '/fm_stores')
api.add_resource(FamilyMartStoreNumByGivenCity,'/fm_stores/<string:city>')



if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
