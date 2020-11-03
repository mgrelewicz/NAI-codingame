# Marcin Grelewicz (s17692) NAI
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

tmp = []
value = 0
result = 0
result0 = 0
result1 = 0

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if t not in tmp:
        tmp.append(t)

if len(tmp) == 0:
    result = 0
elif len(tmp) == 1:
    result = tmp[0]
elif len(tmp) > 1:
    result0 = sorted(tmp, key=lambda x:abs(x-value))[0]
    result1 = sorted(tmp, key=lambda x:abs(x-value))[1]

if abs(result0) == abs(result1):
    result = abs(result0)
elif abs(result0) != abs(result1):
    result = result0

#print(tmp)
#print(result0)
#print(result1)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result)
