li = [1,4,9,16,25,36,49,64,81,100]
n = int(input("enter the num : ")) 
# to find - 36
found = False
for i in li:
    if (n == i):
        found = True
if found :
    print ("Found")
else :
    print ("Not found")