import sys

import logging

reducer_logfile="reducerlog.txt"
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should PRINT
    (not return) one line per UNIT along with the total number of ENTRIESn_hourly
    over the course of May (which is the duration of our data), separated by a tab.
    An example output row from the reducer might look like this: 'R001\t500625.0'

    You can assume that the input to the reducer is sorted such that all rows
    corresponding to a particular UNIT are grouped together.

    Since you are printing the output of your program, printing a debug
    statement will interfere with the operation of the grader. Instead,
    use the logging module, which we've configured to log to a file printed
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''
    old_u=None
    hours=0
    for line in sys.stdin:
        u,v = line.split('\t')
        #logging.info("{0}\t{1}".format(old_u,hours))
        if old_u and u != old_u:
            print("{0}\t{1}".format(old_u,hours))
            hours=0
        hours += float(v)
        old_u = u
    if old_u:
        print("{0}\t{1}".format(old_u,hours))
reducer()

