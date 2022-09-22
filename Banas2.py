#o/p based on age
# 1 - 18 -> Important
# 21, 50, > 65 -> Important
#all other are uninmportang

# Receive age and store
age = eval(input('Enter age: ')) #eval automaticaly converts strings to integers
#and : if both are true then return true
#or :  if either condition is true then true
#not : converts a true condition into false
if (age >= 1) and (age <= 18):
    print("Important Birthday")

elif (age == 21) or (age == 50):
    print("Important Birthday")
elif not(age < 65):
    print("Important Birthday")

else:
    print("Sorry not Important Birthday")

