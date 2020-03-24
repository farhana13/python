#list constants, another list or list elements, empty list.
print ([1, 24, 76])
print (['red', 'yellow', 'blue'])
print (['red', 24, 98.6])
print ([1, [5, 6], 7])
print ([])
for i in [5, 4, 3, 2, 1]:
    print (i)
print ('blastoff!')
#lists and definite loops
friends = ['John', 'Bob', 'Ray']
for friend in friends :
    print ('Happy new year:',   friend)
print ('Done!')
#friends sub one- (frineds[1]), it will print the second name.
friends = ['John', 'Bob', 'Ray']
print (friends[1])
#lists are mutable, string are not mutable
fruit = 'Banana'
#you cant write - fruit [0]= 'b', to change a number in a list.
x = fruit.lower()
print (x)
lotto = [2, 14, 26, 41, 63]
print (lotto)
lotto[2] = 28
print (lotto)

#how long is a list? len()
greet = 'Hello Bob'
print (len(greet))
x = [1, 2, 3, 'Joe', 99]
print (len(x))

#rage() function returns a list of numbers
print (range(4))
friends = ['Joseph', 'Glenn', 'Sally']
print (len(friends))
print(range(len(friends)))
for i in range(len(friends)):
    friend = friends[i]
    print ('Happy New Year:', friend)

#manipulating lists
#concatenating lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print (c)
#slicing operators, up to but not including
t = [9, 41, 12, 3, 74, 15]
print (t [1:3])
print (t[:4])
print (t[3:])
print (t[:])
#list methods
#x = list()
#type(x)
#dir(x)
#['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#building a list from scartch, add elements into an empty list.
stuff = list()
stuff. append('book')
stuff. append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

#is something is a lists
some = [1, 9, 21, 10, 16]
ll = 9 in some
print (ll)
mm = 15 in some
print (mm)
nn = 20 not in some
print (nn)
if 27 not in some:
    print ('true')

#lists are in order ,
friends = ['Belly', 'Gen', 'Ceny']
friends.sort()
print (friends)
print (friends[1])

#buit-in functions and lists, sum up, average.
nums = [3, 41,12,9,74,15]
print (len(nums))
print (max(nums))
print (min(nums))
print (sum(nums))
print (sum(nums)/len(nums))
#differene of for loops, in Enter data  , if you dont have lists
total = 0
count = 0
while True :
    inp = input('Enter a number:')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count
    print ( 'Average:', average)

##solving same problem with data structure, had problem with this
#####?????
    numlist = list()
    while True :
        inp = input('Enter a number: ')
        if inp == 'done' :
            break
        value = float(inp)
        numlist.append(value)
    average = sum(numlist) / len(numlist)
    print('Average:', average)

#lists and string together, split methods
abc = 'With three words'
stuff = abc.split()
print (stuff)
print (len(stuff))
print (stuff[0])
print (stuff)
for w in stuff :
    print (w)

#delimiter, split
line = 'A lot       of spaces'
etc = line.split()
print (etc)

line = 'first;second;third'
thing = line.split()
print (thing)
print (len(thing))

thing = line.split(';')
print (thing)
print (len(thing))

#see folder file.py

#double split pattern
#?
words = line.split()
email = words[1]
pieces = email.split('@')
print (pieces[1])
