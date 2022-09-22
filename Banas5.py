#string functions
rand_string = "   this is very important   "
rand_string = rand_string.lstrip() #strips the spaces on the left depnding on the values in the brackets
rand_string = rand_string.rstrip()
rand_string = rand_string.strip()

print(rand_string.lstrip())
print(rand_string.capitalize())
print(rand_string.upper())
print(rand_string.lower())

#manipulating a string
a_list = ["Felix", "Muriithi", "Miriti"]
# you can joing them into a sentence
print(" ".join(a_list))
#we can also split a string
a_list2 = rand_string.split()
for i in a_list2:
    print(i)
#we can also replace a part
print(rand_string.replace("is", "isn't fucking"))