from config import *

from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine


db_url=settings.DB_URL

Base=declarative_base()
engine=create_engine(db_url)

SessionFactory=sessionmaker(bind=engine,autoflush=False,autocommit=False)

def connect():
    db=SessionFactory()
    try:
        yield db 
    finally:
        db.close()

