#!/usr/bin/python
# -*- coding: utf-8 -*-

## input parameters
username='reliable'
password='9ykhCFG1PB1dwvm5'

locals = [
    {
        'name': 'Centro Social e Paroquial de Cabril',
        'name_alt': 'Cabril',
        'latitude': 41.714849,
        'longitude': -8.034901,
    },
    {
        'name': 'Centro Social e Paroquial de Vilar de Perdizes',
        'name_alt': 'VilarPerdizes',
        'latitude': 41.855523,
        'longitude': -7.633986,
    }
]

parameters = {
    't2': {'name': 'temperature at 2m', 'key': 'temp', 'units': 'ºC', 'var': 't2'},
    'hr': {'name': 'relative humidity at 2m', 'key': 'hum', 'units': '%', 'var': 'hr'},
    'pp': {'name': '1-hour rainfall accumulation', 'key': 'rain', 'units': 'mm/h', 'var': 'pp'},
    'cl': {'name': 'cloud cover', 'key': 'cloud', 'units': '%', 'var': 'cl'},
    'ws': {'name': 'wind speed at 2m', 'key': 'wind_vel', 'units': 'm/s', 'var': 'ws'},
    'wd': {'name': 'wind direction at 2m', 'key': 'wind_dir', 'units': 'º', 'var': 'wd'},
}

n_days_forecast = 7
