'''
issue: "gl2_processing_error" 
Replaced invalid timestamp value in message <message_id> with current time - Value <2024-02-28T8:50:02.485Z> caused exception: Invalid format: "2024-02-28T8:50:02.485Z" is malformed at "T8:50:02.485Z".
setting timestammp in 'time' key ({'time': '2024-02-28T8:50:02.485Z'} not {'timestamp':'2024-02-28T8:50:02.485Z'}) 
to avoid conflict 
'''

import logging
import graypy
import json
from datetime import datetime

my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFUDPHandler('10.0.2.15', 12201)
my_logger.addHandler(handler)

counter = 0
sending_errors = 0

with open(<path_to_cowrie_json_logs>, 'r') as file:
    for line in file:
        json_line = json.loads(line)
        
        if 'timestamp' in json_line:
            json_line['time'] = json_line.pop('timestamp')
            try:
                my_logger.debug(json.dumps(json_line))
                counter += 1
            except Exception as e:
                print(f'Error: {e}')
                sending_errors += 1
        else:
            print(f"Timestamp does not exist: {json_line}")

print(f"Logs sent: {counter}")
print(f"Sending errors: {sending_errors}")
		
