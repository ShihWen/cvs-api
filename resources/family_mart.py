import simplejson as json
from flask_restful import Resource


from db import db
from db import fm_table


class FamilyMart(Resource):
    def get(self, name):

        fields = (fm_table.c.extract_date, 
                  fm_table.c.store_name, 
                  fm_table.c.address, 
                  fm_table.c.longitude, 
                  fm_table.c.latitude,
                  fm_table.c.services)

        results = db.session.query(fm_table).\
            with_entities(*fields).\
            filter(fm_table.c.store_name==name).\
            order_by(fm_table.c.extract_date.desc()).limit(1)
        
        output = {'store':[]}
        
        for row in results:
            extract_date = str(row[0])
            store_name = row[1]
            address = row[2]
            lng = json.dumps(row[3], use_decimal=True)
            lat = json.dumps(row[4], use_decimal=True)
            services = row[5].split(",")
            output['store'].append({'extract_date':extract_date,
                'store_name':store_name, 
                'address':address,
                'longitude':lng,
                'latitude': lat,
                'services':services})
        return output
        