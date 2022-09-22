sec_num = 7
#while True:
    #guess = int(input("Guess a no. btw 1 and 10: "))
#    if guess == sec_num:
#        print("correct")
 #       break

 # assigns unicode
 # A - Z is 65 - 90
 # a - z is 97 - 122
print("A = ", ord("A"))
print("65 = ", chr(65))

# Enter string to hide in uppercase
enc = input("Enter the string to hide: ")
sec_enc = ""
#Convert it to unicode
for char in enc:
    sec_enc += str(ord(char))
#print the secret message
print("Secret message: ", sec_enc)


#original messege