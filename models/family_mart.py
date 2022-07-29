from db import db


class FamilyMartModel(db.Model):    
    __tablename__ = 'snvnt_str_fm'

    extract_date = db.Column(db.DateTime)
    store_name = db.Column(db.String(80))
    store_type = db.Column(db.String(80))
    store_city = db.Column(db.String(80))
    store_district = db.Column(db.String(80))
    store_addr = db.Column(db.String(100))
    store_long = db.Column(db.Float(precision=8))
    store_lat = db.Column(db.Float(precision=8))
    store_service = db.Column(db.String(100))
    insert_datetime = db.Column(db.DateTime)

    inputs = (extract_date
              , store_name
              , store_type
              , store_city
              , store_district
              , store_addr
              , store_long
              , store_lat
              , store_service
              , insert_datetime )


    def __init__(self, extract_date, store_name
                     , store_type, store_city
                     , store_district, store_addr
                     , store_long, store_lat
                     , store_service, insert_datetime):
        self.extract_date = extract_date
        self.store_name = store_name
        self.store_type = store_type
        self.store_city = store_city
        self.store_district = store_district
        self.store_addr = store_addr
        self.store_long = store_long
        self.store_lat = store_lat
        self.store_service = store_service
        self.insert_datetime = insert_datetime

    def json(self):
        return {'extract_date':self.extract_date,
                'store_name':self.store_name,
                'store_type':self.store_type,
                'store_city':self.store_city,
                'store_district':self.store_district,
                'store_addr':self.store_addr,
                'store_long':self.store_long,
                'store_lat':self.store_lat,
                'store_service':self.store_service,
                'insert_datetime':self.insert_datetime}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()