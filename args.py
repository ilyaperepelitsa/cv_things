#!/usr/bin/python
__author__ = 'nixCraft'


import sys, getopt

total = len(sys.argv)
# total
cmdargs = str(sys.argv)
# cmdargs
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)


print ("Script name: %s" % str(sys.argv[0]))
for i in xrange(total):
    print ("Argument # %d : %s" % (i, str(sys.argv[i])))
