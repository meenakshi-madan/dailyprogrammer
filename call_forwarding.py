"""
Developer: Meenakshi Madan

Solution to http://www.reddit.com/r/dailyprogrammer/comments/1g09qy/060913_challenge_127_intermediate_call_forwarding/

"""

from collections import defaultdict
from operator import itemgetter

#Dictionary describing whose calls to forward to whom
forward_dict = {}

#List that will contain call-forward chains for test_day  
forwards = defaultdict(lambda: [])

#- - - Input the data - - -

print "Enter the number of vacation schedule descriptions followed by the descriptions, followed by the test day\n"
n = int(raw_input())
for i in range(n):
	desc = [int(x) for x in raw_input().split()]
	forward_dict[desc[0]] = desc[1:]
test_day = int(raw_input())
	

# - - - Generate call-forward chains - - -
for des in forward_dict.keys():
	callee = des
	try:
		while forward_dict[callee][1] <= test_day and forward_dict[callee][1] + forward_dict[callee][2] > test_day:
			forwards[des].append(forward_dict[callee][0])
			callee = forward_dict[callee][0]
	except KeyError: #Information about the last link in the chain of call-forwards isn't available
		None

		
# - - - Print the results - - -	
if forwards:	
	print "%d call forwardings set up on day %d"%(len(forwards), test_day)
	print "%d call forwardings are the longest chain on day %d"%(len(sorted(forwards.items(), key = itemgetter(1), reverse = True)[0][1]) + 1, test_day)
else:
	print "No call forwardings set up on day %d"%test_day
