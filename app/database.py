# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DatabaseAccess:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseAccess, cls).__new__(cls)
            cls._instance.init_engine()
        return cls._instance

    def init_engine(self):
        self.engine = create_engine("mysql+pymysql://root:@localhost/smart_parking")
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()
