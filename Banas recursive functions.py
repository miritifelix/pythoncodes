#functions that refers to itself
# calls itself inside itself
# 3! = 3 * 2 * 1
def factorial(num):

    if num <= 1:
        return 1
    else:
        result = num * factorial(num-1)
        return result
print(factorial(4))
#solution is 24 but this is how it works
#1st : result = 4 * factorial(3) : 4 * 6
#2nd : result = 3 * factorial(2) : 3 * 2
#3rd : result = 2 * factorial(1) : 2 * 1

#fibbonacci
