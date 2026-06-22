# factorial of a number
n = int(input("Enter the number n to find the factorial of : "))
fac = 1
for i in range (1,n+1):
    fac *= i
print(fac)
