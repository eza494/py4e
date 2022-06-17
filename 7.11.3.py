fname = input('Enter a file name: ')
try:
    fnamenew = open(fname,'r')
    if fnamenew == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
except :
    print('File cannot be opened:',fname)
    exit()

count = 0
for line in fnamenew:
    if line.startswith('Subject:'):
        count = count +1

print('There were',count,'subject lines in',fname)
