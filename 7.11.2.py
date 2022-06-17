fname = input('Enter a file name: ')
try:
    lines = open(fname,'r')
except :
    print('File cannot be opened',fname)
    exit()

total = 0
count = 0
for line in lines:
    if line.startswith('X-DSPAM-Confidence:') == True:
        count = count+1
        search = int(line.find('0'))
        total = total + float(line[search:])

average = total/count
print('Average spam confidence: ',average)
