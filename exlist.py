#exercise lists, parsing, read some mailbox data , sat - days
han = open ('mbox-short.txt')
for line in han :
    line = line.rstrip()
    wds = line.split()
    #durdian in a compound statement
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print (wds[2])
