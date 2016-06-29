#!/usr/bin/python3
import sys
import requests
import datetime

if len(sys.argv) != 3:
    print("Usage: {} <from station> <to station>".format(sys.argv[0]))
    sys.exit()
today = datetime.datetime.today().strftime('%m%d%Y')

f_station = sys.argv[1]
t_station = sys.argv[2]
url = 'https://secure.gotransit.com/service/EligibilityService.svc/GetTrips?dateString={}&fromStation={}&tostation={}'.format(today, f_station, t_station)

for x in requests.get(url).json()['GetTripsResult']['Trips']:
    print("{} - {}".format(x['DepartTime'], x['TripNumber']))
