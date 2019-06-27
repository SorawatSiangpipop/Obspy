# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:18:25 2019

@author: Omen
"""

from obspy.core import UTCDateTime

print(UTCDateTime("2012-09-07T12:15:00"))
print(UTCDateTime(2012, 9, 7, 12, 15, 0))
print(UTCDateTime(1347020100.0))
print(UTCDateTime("2012-09-07T12:15:00+02:00"))