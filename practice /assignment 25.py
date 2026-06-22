# Print numbers from 1 to 100.
# For every multiple of 3 print: fizz

for i in range (1, 101):
    if (i%3 ==0 and i%5 == 0):
        print("fizzbuzz")
    elif (i%5 == 0):
        print ("Buzz")
    elif (i%3 == 0):
        print ("Fizz")
    else:
        print(i)