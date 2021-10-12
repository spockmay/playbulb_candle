#!/usr/bin/env python2

import subprocess32 as subprocess
import time

mac_list = ['ac:e6:4b:05:0c:c3',
            'AC:E6:4B:05:44:2D', # Master Bed
#            'AC:E6:4B:05:48:CC', # Living Room
            'ac:e6:4b:05:53:48',
            'AC:E6:4B:05:2B:46'] # Office

clr_list = ['00000000',
            '00000000',
            '00000000',
            '00000000',
            '00000000']

i=0
for mac in mac_list:
    gatt = subprocess.Popen([ 'gatttool','-b',mac,'--char-write','-a','0x16','--value=%s' % (clr_list[i],)])
    time.sleep(2)
    i += 1
