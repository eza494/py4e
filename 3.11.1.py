try:
        Hours = float(input('Enter Hours: '))
        Rate = float(input('Enter Rate: '))
        n =2
except :
        print('Please enter a valid number')
        exit()

if Hours >40:
    Pay = (Hours - 40)*Rate*1.5 + 40*Rate
else:
    Pay = Hours*Rate

print('Pay:', Pay)
