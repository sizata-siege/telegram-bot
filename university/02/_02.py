# IN THE NAME OF GOD
# 2nd algorithm 

n = input("How many to comapre?")
n = int(n)
i = 1
max = 0
r = n - i

while i<n :
    adad = input("enter the number " + str(r) + " ( remaining ) : ")
    adad = int(adad)
    i = i + 1
    r = n - i
    if adad>max :
        max = adad
    print(max)
    print("i = " + str(i))

print("h")
