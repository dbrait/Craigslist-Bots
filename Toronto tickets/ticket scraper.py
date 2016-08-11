from craigslist import CraigslistEvents
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse 
from util import post_listing_to_slack, find_points_of_interest
from slackclient import SlackClient 
import time 
import settings 

engine = create_engine("sqlite:///listings.db", echo=False)

Base = declarative_base()

class Listing(Base):
	"""
	table store data on craigslist listings
	"""

	__tablename__ = "listings"

	id = Column(Integer, primary_key = True)
	link = Column(String, unique=True)
	created = Column(DateTime)
	geotag = Column(String)
	lat = Column(Float)
	lon = Column(Float)
	name = Column(String)
	price = Column(Float)
	location = Column(String)
	cl_id = Column(Integer, unique=True)
	area = Column(String)
	bart_stop = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


