try:
    Hours = float(input('Enter Hours: '))
    Rate = float(input('Enter Rate: '))
    n =2
except :
    print('Please enter a valid number')
    exit()


def computepay(hours,rate):

    if hours >40:
        pay = (hours - 40)*rate*1.5 + 40*rate
    else:
        pay = hours*rate
    return pay

pay = computepay(Hours,Rate)
print('Pay:',pay)
