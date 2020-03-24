#try, except
hr = input ('enter hours: ')
rt = input ('enter rate: ')
try:
    hrt = float (hr)
    rtt = float (rt)
except:
    print ('error, please enter numeric input')
    quit()
print (hrt, rtt)
if hrt > 40.0 :
    reg = hrt * rtt
    opt = (hrt - 40.0) * (rtt * 0.5)
    xp = reg + opt
else:
    xp = hrt * rtt
print ('pay:', xp)
