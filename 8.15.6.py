t = list()
while True:
    userinput = input('Enter a number: ')
    try:
        if userinput == 'done':
            break
        userinput = int(userinput)
        t.append(userinput)
    except:
        print('Please input a number')
        continue

print('Maximum: ',max(t))
print('Minimum: ',min(t))
