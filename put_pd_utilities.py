#! /usr/bin/env python3

import time
import httplib2
import json
import pprint
from datetime import datetime

from log_changes import write_to_log

"""
Pipedrive API documentation: https://developers.pipedrive.com/v1
"""
        
def create_organization(json_data):
    query = 'https://api.pipedrive.com/v1/organizations/'
    query += '?api_token=' + API_KEY
    
    h = httplib2.Http('.cache')
    response, content = h.request(query,
                                  method='POST',
                                  body=json_data,
                                  headers={'content-type': 'application/json'})

    raw_json = json.loads(content.decode('utf-8'))

    if raw_json['success']:
        message = 'Organization {} created in Pipedrive with org_id is {}'.format(raw_json['data']['name'], raw_json['data']['id'])

        record = [raw_json['data']['id'], message, json_data]

        write_to_log(record)
        
        return raw_json['data']['id']
    else:
        pprint.pprint(raw_json)
        return 0


def update_organization_field(org_id, json_data):
    query = 'https://api.pipedrive.com/v1/organizations/'
    query += str(org_id)
    query += '?api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'PUT', json_data,
                                  headers={'content-type': 'application/json'})

    raw_json = json.loads(content.decode('utf-8'))

    if raw_json['success']:
        message = 'Organization {} updated.'.format(org_id)
        print(message)
        record = [org_id, message, json_data]
        write_to_log(record)
    else:
        print(raw_json)


def create_new_person(json_data):
    query = 'https://api.pipedrive.com/v1/persons/'
    query += '?api_token=' + API_KEY
    
    h = httplib2.Http('.cache')
    response, content = h.request(query,
                                  method='POST',
                                  body=json_data,
                                  headers={'content-type': 'application/json'})

    raw_json = json.loads(content.decode('utf-8'))

    if raw_json['success']:
        person_id = raw_json['data']['id']
        message = 'Person {} created in Pipedrive with org_id is {}'.format(raw_json['data']['name'], person_id)

        record = [person_id, message, json_data]

        write_to_log(record)
        
        return person_id
    else:
        pprint.pprint(raw_json)
        return 0



def create_activity(json_data):
    query = 'https://api.pipedrive.com/v1/activities'
    query += '?api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'POST', json_data,
                                  headers={'content-type': 'application/json'})

    raw_json = json.loads(content.decode('utf-8'))

    if raw_json['success']:
        message = 'Activity created for org_id {}.'.format(raw_json['data']['org_id'])
        print(message)
        record = [raw_json['data']['id'], message, json_data]
        write_to_log(record)
    else:
        print(raw_json)


def create_note(json_data):
    query = 'https://api.pipedrive.com/v1/notes'
    query += '?api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'POST', json_data,
                                  headers={'content-type': 'application/json'})

    raw_json = json.loads(content.decode('utf-8'))

    if raw_json['success']:
        message = 'Note created for org_id {}.'.format(raw_json['data']['org_id'])
        print(message)
        record = [raw_json['data']['id'], message, json_data]
        write_to_log(record)
    else:
        print(raw_json)


##################
# Function Calls #
##################

def main():
    start_time = time.time()

   
    end_time = time.time()
    print('\nElapsed time: {:.2f} seconds\n'.format(end_time - start_time))


if __name__ == '__main__':
    main()
