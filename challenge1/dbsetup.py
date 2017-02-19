# =============================================================
# Created Date : 19/1/2017
# Name : dbsetup.py
# Contributers : Ajay
# =============================================================
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

''' session table '''
class session(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    token = Column(String(250), nullable=False)


engine = create_engine('sqlite:///session.db')
Base.metadata.create_all(engine)
    


