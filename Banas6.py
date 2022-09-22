#converts users words to Acronym and capitalizes them

#Ask for the string
acstring = input("Enter the words to acronymize: ")

#convert the string to uppercase
acstring2 = acstring.upper()
#convert the string to a list
list1 = acstring2.split()
#cycle throught the list
for i in list1:
    print(i[0], end="") #prints and at the same time eliminates new line

#########################
#implementing a cypher ina program by encrypting xters

#receive the message to encrypt and
# number of xters to shift
message = input("Enter message: ")
key = int(input("How many xters should we shift( btw 1-26: "))
#prepare secret message
sec_mes = ""
#cycle through each character in message
for char in message:
    # confirm that the chars are all letters if no keep as is
    if char.isalpha():
       char_code = ord(char)
       char_code += key

