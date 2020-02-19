
import random

print ("hello world")
#this is a comment
if 5 > 2:
    print("5 et sup a 2")
if 2 < 3:
    print("2 est inferieur a 3")

x = 10
y = "henry"
print(x)
print(y)
print(type(y))

a, b, c = "a", "b", "c"
print (a)
print(b)
print(c)

a = b = c = "A"
print (a)
print(b)
print(c)

a = "steph"
b= "henry"
print(a + " " + b)

z = str(10)
print(type(z))
print(z)


#random number
print("random nb : " + str(random.randrange(1,10)))

#multiline string
a = """this is
a multiline string """
print(a)

#string are arrays
a = "hello world!"
print(a[1])  #print e
print(a[2:5]) #print llo
print(a[-5:-2]) #print orl
print(len(a)) #print 12
