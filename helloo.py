# elevator converter
ef = input ('europe floor:')
usfloor = 1
uselevator = (int (ef) + usfloor)
print ('usfloor', uselevator)


#if , comparison operators
x = 5
if x < 10:
   print ('smaller')
if x > 20:
   print ('bigger')
print ('done')

#try/except
rawstr = input ('enter a number: ')
try:
    ival = int (rawstr)
except:
    ival = -1
if ival > 0 :
    print ('nice work')
else:
    print ('not a number')
