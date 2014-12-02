#!/usr/bin/env python
# Filename: config.py

# configuration file
# several important parameters

# parameters of peak time window detection
tao = 2
alph = 0.125

databasePath = '/Users/Michyo/PycharmProjects/TwitterData/db.sqlite3'

event_mh370 = 'MH370'
event_epl = 'epl'
event_earthquake = 'earthquake'

# parameters of time windows
start_mh370 = '2014-03-07 00:00:00.000'
end_mh370 = '2014-04-07 00:00:00.000'
interval_mh370 = '0000-00-00 03:00:00.000'

start_epl = '2014-05-11 12:00:00.000'
end_epl = '2014-05-11 18:00:00.000'
interval_epl = '0000-00-00 00:01:00.000'

start_earthq = '2014-04-01 00:00:00.000'
end_earthq = '2014-04-08 00:00:00.000'
interval_earthq = '0000-00-00 01:00:00.000'

# End of frqcnt.py