# IN THE NAME OF GOD
#Learning python by examples

#1-Python Syntax
    #1.1---------------------------------------------------print Hello world!
print("Hello, Wrold!")
print("1st")

    #1.2---------------------------------------------------Comments in python
            #This is a comment

    #1.3---------------------------------------------------
            #multi line comments!


#2-Python Variables
    #2.1---------------------------------------------------
if 5 > 2:
  print("Five is greater than two!")
print("2nd")

    #2.2---------------------------------------------------
x = 5
y = "Hello, wrold!"
print("3rd")

    #2.3---------------------------------------------------add a variable to another variable
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 







#---------------------------------------------------
a = 10
b = 20
if ( a>b ) :
    print("a is larger than b");

else :
    print("wrong");
#---------------------------------------------------
c = 2.3
d = 2.54

print(int(c)+int(d))


print(bin(10))
#---------------------------------------------------
def my_reverse(x):
    return x[::-1]

mytext = my_reverse("I wonder how this text would be reversed !!!")

print(mytext)
#---------------------------------------------------


#---------------------------------------------------
n = input("How many to comapre?")
n = int(n)
i = 0
max = 0
r = n - i

while i<n :
    adad = input("enter the number : " + str(r) + " remaining : ")
    adad = int(adad)
    i = i + 1
    r = n - i
    if adad>max :
        max = adad
    print(max)
    print("i = " + str(i))



