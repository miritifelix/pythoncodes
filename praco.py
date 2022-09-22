name = "Felix Miriti"
print(name + " is getting old")

# manipulating the string
print(name.lower())  #converts to lowercase
print(name.islower()) #checks whether it is lowercase or not
print(name.upper().isupper()) #combining two
print(len(name)) #checks length of string
print(name[0]) #picks the first index/xter of the string
print(name.index(" ")) #returns the position of the character in quotes
print(name.replace("Felix", "Andrew")) #replaces a string that has been specified

#getting input from user/prompts the user
age = input("Enter your age: ")
print("You are " + age + " years old")
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
result = int(num1) + int(num2) #int function changes to integers
print(result)

#lists
friends = ["Flora", "Jeff", "Sharon", "Mike"]
print(friends[0]) #picks the one at index stated
#can be ussed to even replace
friends[0] = "Fiona"








