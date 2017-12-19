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

def create_org_from_person(person_id, data):
    
    person_lead_source = data[person_fields['Lead Source']]

    if person_lead_source not in (None,):
        person_lead_source = person_lead_source_map[int(person_lead_source)]
        person_lead_source = list(org_lead_source_map.keys())[list(org_lead_source_map.values()).index(person_lead_source)]

    person_campaign = data[person_fields['Campaign']]
    
    if person_campaign not in (None,):
        person_campaign = person_campaign_map[int(person_campaign)]
        person_campaign = list(org_campaign_map.keys())[list(org_campaign_map.values()).index(person_campaign)]

    org_name = data['name'] + ' - COMPANY'
    owner_id = data['owner_id']['id']

    org_lead_source = organization_fields['Lead Source'][0]
    org_type = organization_fields['Type'][0]
    org_campaign = organization_fields['Campaign'][0]
        
    data_dict = {'name': org_name,
                 'owner_id': owner_id,
                 org_lead_source: person_lead_source,
                 org_type: 313,
                 org_campaign: person_campaign
                 }
    
    json_data = json.dumps(data_dict, ensure_ascii=False)

    org_id = create_organization(json_data)
    print(org_id)

    data2 = {'org_id': org_id}
    
    json_data2 = json.dumps(data2, ensure_ascii=False)

    update_person_field(person_id, json_data2)


def build_org_update_data(org_id, value):
    data_dict = {}
    
    companyid = organization_fields['Company ID'][0]
    pd_cid = get_org_field(org_id, companyid)
    if not pd_cid:
        data_dict[companyid] = value[0][2]

    backend = organization_fields['Back-end'][0]
    pd_backend = get_org_field(org_id, backend)
    if not pd_backend:
        data_dict[backend] = value[0][4]
        
    lead_source = organization_fields['Lead Source'][0]
    if not get_org_field(org_id, lead_source):
        data_dict[lead_source] = value[0][1]

    org_type = organization_fields['Type'][0]
    if not get_org_field(org_id, org_type):
        data_dict[org_type] = value[0][5]

    activated_on = organization_fields['Activated On'][0]
    if not get_org_field(org_id, activated_on) and pd_cid == value[0][2]:
        if value[0][3] is not None:
            data_dict[activated_on] = datetime.strftime(value[0][3], '%Y-%m-%d')

    print(data_dict)

    if data_dict:
        json_data = json.dumps(data_dict, ensure_ascii=False)
        update_organization_field(org_id, json_data)
    else:
        print('No data for org_id {}'.format(org_id))



def update_person_field(person_id, json_data):
    query = 'https://api.pipedrive.com/v1/persons/'
    query += str(person_id)
    query += '?api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'PUT', json_data,
                                  headers={'content-type': 'application/json'})

    raw_json = json.loads(content.decode('utf-8'))

    if raw_json['success']:
        message = 'Person {} updated.'.format(person_id)
        print(message)
        record = [raw_json['data']['id'], message, json_data]
        write_to_log(record)
    else:
        print(raw_json)


def update_note(note_id, json_data):
    query = 'https://api.pipedrive.com/v1/notes/'
    query += str(note_id)
    query += '?api_token=' + API_KEY

    h = httplib2.Http('.cache')
    response, content = h.request(query, 'PUT', json_data,
                                  headers={'content-type': 'application/json'})

    raw_json = json.loads(content.decode('utf-8'))

    if raw_json['success']:
        message = 'Note {} updated.'.format(note_id)
        print(message)
        record = [raw_json['data']['id'], message, json_data]
        write_to_log(record)
    else:
        print(raw_json)
  
        
def update_bad_emails(person_id, pd_value):
    data_dict = {}

    email = pd_value['email'][0]['value'].lower()
    if email in bad_emails_dict.keys():

        auto_email_field = person_fields['Automated Email Status']
        if not get_person_field(person_id, auto_email_field):
            data_dict[auto_email_field] = bad_emails_dict[email]
                
            if data_dict:
                json_data = json.dumps(data_dict, ensure_ascii=False)
                   
                update_person_field(person_id, json_data)
            else:
                print('No data for person_id {}'.format(person_id))
    else:
        print('{}. No values to update.'.format(person_id))


##################
# Function Calls #
##################

def main():
    start_time = time.time()

    
    end_time = time.time()
    print('\nElapsed time: {:.2f} seconds\n'.format(end_time - start_time))


if __name__ == '__main__':
    main()
