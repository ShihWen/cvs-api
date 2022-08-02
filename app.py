from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy import select

from config import config
# from db import db
# from resources.family_mart import FamilyMart

params = config()
DB_FULL_URL = f"postgresql+psycopg2://{params['user']}:{params['password']}@{params['host']}/{params['database']}"


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_FULL_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'apple'
db = SQLAlchemy(app)

api = Api(app)

metadata_obj = MetaData()
fm_table = Table('cnvnt_str_fm', metadata_obj,
    Column('extract_date', String),
    Column('store_name', String),
    Column('address', String)                
)

class FamilyMart(Resource):
    def get(self, name):
        results = db.session.query(fm_table).filter_by(store_name=name).all()
        
        output = {'store':[]}
        
        for row in results:
            extract_date = str(row[0])
            store_name = row[1]
            address = row[2]
            output['store'].append({'extract_date':extract_date,
                'store_name':store_name, 
                'address':address})
        return output
        


api.add_resource(FamilyMart, '/familymart/<string:name>')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
