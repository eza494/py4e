count = 0
total = 0
while True:

    try:
        num = input('Enter a number: ')
        if num == 'done':
            break
        num = int(num)
    except :
        print('Invalid number')
        continue
    count = count + 1
    total = num + total

average = total/count
print(total,'',count,'',average)
