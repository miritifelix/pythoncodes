def sayhi(name):   #functioon; name is a parameter
    print("hello " + name)

#calling the function
sayhi("Mike")

def say_hi(name, age):
    print("hello " + name + " you are " + age)

say_hi("Felix", "32")

#function to cube a number
def cube(num):
    return num*num*num #allows a value to be returned
print(cube(4))