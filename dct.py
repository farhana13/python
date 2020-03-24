#dictionaries week 5 chapter 9
# second data structures, collections - more than one thing in a single variable
#list - ordered collection
#dictionary : put things in, give thme a lable, key value pair...its data collection
#associative array - data structure
# mempory based key value stores

purse = dict()
purse['money'] = 12
purse ['candy'] = 3
purse ['tissues'] = 75
print (purse)
print(purse['candy'])
purse['candy'] = purse ['candy'] + 2
print (purse ['candy'])
#list
lst = list()
lst.append(21)
lst.append(183)
print (lst)
lst[0] = 23
print(lst)
#dictionaries
ddd = dict()
ddd ['age'] = 21
ddd ['course'] = 182
print(ddd)
ddd ['age']= 23
print (ddd)

#dictionary literals use curly braces and have a list of key : value pairs
#make empty dictionary with empty curly braces
jjj = { 'john' : 1, 'bob' : 42, 'jeny' : 100 }
print (jjj)
ppp = { }
print (ppp)

#solving promts using dictionaries, counting with dictionaries
#how often we see something. bus, tram - key, keys in the dictionary, values are as count.
ccc = dict()
ccc ['bus'] = 1
ccc ['tram'] = 1
print (ccc)
ccc['bus'] = ccc['bus']+ 1
print (ccc)
#use in operator to see if a key is in the dictionary

#when we see a new name
counts = dict()
names = ['john', 'mac', 'jeny', 'mac', 'jeny']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts [name] = counts[name] + 1
print (counts)

#the get() method for dictionaries
if name in counts :
    x = counts[name]
else :
    x = 0
x = counts.get(name, 0)

counts = dict()
names = ['john', 'mac', 'jeny', 'mac', 'jeny']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print (counts)
