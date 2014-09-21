import requests
from datetime import datetime
import config
import random
import json
import pyzipcode
from pyzipcode import ZipCodeDatabase

jambase_api = config.jambase
google_api = config.google

def get_venue(zipcode, radius=25, api_key=jambase_api):
	r = requests.get('http://api.jambase.com/events', params={'zipCode':zipcode, 'radius':radius, 'api_key':api_key})
	js = json.loads(r._content)
	events = js['Events']
	current_time = datetime.today()
	viable_events = []
	for item in events:
		date = datetime.strptime(item['Date'], '%Y-%m-%dT%H:%M:%S')
		if (date - current_time).total_seconds() < 186300.0 and (date - current_time).total_seconds() >= 0.0:
			viable_events.append(item)
	return random.choice(viable_events)

def get_latlng(zipcode):
	db = ZipCodeDatabase()
	zc = db[zipcode]
	longitude = zc.longitude
	latitude = zc.latitude
	return latitude, longitude

def get_bars(zipcode, radius=1000, api_key=google_api):
	latitude, longitude = get_latlng(zipcode)
	r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json', params = {'location':str(latitude)+','+str(longitude),'radius':radius,'types':'bar','key':api_key})
	viable_bars = []
	js = json.loads(r._content)
	bar = random.choice(js['results'])
	return bar

if __name__ == "__main__":
	r = get_bars(30332)
	print r['name']




