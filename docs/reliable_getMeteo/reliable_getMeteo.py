#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################
## must run with python 3
## author: Jorge Palma
##   date: 2019-05-23
##########################


import sys
import os

## verify python version
if (sys.version_info < (3, 0)):
    print('You must run with python 3')
    sys.exit(1)

import argparse
import json
import datetime
import urllib.request
import base64


## import config variables in config.py
import reliable_getMeteo_config as config


def get_parser():

    """ Get parser object """
    parser=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description='get forecast data fromo meteo|Técnico')

    parser.add_argument('-nv', '--noverbose',
                        help="no verbose",
                        action="store_true")

    parser.add_argument('-vv', '--vverbose',
                        help="more verbose",
                        action="store_true")

    parser.add_argument('-o', '--output',
                        help="output to screen",
                        action="store_true")


     ## Assign args to variables
    args = parser.parse_args()
    args.verbose = True

    if args.noverbose:
        args.verbose = False

    if args.vverbose:
        args.verbose = True
        args.noverbose = False

    return args

def download_data(lat, lon, date, param):
    url = 'http://meteo.tecnico.ulisboa.pt/service/reliable/PrevByDateAndMetric'
    url = url + '?lat='+str(lat)+'&lon='+str(lon)+'&date='+date+'&metric='+param

    req = urllib.request.Request(url)

    credentials = ('%s:%s' % (config.username, config.password))
    encoded_credentials = base64.b64encode(credentials.encode('ascii'))
    req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))

    try:
        with urllib.request.urlopen(req) as response:
            json_download = response.read()
    except urllib.error.HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        sys.exit(1)
    except urllib.error.URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        sys.exit(1)
    else:
        try:
            d = json.loads(json_download)
            return d
        except ValueError as e:
            print( '  ' + date +': No data available. skip')
            return False

## get arguments
args=get_parser()

## init output variable
data = {}

## iterate locals
for l in config.locals:
    start_date = datetime.datetime.today()
    current_date = start_date

    latitude = l['latitude']
    longitude = l['longitude']
    local = l['name_alt']

    data[local] = {}

    if args.verbose: print('get meteo forecast to ' + local + ' ...')

    ## iterate days
    for day in range(0,config.n_days_forecast):

        timedelta = datetime.timedelta(days=day)
        current_date = start_date + timedelta
        current_date_str = current_date.strftime("%Y%m%d")

        if args.vverbose: print(' ' + start_date.strftime("%Y%m%d") + ' +' + str(day) + ' day: ' + current_date_str)

        ##iterate parameters
        for key, param in config.parameters.items():

            ## download data
            d = download_data(latitude, longitude, current_date_str, param['key'])

            if not d:
                break

            ## join all by hours
            serie = d[0]['response']['points']

            h = 0
            for val in serie:
                current_date_int = int(current_date_str)
                hh = str(h).zfill(2)
                current_datetime = str(current_date_int) + ' ' + hh + ':00:00'

                if not current_datetime in data[local]:
                    data[local][current_datetime] = {}

                data[local][current_datetime][param['var']] = val

                h += 1
## output
data_json = json.dumps(data)

if args.output:
    print(data_json)
else:
    filename = 'meteo_' + start_date.strftime("%Y%m%d") + '.json'
    with open(filename, 'w') as outfile:
        outfile.write(data_json)
