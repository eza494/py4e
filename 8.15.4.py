handle = input('Enter name of file: ')
fhand = open(handle)
t = list()
for line in fhand:
    h = line.split()
    for element in h:
        if element in t: continue
        t.append(element)

t.sort()
print(t)
