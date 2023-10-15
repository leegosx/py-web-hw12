import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def connect_url():
    file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
    config = configparser.ConfigParser()
    config.read(file_config)

    db_user = config.get('DB', 'user')
    db_pass = config.get('DB', 'password')
    db_host = config.get('DB', 'host')
    db_name = config.get('DB', 'dbname')
        
    db_url = f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'
    return db_url
    
SQLALCHEMY_DATABASE_URL = connect_url()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Dependecy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()