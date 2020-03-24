fname = input ('Enter File:')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand :
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print (wds)
    for w in wds:
        # print ('**', w, di.get(w,-99)) # -99 is default if the w key doesnt exist in the dict.
        ## if the key is not there the count is zero
        #oldcount = di.get(w,0)
        #print (w, 'old', oldcount)
        #newcount = oldcount + 1
        #di[w] = newcount

        # idion: retrive, create, update, count all in one line
        di [w] = di.get(w,0) + 1
        # print (w, 'new', newcount)
        print (w, 'new', di[w])

        # if w in di :
            # di[w] = di[w] + 1
            # print ('**Existing**')
        # else:
            # di[w] = 1
            # print ('**NEW**')
            # print(w, di[w])
        # print (di[w])
    print (di)

    #find most common words
    largest = -1
    theword = None
    for k,v in di.items() :
        # print (k,v)
        if v > largest :
            largest = v
            theword = k  # remeber the word that was largest
        print (theword, largest)
