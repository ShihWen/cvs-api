# import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy import select

from test.config import config
# check version: 1.4.39
# print(sqlalchemy.__version__)

params = config()
DB_FULL_URL = f"postgresql+psycopg2://{params['user']}:{params['password']}@{params['host']}/{params['database']}"


engine = create_engine(DB_FULL_URL, echo=True)
metadata_obj = MetaData()

fm_table = Table('cnvnt_str_fm', metadata_obj,
    Column('extract_date', DateTime),
    Column('store_name', String),
    Column('address', String)            
)

stmt = select(fm_table).where(fm_table.c.store_name == '全家新德光店')
print(stmt)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)
        break

