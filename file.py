#open a file, flat text,
#handle = open(filename, mode)
#fhand = open('mbox.txt','r')

#newline character
stuff = 'Hello\nWorld!'
stuff
'Hello\nWorld!'
print (stuff)
stuff = 'X\nY'
print (stuff)
sp = len(stuff)
print (sp)

#processing files, read through the files
xfile = open ('mbox.txt')
for cheese in xfile:
    print (cheese)
#counting lines in a files, read only
fhand = open ('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print ('Line count:', count)

#reading the whole files
fhand = open ('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print (len[:20])
#searching through a files
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith ('From:'):
        print (line)
#searching through a file, remove line space
fhand = open ('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print (line)
#skipping with continue
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
#using in to select lines, hilight specific line
fhand = open ('mbox-short.txt')
for line in fhand:
    line = line.rsrtip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

#promt for file filename
fname = input('Enter the file name:  ')
fhand = open(fname)
count = 0
for line in fhand :
    if line.startswith('subject:'):
        count = count + 1
    print ('There were', count, 'subjects lines in', fname)

#try, except
fname = input('Enter the file name:  ')
try:
    fhand = open (fname)
except:
    print ('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject.'):
        count = count + 1
    print ('There were', count, 'subject lines in', fname)




#lists and strings week 4
