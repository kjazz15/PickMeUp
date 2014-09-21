import nltk
import apis
from machine import *

class SadnessFactory():

	def __init__(self):
		self.master_dict = {}
		self.classifier = open_classifier()

	def process_text(self, number, text, zipcode):
		reg_prob = self.classifier.predict([text])
		if reg_prob == ['sad']:
			probs = self.classifier.predict_proba([text])
			sad = probs[0][1]
			if number in self.master_dict.keys():
				self.master_dict[number] += sad
			else:
				self.master_dict[number] = sad
			if self.master_dict[number] >= 3.0:
				return self.get_uri(number, zipcode)
		return None

	def get_uri(self, number, zipcode):
		if int(number) / 2 == 1:
			place = apis.get_venue(zipcode)
		else:
			place = apis.get_bars(zipcode)
			latitude = place['geometry']['location']['lat']
			longitude = place['geometry']['location']['lon']
			name = place['name']
		print place
		uber_uri = 'uber://?action=setPickup&pickup=my_location&dropoff[latitude]='+latitude+'&dropoff[longitude]='+longitude+'dropoff[nickname]=Coit%20Tower&dropoff[formatted_address]=1%20Telegraph%20Hill%20Blvd%2C%20San%20Francisco%2C%20CA%2094133'
		return uber_uri

if __name__ == "__main__":
	sf = SadnessFactory()
	sf.get_uri('8472718339', '61820')
