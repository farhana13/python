#building functions, indentations
print ('Imagine')
print ('Lyrics')
def print_lyrics():
    print ('You may say Im a dreamer')
    print ('but Im not the only one')
print('Lets sing')
print_lyrics ()


#parameter
def greet (lang):
    if lang == 'es' :
        print ('hola')
    elif lang == 'fr':
        print ('hi')
    else:
        print ('hello')
greet ('en')
greet ('es')
greet ('fr')


#return values
def greet ():
    return 'hello'
print (greet(), 'John')
print (greet(), 'Bob')

def greet(lang):
    if lang == 'es':
        return 'hola'
    if lang == 'fr':
        return 'hi'
    else:
        return 'hello'
print (greet('en'), 'John')
print (greet('es'), 'Bob')
print (greet('fr'), 'Ray')


#multiple parameters/arguments
def addtwo (a, b):
    added = a + b
    return added
x = addtwo (3, 5)
print (x)


#loops and interation
n = 5
while n > 0 :
    print (n)
    n = n - 1
print ('blastoff!')
print (n)


#indefinite interation,infinite loops, break statement to break get out of the loop,
while true:
    line = input ('> ')
    if line == 'done':
        break
    print (line)
print ('done!')


#continue statement, ends the current interation,
#and jumps to the top of the loop and starts the next interation
while true :
    line = input ('> ')
    if line [0] == '#':
        continue
    if line == 'done':
        break
    print (line)
print ('done!')


#for definite loops
for i in [5, 4, 3, 2, 1] :
    print (i)
print ('blastoff!')

friends =['John', 'Bob', 'Nick']
for friend in friends :
    print ('happy new year:' , friend)
print('done!')


#finding the largest values
largest_so_far = -1
print ('before', largest_so_far)
for the_num in [9, 4, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print ('largest_so_far', the_num)
print ('after', largest_so_far)


#counting total numbers in a loop
zork = 0
print ('before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print (zork, thing)
print ('after', zork)


#total sum up of a series of values, summing in a loops
zork = 0
print = ('before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print ('after', zork)


#finding the everage in a loops
count = 0
sum = 0
print ('before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print (count, sum, value)
print ('after', count, sum, sum/count)


#filtering in a loops
print ('before')
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20 :
        print 'large number', value
print ('after')


#loop idioms
#search using a boolean variable, true/false
found = false
print ('before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = true
        print (found, value)
print ('after', found)

#none , absence of a values
#finding the smallest value in a loop
smallest = none
print ('before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is none :
        smallest = value
    elif value < smallest :
        smallest = value
    print (smallest, value)
print ('after', smallest)
# is and is not operators, use for logical expressions.
