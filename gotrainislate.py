#!/usr/bin/python3
import sys
import requests
import datetime

if len(sys.argv) != 3:
    print("Usage: {} <station code> <trip num>".format(sys.argv[0]))
    sys.exit()

REQ_DATE_FMT = '%m%d%Y'
LOG_DATE_FMT = '%Y-%m-%d'
CHECK_URL = 'https://secure.gotransit.com/service/EligibilityService.svc/CheckEligible'

station = sys.argv[1]
trip = sys.argv[2]

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, 7)]

for day in date_list:
    post_json = {"dateString": day.strftime(REQ_DATE_FMT),"arrivalstationCode": station,"tripNumber": trip,"lang":"en"}
    res = requests.post(CHECK_URL, json=post_json).json()['CheckEligibleResult']
    if res['ResultType'] == 1:
        print('{}: ಠ_ಠ You are owed money!'.format(day.strftime(LOG_DATE_FMT)))
    else:
        print('{}: ¯\_(ツ)_/¯ {}'.format(day.strftime(LOG_DATE_FMT), res['Reason']))
