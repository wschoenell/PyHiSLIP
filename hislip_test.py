#!C:\Python34\python.exe
# -*- coding: utf-8 -*-
'''
Created on 22 feb. 2017

@author: Levshinovsky Mikhail
'''
import time

from pyhislip import HiSLIP

a = HiSLIP()
a.connect('172.16.10.60')

a.set_max_message_size(256)

a.device_clear()

a.request_lock()

# Reset
# a.write(":SYSTem:PRESet")
# a.write(":AUT")

# Labels
# a.write(":CHANnel1:LABel 'RS-232'")
# a.write(":DISPlay:LABel 1")

# delay
# a.write("TRIGger:DELay:TDELay:TIME 4.00E-9")  # NR3 format


# horizontal scale

# trigger

# measurements
a.write(":MEASure:NWIDth CHANnel1")
a.write(":MEASure:PWIDth CHANnel1")


# show statistics
a.write(":MEASure:SHOW 1")
a.write(":MEASure:STATistics:DISPlay 1")


while True:
    try:
        time.sleep(1)
        raw_data = a.ask(":MEASure:RESults?").split(',')
        for i in range(0, len(raw_data), 7):
            print(raw_data[i:i + 7])
    except KeyboardInterrupt:
        break

a.release_lock()
a.release_lock()
#
# print(raw_data[0:100])
