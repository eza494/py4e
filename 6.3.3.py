testword = 'banana'
testicker = input('Please input the letter to be checked')

def count(word,ticker):
    counter = 0
    for letter in word:
        if letter == ticker:
            counter = counter +1
    return counter

counter = count(testword,testicker)
print('The letter', testicker, 'came up', counter,'times')
