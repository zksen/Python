from sys import argv

name, time, bid, premium = argv
print((int(time) * int(bid)) + int(premium))
