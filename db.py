from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime, Numeric

db = SQLAlchemy()

metadata_obj = MetaData()

fm_table = Table('cnvnt_str_fm', metadata_obj,
    Column('extract_date', String),
    Column('store_name', String),
    Column('city', String),
    Column('district', String),
    Column('address', String),
    Column('longitude', Numeric),
    Column('latitude', Numeric),
    Column('services', String)                
)