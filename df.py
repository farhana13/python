#counting pattern
counts = dict()
print ('Enter a line of text: ')
line = input ('')
words =line.split()
print ('Words:', words)
print ('Counting...')
for word in words :
    counts[word] = counts.get(word, 0) + 1
    print('Counts', counts)
counts = dict()
line = input ('Enter a line of text:')
words = line.split()

print ('Words:', words)
print ('Counting...')

for word in words:
    counts[word] = counts.get(word,0) + 1
    print('Counts', counts)

#definite loops and files , key value pairs
counts = {'bob': 2, 'jeny' : 42, 'amy' : 100}
for key in counts :
    print ( key, counts[key])

#retriving lists of keys and values
jjj = { 'bob' : 3 , 'john' : 42 , 'jeny' : 100}
print (list(jjj))
print(jjj.keys())
print(jjj.values())
print (jjj.items())
#items gives us back keys and values , called this data structure tuples.
#two iteration variables. aaa-key, bbb-value.
jjj = { 'bob' : 3 , 'john' : 42 , 'jeny' : 100}
for aaa,bbb in jjj.items() :
    print(aaa, bbb)
# dictionaries and files
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount :
        bigcount = word
        bigcount = count
print (bigword, bigcount) 
