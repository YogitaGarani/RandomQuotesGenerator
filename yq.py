# main program to show quotes
#
#

import getq

# Get list of topics
print (getq.get_topics())

# get quote from user defined topic 
topic = "life"
print (getq.get_quote(topic))

# get quote from any random topic 
print (getq.get_quote("any"))
