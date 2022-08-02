from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime

db = SQLAlchemy()

metadata_obj = MetaData()

fm_table = Table('cnvnt_str_fm', metadata_obj,
    Column('extract_date', String),
    Column('store_name', String),
    Column('address', String)                
)