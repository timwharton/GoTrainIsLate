#!/usr/bin/python3
import sys
import requests
import datetime

today = datetime.datetime.today().strftime('%m%d%Y')
url = 'https://secure.gotransit.com/service/EligibilityService.svc/GetArrivalStations?dateString={}&departStationCode=UN'.format(today)

for x in requests.get(url).json()['GetArrivalStationsResult']['Stations']:
    print("{} - {}".format(x['Code'], x['Name']))

f_station = 'UN'
t_station = 'PO'
url = 'https://secure.gotransit.com/service/EligibilityService.svc/GetTrips?dateString={}&fromStation={}&tostation={}'.format(today, f_station, t_station)

for x in requests.get(url).json()['GetTripsResult']['Trips']:
    print("{} - {}".format(x['DepartTime'], x['TripNumber']))
