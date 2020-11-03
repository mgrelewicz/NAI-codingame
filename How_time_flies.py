# Marcin Grelewicz (s17692) NAI
import sys
import math
import datetime

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

begin = input()
end = input()

start = datetime.datetime.strptime(begin, '%d.%m.%Y')
stop = datetime.datetime.strptime(end, '%d.%m.%Y')
output = stop - start
days = output.days

if stop.month < start.month:
    months = stop.month + 12 - start.month
    years = stop.year - start.year - 1
else:
    months = stop.month - start.month
    years = stop.year - start.year

if years < 1:
    if months == 0:
        print("total", days, "days")
    elif months == 1:
        print(months, "month, total", days, "days")
    elif months > 1:
        print(months, "months, total", days, "days")
elif years == 1:
    if months == 0:
        print(years, "year, total", days, "days")
    elif months == 1:
        print(years, "year,", months, "month, total", days, "days")
    elif months > 1:
        print(years, "year,", months, "months, total", days, "days")    
elif years > 1:
    if months == 0:
        print(years, "years, total", days, "days")
    elif months == 1:
        print(years, "years,", months, "month, total", days, "days")
    elif months > 1:
        print(years, "years,", months, "months, total", days, "days")
    

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#print("YY year[s], MM month[s], total NN days")


