from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

driver = "mysqlconnector"
username = "root"
password = "test123"
database = "ann"
server = "127.0.0.1:3308"
charset = "utf8"
engine = create_engine(f"mysql+{driver}://{username}:{password}@{server}/{database}?charset={charset}")
MapBase = declarative_base(bind=engine)
DBSession = sessionmaker(bind=engine)