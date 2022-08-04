import simplejson as json
from flask_restful import Resource
from sqlalchemy import func


from db import db
from db import fm_table


class Tools:
    @classmethod
    def get_latest_dt(cls): 
        latest_dt = db.session.query(fm_table.c.extract_date).\
        group_by(fm_table.c.extract_date).\
        order_by(fm_table.c.extract_date.desc()).limit(1).cte('latest_dt')

        latest_var = db.session.query(fm_table.c.extract_date).\
        group_by(fm_table.c.extract_date).\
        order_by(fm_table.c.extract_date.desc()).limit(1)

        return latest_dt, str(latest_var[0][0])


class FamilyMartByName(Resource):
    def get(self, name):

        fields = (fm_table.c.store_name, 
                  fm_table.c.address, 
                  fm_table.c.longitude, 
                  fm_table.c.latitude)

        latest_cte, latest_var = Tools.get_latest_dt()
        
        results = db.session.query(fm_table).\
            with_entities(*fields).\
            filter(fm_table.c.store_name.like(f'%{name}%'), 
                   fm_table.c.extract_date==latest_cte.c.extract_date)
        
        output = {'extract_date':latest_var, 'store':[]}
        
        for row in results:
            
            store_name = row[0]
            address = row[1]
            lng = json.dumps(row[2], use_decimal=True)
            lat = json.dumps(row[3], use_decimal=True)
            output['store'].append({'store_name':store_name, 
                'address':address,
                'longitude':lng,
                'latitude': lat})
            
        return output


class FamilyMartByCity(Resource):
    def get(self, city):

        fields = (fm_table.c.store_name, 
                  fm_table.c.address, 
                  fm_table.c.longitude, 
                  fm_table.c.latitude)

        latest_cte, latest_var = Tools.get_latest_dt()
        
        refined_city = city.replace('臺', '台')
        results = db.session.query(fm_table).\
            with_entities(*fields).\
            filter(fm_table.c.address.like(f'{refined_city}%'), 
                   fm_table.c.extract_date==latest_cte.c.extract_date)
        
        output = {'extract_date':latest_var, 'store':[]}
        
        for row in results:
            store_name = row[0]
            address = row[1]
            lng = json.dumps(row[2], use_decimal=True)
            lat = json.dumps(row[3], use_decimal=True)
            output['store'].append({'store_name':store_name, 
                'address':address,
                'longitude':lng,
                'latitude': lat})
            
        return output


class FamilyMartStoreNumByCity(Resource):
    def get(self):

        latest_cte, latest_var = Tools.get_latest_dt()
        
        results = db.session.query(fm_table.c.city, func.count(fm_table.c.store_name)).\
            filter(fm_table.c.extract_date==latest_cte.c.extract_date).\
            group_by(fm_table.c.city).\
            order_by(func.count(fm_table.c.store_name).desc())
        
        output = {'extract_date':latest_var, 'store_counts':{}}

        for city_name, store_count in results:
            output['store_counts'][city_name] = store_count
                
        return output


class FamilyMartStoreNumByGivenCity(Resource):
    def get(self, city):

        latest_cte, latest_var = Tools.get_latest_dt()
        
        refined_city = city.replace('臺', '台')
        results = db.session.query(fm_table.c.city,fm_table.c.district, func.count(fm_table.c.store_name)).\
            filter(fm_table.c.address.like(f'{refined_city}%'),
                   fm_table.c.extract_date==latest_cte.c.extract_date).\
            group_by(fm_table.c.city, fm_table.c.district).\
            order_by(func.count(fm_table.c.store_name).desc())
        
        output = {'extract_date':latest_var, 'store_counts':{}}
        for city_name, district_name, store_count in results:
            city_district = city_name + district_name
            output['store_counts'][city_district] = store_count
                
        return output
        