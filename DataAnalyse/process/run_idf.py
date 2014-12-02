#!/usr/bin/env python

__author__ = "Echo ZHAN"

import os
import peakDetect
import config

import outputGen

event = config.event_mh370
start = config.start_mh370
end = config.end_mh370
interval = config.interval_mh370

wnd = peakDetect.peakWnd(start, end, interval, event)
wnd.find_peak_windows()
wnd.keywgen_idf()

raw_input()