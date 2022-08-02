from flask_restful import Resource

from db import db
from db import fm_table


class FamilyMart(Resource):
    def get(self, name):
        results = db.session.query(fm_table).filter_by(store_name=name).\
            order_by(fm_table.c.extract_date.desc()).limit(3)
        
        output = {'store':[]}
        
        for row in results:
            extract_date = str(row[0])
            store_name = row[1]
            address = row[2]
            output['store'].append({'extract_date':extract_date,
                'store_name':store_name, 
                'address':address})
        return output
        