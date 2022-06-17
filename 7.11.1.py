fname = input('Enter a file name: ')
try:
    fnamenew = open(fname,'r')
except :
    print('File cant be opened: ',fname)
    exit()

for line in fnamenew:
    print(line.upper())
