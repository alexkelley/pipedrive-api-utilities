#! /usr/bin/env python3

import time
import httplib2
import json
import pprint
from datetime import datetime

"""
Pipedrive API documentation: https://developers.pipedrive.com/v1
"""

def get_open_deals(filter_id, start, limit):
    query = 'https://api.pipedrive.com/v1/deals'
    query += '?filter_id=' + str(filter_id)
    query += '&status=all_not_deleted'
    query += '&start=' + str(start)
    query += '&limit=' + str(limit)
    query += '&api_token=' + API_KEY

    h = httplib2.Http('.cache')
    print(query)
    response, content = h.request(query, 'GET')

    raw_json = json.loads(content.decode('utf-8'))

    return raw_json


def combine_open_deals(filter_id):
    start = 0
    limit = 100

    raw_json = get_open_deals(filter_id, start, limit)

    data = (raw_json['data'])

    while raw_json['additional_data']['pagination']['more_items_in_collection']:
        start = raw_json['additional_data']['pagination']['next_start']
        raw_json = get_open_deals(filter_id, start, limit)
        data += raw_json['data']

    print('{} deals returned'.format(len(data)))

    return data


def get_people(start, limit):
    query = 'https://api.pipedrive.com/v1/persons:(id,org_id,name,owner_id,dc35866d2b1f336bf4ffc71bca166af53c726969,1ba5d701b1cbf5ad37f2ef28a6682d46dfcae7b1,email,f907c294edd1f4703ddc5bbddb045d580f42a4a6)'
    query += '?start=' + str(start)
    query += '&limit=' + str(limit)
    query += '&api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'GET')

    raw_json = json.loads(content.decode('utf-8'))

    return raw_json


def combine_people():
    start = 0
    limit = 100

    raw_json = get_people(start, limit)

    data = (raw_json['data'])

    while raw_json['additional_data']['pagination']['more_items_in_collection']:
        start = raw_json['additional_data']['pagination']['next_start']
        raw_json = get_people(start, limit)
        data += raw_json['data']

    print('{} people returned'.format(len(data)))

    return data


def get_notes(start, limit):
    query = 'https://api.pipedrive.com/v1/notes'
    query += '?start=' + str(start)
    query += '&limit=' + str(limit)
    query += '&api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'GET')

    raw_json = json.loads(content.decode('utf-8'))

    return raw_json


def combine_notes():
    start = 0
    limit = 100

    raw_json = get_notes(start, limit)

    data = (raw_json['data'])

    while raw_json['additional_data']['pagination']['more_items_in_collection']:
        start = raw_json['additional_data']['pagination']['next_start']
        raw_json = get_notes(start, limit)
        data += raw_json['data']

    print('{} notes returned'.format(len(data)))

    return data


def get_people_with_filter(filter_id, start, limit):
    query = 'https://api.pipedrive.com/v1/persons:(id,org_id,name,owner_id,dc35866d2b1f336bf4ffc71bca166af53c726969,1ba5d701b1cbf5ad37f2ef28a6682d46dfcae7b1,email,f907c294edd1f4703ddc5bbddb045d580f42a4a6)'
    query += '?filter_id=' + str(filter_id)
    query += '&start=' + str(start)
    query += '&limit=' + str(limit)
    query += '&api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'GET')

    raw_json = json.loads(content.decode('utf-8'))

    return raw_json


def combine_people_with_filter(filter_id):
    start = 0
    limit = 100

    raw_json = get_people_with_filter(filter_id, start, limit)

    data = (raw_json['data'])

    while raw_json['additional_data']['pagination']['more_items_in_collection']:
        start = raw_json['additional_data']['pagination']['next_start']
        raw_json = get_people_with_filter(filter_id, start, limit)
        data += raw_json['data']

    print('{} people returned'.format(len(data)))

    return data


def get_field_data(object_type, field_id):
    query = 'https://api.pipedrive.com/v1/'
    query += str(object_type)
    if field_id is not None:
        query += '/'
        query += str(field_id)
    query += '?api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'GET')

    raw_json = json.loads(content.decode('utf-8'))

    return raw_json


def get_organizations(start, limit):
    query = 'https://api.pipedrive.com/v1/organizations'
    query += '?start=' + str(start)
    query += '&limit=' + str(limit)
    query += '&api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'GET')

    raw_json = json.loads(content.decode('utf-8'))

    return raw_json


def combine_organizations():
    start = 0
    limit = 100

    raw_json = get_organizations(start, limit)

    data = (raw_json['data'])

    while raw_json['additional_data']['pagination']['more_items_in_collection']:
        start = raw_json['additional_data']['pagination']['next_start']
        raw_json = get_organizations(start, limit)
        data += raw_json['data']

    print('{} organizations returned'.format(len(data)))

    return data


def get_activities(start, limit):
    query = 'https://api.pipedrive.com/v1/activities'
    query += '?user_id=0'
    query += '&start=' + str(start)
    query += '&limit=' + str(limit)
    query += '&api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'GET')

    raw_json = json.loads(content.decode('utf-8'))

    return raw_json


def combine_activities():
    start = 0
    limit = 100

    raw_json = get_activities(start, limit)

    data = (raw_json['data'])

    while raw_json['additional_data']['pagination']['more_items_in_collection']:
        start = raw_json['additional_data']['pagination']['next_start']
        raw_json = get_activities(start, limit)
        data += raw_json['data']

    print('{} activities returned'.format(len(data)))

    return data


def get_org_field(org_id, field_id):
    query = 'https://api.pipedrive.com/v1/organizations'
    query += '/' + str(org_id)
    query += '?api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'GET')
    raw_json = json.loads(content.decode('utf-8'))
    field_value = raw_json['data'][field_id]

    return field_value


################
# Setup values #
################
global API_KEY

with open('api.secrets', 'r') as f:
    API_KEY = f.read().strip() 

##################
# Function Calls #
##################

if __name__ == '__main__':
    start_time = time.time()
    deals = combine_open_deals(241)

    pprint.pprint(deals)
    
    end_time = time.time()
    print('\nElapsed time: {:.2} seconds\n'.format(end_time - start_time))


