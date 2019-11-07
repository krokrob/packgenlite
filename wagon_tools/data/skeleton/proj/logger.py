#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Utility STYCKR python lib
"""

from __future__ import print_function
from datetime import datetime
# removed for check_code
# from glob import glob
# import argparse#
import logging
import os
import sys
import time


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        pass


def get_logger(logfile=None, remove_if_any=False, timestamp=False):
    """
    Return a logger that log on stdout and in LOGFILE
    logfile default filename is 'run.log'
    if timestamp is True timestamp is added to the filename
    if remove_if_any is set to True, old run.log is removed
    """
    timestr = time.strftime('%Y-%m-%d_%Hh%Mmin%Ssec', time.localtime())
    if timestamp:
        if not logfile:
            logfile = 'run_{}.log'.format(timestr)
        else:
            logfile = logfile.split('.log', 1)[0]
            logfile = '{}_{}.log'.format(logfile, timestr)
    else:
        if not logfile:
            logfile = 'run.log'
        if remove_if_any:
            if os.path.isfile('{}'.format(logfile)):
                os.remove('{}'.format(logfile))
        if not logfile.endswith('.log'):
            logfile = '{}.log'.format(logfile)

    logging.basicConfig(filename=logfile, level=logging.INFO, filemode='a')
    logger = logging.getLogger('')

    if len(logger.handlers) == 1:
        logging.getLogger('').addHandler(logging.StreamHandler())

    stdout_logger = logging.getLogger('STDOUT')
    sl = StreamToLogger(stdout_logger, logging.INFO)
    sys.stdout = sl

    stderr_logger = logging.getLogger('STDERR')
    sl = StreamToLogger(stderr_logger, logging.ERROR)
    sys.stderr = sl

    return logger.info


def duration(start, now=None, linehead=''):
    """
    Prettify duration in days, hours, mins and sec
    start = datetime(2015, 10, 11, 1, 46, 31, 151236)
    end   = datetime(2015, 10, 11, 3, 1, 33, 151236)
    assert duration(start, end) == '1 hours 15 min 2 sec'
    start = datetime(2015, 10, 11, 1, 46, 31, 151236)
    end   = datetime(2015, 10, 12, 3, 1, 33, 151236)
    assert duration(start, end) == '1 days 1 hours 15 min 2 sec'
    start = datetime(2015, 10, 11, 1, 46, 31, 151236)
    end   = datetime(2015, 10, 12, 23, 46, 33, 151236)
    assert duration(start, end) == '1 days 22 hours 0 min 2 sec'
    start = datetime(2015, 10, 11, 1, 46, 31, 151236)
    end   = datetime(2015, 10, 11, 1, 55, 13, 151236)
    assert duration(start, end) == '8 min 42 sec'
    start = datetime(2015, 10, 11, 1, 46, 31, 151236)
    end   = datetime(2015, 10, 11, 1, 47, 17, 151236)
    assert duration(start, end) == '0 min 46.0 sec'
    start = datetime(2015, 10, 11, 1, 46, 31, 151236)
    end   = datetime(2015, 10, 11, 1, 47, 17, 131036)
    """
    if not now:
        now = datetime.now()
    delta = now - start
    days, seconds = delta.days, delta.total_seconds()
    hours = int(seconds // 3600 - 24 * days)
    minutes = int((seconds % 3600) // 60)

    seconds = seconds % 60

    if (days, hours, minutes) != (0, 0, 0):
        seconds = int(seconds)
    dateformat = '{} min {} sec'.format(minutes, seconds)
    if hours:
        dateformat = '{} hours '.format(hours) + dateformat
    if days:
        dateformat = '{} days '.format(days) + dateformat
    return linehead + dateformat
