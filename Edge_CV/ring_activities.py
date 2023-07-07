# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:22:48 2023

@author: ifrommer
"""
import ring_test 

ring = ring_test.main()

devices = ring.devices()

stickup_cams = devices['stickup_cams']

side = stickup_cams[0]
#%%
for dev in list(devices['stickup_cams']):
    dev.update_health_data()
    print('\nAddress:    %s' % dev.address)
    print('Family:     %s' % dev.family)
    print('ID:         %s' % dev.id)
    print('Name:       %s' % dev.name)
    print('Timezone:   %s' % dev.timezone)
    print('Wifi Name:  %s' % dev.wifi_name)
    print('Wifi RSSI:  %s' % dev.wifi_signal_strength)
    

#%%
for camera in stickup_cams:

    # listing the last 15 events of any kind
    for event in camera.history(limit=15):
        print('ID:       %s' % event['id'])
        print('Kind:     %s' % event['kind'])
        print('Answered: %s' % event['answered'])
        print('When:     %s' % event['created_at'])
        print('--' * 50)

    # get a event list only the triggered by motion
    events = camera.history(kind='motion')
    #print('\n',events)
#%%  this worked
#camera.recording_download(camera.history()[0]['id'],
#                          filename='test_download.mp4')

#side_hist = side.history(limit=500); print(len(side_hist))
# above worked, got 500 events from 5/19/23 back to 4/19/23
# looks like it maxed out at 745 events, back to 3/20/23

# the video was 5.3 Mb and 30 seconds long
# all 745 would take up about 4 Gb
# my work laptop has 327 GB free, so plenty of room

def make_file_name(history_event):
    """ Parameter:  history_event : dict
          ring camera event with many useful fields
    Returns:    string file_name              """
    prefix = 'data/'; suffix = '.mp4'
    file_name_format = '%Y_%m_%d_%H_%M_%S'  
    
    event_date_time   = history_event['created_at']
    event_date_string = event_date_time.strftime(file_name_format)
    file_name = prefix + event_date_string + suffix 
    return file_name

side_hist = side.history(limit=900)   # can go up to around 861 (as of 5/25)

import time
start_time = time.time()
#%%
VIDS_TO_DOWNLOAD = range(416, 448) #829,861)
for i in VIDS_TO_DOWNLOAD:
    current_event: dict = side_hist[i]
    file_name = make_file_name(current_event)
    print('downloading ',file_name, ' file ',i,' of ',VIDS_TO_DOWNLOAD[-1])
    side.recording_download(current_event['id'], filename=file_name)
elapsed_time = time.time() - start_time
print('Elapsed time (in seconds) = ', elapsed_time)
print('Time per download (in seconds) = ', 
      elapsed_time / len(VIDS_TO_DOWNLOAD))