from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///parcel.db', echo=True)
Base = declarative_base()


class Data(Base):

    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    title = Column(String)  
    url = Column(String)  
    preview_url = Column(String,default=None)  
    download_url = Column(String,default=None)  
    password = Column(String,default=None)  



Base.metadata.create_all(engine)