"""
Developer: Meenakshi Madan

Solution to http://www.reddit.com/r/dailyprogrammer/comments/1fnutb/06413_challenge_128_easy_sumthedigits_part_ii/

"""

num = raw_input("Enter a string of digits\n")
while len(num) > 1:
  num = str(reduce(lambda x,y: int(x) + int(y), num))
print num
