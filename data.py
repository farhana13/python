#while , letter with ssequence numbers
fruit = 'banana'
index = 0
while index < len (fruit) :
    letter = fruit[index]
    print (index, letter)
    index = index + 1

#for , letters in a string
fruit = 'banana'
for letter in fruit :
    print (letter)

# count the number of a specific letter in a word
word = 'farhana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print (count)

#slicing/ grab a pice of a string, (upto but not including the number)
s = 'life is beautiful.'
print (s [0: 4])
print (s [5: 7])
print (s [8:20])
print (s [ : 7])
print (s [8: ])
print (s [ : ])

#string concatenation
a = 'hello'
b = a + 'there'
print (b)
c = a + ' ' + 'there'
print (c)
# in logical statemnt
fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit :
    print ('fount it')

#string library, .lower() , object method, lower case letter.
greet = 'Hello Vasilis'
zap = greet. lower()
print (zap)
print (greet)
print (' Hi there' .lower() )
#upper case letter
greet = 'Dear Vasilis'
nnn = greet. upper()
print (nnn)

#string library , find() function
fruit = 'banana'
pos = fruit.find('na')
print (pos)
aa = fruit.find('z')
print (aa)
#search ans replace
greet = 'Hello Farhana'
nnn = greet. replace ( 'Farhana', 'Yesmin')
print (nnn)
nnn = greet. replace ('h', 'm')
print (nnn)

#stripping whitespaces
greet = '     hello bob   '
ss = greet. lstrip()
print (ss)
pp = greet. rstrip()
print (pp)
rr = greet. strip ()
print (rr)

#prefixes
line = 'Please have a nice day'
gp = line.startswith ('Please')
print (gp)
hp = line.startswith ('p')
print (hp)

#parsing and extracting
data = 'from farhanayesmin13@gmail.com Sat Mar 14:19:15 2020'
atpos = data. find('@')
print (atpos)
sppos = data. find(' ', atpos)
print (sppos)
host = data[atpos+1 : sppos]
print (host)

#
str = 'x-dspam-confidence: 0.8475'
ipos = str. find(':')
print (ipos)
piece = str[ipos+2:]
print (piece)
value = float(piece)
print (value)
print (value + 30)
