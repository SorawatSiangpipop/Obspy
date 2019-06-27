# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:23:37 2019

@author: Omen
"""

from obspy.core import UTCDateTime

time = UTCDateTime("2012-09-07T12:15:00")

print("time= ", time)
print("year= ", time.year)
print("julday= ", time.julday)
print("timestamp= ", time.timestamp)
print("weekday= ", time.weekday)