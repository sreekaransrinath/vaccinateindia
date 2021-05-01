from json.decoder import JSONDecodeError
import requests
from playsound import playsound
from datetime import datetime as dt
import time 

while 1:
	print(dt.now())
	response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=571&date=01-05-2021").json()
	print(response)
	try:
		for center in response['centers']:
			centerDeets = {
				"Name": center["name"], 
				"Pincode": center["pincode"]
			}
			sessionList = center["sessions"]
			for session in sessionList:
				sessionDeets = {
					"Date": session["date"], 
					"Capacity": session["available_capacity"]
				}
				if session["min_age_limit"] == 18 and session["available_capacity"] > 0 and ('UPHC' in center["name"] or 'VIJAYA' in center["name"] or 'UCHC' in center["name"] or 'APOLLO' in center["name"]):
					print(centerDeets, sessionDeets)
					playsound("./suffer.mp3")
	except Exception as e:
		print(e)
	time.sleep(1)