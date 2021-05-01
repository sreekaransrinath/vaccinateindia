import requests
import re
import json
from playsound import playsound

# while 1:
response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=571&date=01-05-2021")
response = json.loads(response.text)
num_centers = len(response['centers'])
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
		if session["min_age_limit"] == 18 and session["available_capacity"] > 0:
			print(centerDeets, sessionDeets)