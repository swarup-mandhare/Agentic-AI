# Search for a number entered by the user in:
n = int(input("Enter the number which you want to find :"))
li = [1,4,9,16,25,36,49,64,81,100]
found = False
for i in li :
    if (n == i):
        found = True
if found == True :
    print ("Found")
else :
    print("Not Found")




