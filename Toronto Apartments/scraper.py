from craigslist import CraigslistHousing
from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse 
from util import post_listing_to_slack, find_points_of_interest
from stackclient import stackClient 
import time 
import settings 

engine = create_engine("sqlite:///listings.db", echo=False)

Base = declarative_base()

class Listing(Base):
	"""
	A table to store data on craigslist listings
	"""

	__tablename__ = "listings"

	id = Column(Integer, primary_key=True)
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
	ttc_stop = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def scrape_area(area):
	"""
	Scrapes craigslist for certain geographic area, and finds latest listings
	:param area:
	:return: A list of results.
	"""
	cl_h = CraigslistHousing(site=settings.CRAIGSLIST_SITE, area=area, category=settings.CRAIGSLIST_HOUSING_SECTION,
							filters={"max_price": settings.MAX_PRICE, "min_price": settings.MIN_PRICE})

	results = []
	gen = cl_h.get_results(sort_by="newest", geotagged=True, limit=20)
	while True:
		try:
			result = next(gen)
		except = StopIteration:
			break
		except Exception:
			continue 
		listing = session.query(Listing).filter_by(cl_id=result["id"]).first()

		#dont store listing if it already exists
		if listing is None:
			if result["where"] is None:
				#if there is no string identifying which neighborhood result is from skip it
				continue

			lat = 0
			lon = 0
			if result["geotag"] is not None:
				#assign coordinates
				lat = result["geotag"][0]
				lon = result["geotag"][1]

				#annotate result with info about area its in and points of interest near it
				geo_data = find_points_of_interest(result["geotag"], result["where"])
				result.update(geo_data)
			else:
				result["area"] = ""
				result["bart"] = ""

			#try parsing price
			price = 0
			try:
				price = float(result["price"].replace("$",""))
			except Exception:
				pass


			#create listing object
			listing = Listing(
				link=result["url"],
				created=parse(result["datetime"]),
				lat=lat,
				lon=lon,
				name=result["name"],
				price=price,
				location=result["where"],
				cl_id=result["id"],
				area=result["area"],
				ttc_stop=result["ttc"]
			)

			#save listing so we dont grab it again
			session.add(listing)
			session.commit()

			#return result if its near ttc station or if in area defined
			if len(result["ttc"]) > 0 or len(result["area"]) > 0
				results.append(result)

		return results

	def do_scrape():
		"""
		runs craigslist scraper, and posts data to slack 
		"""

		#create slack client 
		sc = SlackClient(settings.SLACK_TOKEN)

		#get results from craigslist
		all_results = []
		for area in settings.AREAS:
			all_results += scrape_area(area)

		print("{}: Got {} results.".format(time.ctime(), len(all_results)))

		#post each result to slack 
		for result in all_results:
			post_listing_to_slack(sc, result)