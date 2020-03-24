#tuples are unmodified lists
x = ('john', 'sally', 'bob')
print ( x[2])
#constant syntax
y = (1, 9, 2)
print (y)
print (max(y))

for iter in y:
    print (iter)
# unlike lists once you create a tuple, you cannt alter its contents-similar to a string.
x = [9,8,7]
x[2] = 6
print (x)

#things not to do with tuples
# x = (3,2,1)
# x.sort()
# x.append(5)
# x.reverse()

# tuple on the left hand side
(x, y) = (4, 'fred')
print (y)
(a, b) = (99, 98)
print (a)

# tuples and dictionaries
# items() method in dict returns a list of key, value tuples.
d = dict()
d ['john'] = 2
d ['bob'] = 4
for (k,v) in d.items() :
    print (k,v)
tups = d.items()
print (tups)

# tuples are comparable
t = (0,1,2) < (5, 1,2)
print (t)
tup = (0,1,2000000) < (0,3,4)
print (t)
tupl= ( 'jenny', 'zob') > ('adams', 'silvi')
print (tupl)

#sorting lists of tuples, keys
d = {'a' : 10, 'b' : 1, 'c' : 22}
p = d.items()
print (p)
pp = sorted (d.items())
print (pp)

#using sorted, key order
d = {'a' : 10, 'b' : 1, 'c' : 22}
tp = sorted(d.items())
print (tp)
for k,v in sorted(d.items()) :
    print (k,v)

#key value tuples- value key
c = {'a' : 10, 'b' : 1, 'c' : 22}
tmp = list()
for k,v in c.items():
    tmp.append( (v, k) )
print (tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

# solve a problem, find ten most common words
fhand = open ('intro.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
lst = list()
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)

for val,key in lst[:10]:
    print (key, val)

#do this in only one line
#list comprehension
c = {'a': 10, 'b':1, 'c':22}
print (sorted ( [ (v , k) for k, v in c.items() ] ) )
