min = None
max = None

while True:

    try:
        num = input('Enter a number: ')
        if num == 'done':
            break
        num = int(num)
    except :
        print('Invalid number')
        continue
    if min is None or min>num:
        min = num
    if max is None or max<num:
        max = num

print('Min is:',min,'\nMax is:',max)
