import random
import math

num_list = []
#generates a random string
for i in range(5):
    num_list.append(random.randrange(1,10))

for k in num_list:
    print(k, end=", ")
#list comprehension

even