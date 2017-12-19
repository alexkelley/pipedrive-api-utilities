#! /usr/bin/env python3

from datetime import datetime

"""
Pipedrive API documentation: https://developers.pipedrive.com/v1
"""

def write_to_log(log_file):
    timestamp = datetime.strftime(datetime.now(), '%Y-%m-%dT%H-%M-%S')
    record.insert(0, timestamp)
    
    with open(log_file, 'a') as text_file:
        text_file.write(', '.join(map(str, record)) + '\n')
