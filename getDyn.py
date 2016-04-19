#!/usr/bin/python

# Import libs
import re, sys, urllib


iarg = 'default'
if sys.argv[1:]:
   iarg = sys.argv[1]

if iarg == 'default':
    print "----------------------------------------------------"
    print "    dynEPFL - try to get the dyndns of your host    "
    print "----------------------------------------------------"
    print "... querying http://network.epfl.ch/epnet/dyndns.pl for IP name.."

# Creating sock
sock = urllib.urlopen("http://network.epfl.ch/epnet/dyndns.pl")
# Read sock source
htmlSource = sock.read()
# Closing the sock
sock.close()

#print htmlSource

# Regexping the MMAC.dyn.epfl.ch
p = re.search('(:?<b>)([M][A-Z,0-9]{12})', htmlSource)

# In case of match
if p:
    #print p.groups()[1]
    match = p.groups()[1]
    if iarg == 'default':
        print "... found a match"
        print "The dyndns for your host is " + match + ".dyn.epfl.ch"
    elif iarg == 'url':
       print match + ".dyn.epfl.ch"
    elif iarg == 'mac':
       print match
    else:
       print "Usage ./getDyn.py [url] or [mac]"
# Or...
else:
    print "... no match found, is epnet/dyndns.pl up ?"


# The quick and dirty regex:
#     (:?<b>)([M][A-Z,0-9]{12}) 
# - any improvements are welcome !
