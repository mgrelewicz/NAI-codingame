import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

tmp = []
value = 0

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    tmp.append(t)


result = min(tmp, key=lambda x:abs(x-value))




# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result)
