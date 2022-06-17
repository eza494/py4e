handle = input('Enter a file name: ')
fhandle = open(handle)
t = list()
for line in fhandle:
    if line.startswith('From'):
        t.append(line)
        h = line.split()
        print(h[1])

print('There were %d lines in the file with From as the first word'%(len(t)))
