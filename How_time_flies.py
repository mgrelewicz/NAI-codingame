# Marcin Grelewicz (s17692) NAI
import sys
import math
import datetime

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

begin = input()
end = input()

##dt = datetime.datetime.strptime(begin, '%d.%m.%Y')
##print '{0}/{1}/{2:02}'.format(dt.month, dt.day, dt.year % 100)

start = datetime.datetime.strptime(begin, '%d.%m.%Y')
stop = datetime.datetime.strptime(end, '%d.%m.%Y')

output = stop - start

print(output.days)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#print("YY year[s], MM month[s], total NN days")
