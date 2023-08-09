# calculate the sum of numbers until you enter zero

total = 0

number = float(input('Enter a number: '))

# add numbers until number is zero
while number != 0:
    total += number    # total = total + number
    
    # take input again
    number = float(input('Enter a number: '))
    

print('total =', total)