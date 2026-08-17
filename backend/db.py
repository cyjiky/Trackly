from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 

load_dotenv()

URL_DB = os.getenv('SQL_DB_URL')

engine = create_engine(URL_DB, connect_args={'check_same_thread': False})

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()