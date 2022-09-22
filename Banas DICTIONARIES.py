

felixdict = {"fname" : "Felix", "lname" : "Miriti",
             "address": "Makongo"}
print("My first name is", felixdict["fname"])

#we can add a new key
felixdict["city"] = "Nakuru"
#we can get the values and keys in the dictionary
print(felixdict.values())
print(felixdict.keys())
#use for loop to print keys and values
for k, v in felixdict.items():
    print(k, v)
#we can create lists that hold dictionaries
employees = []
fname, lname = input("Enter employee first and last name: ").split()
employees.append({'fname': fname, 'lname': lname})
print(employees)
#create a customer list
customer = []

while True:
    req1 = input("Enter Customer (Yes/No) : ")
    if req1 == "y":
        fname, lname = input("Enter customer names: ").split()
        customer.append({'fname': fname, 'lname': lname})

    elif req1 == "n":
        break
    else:
        print("invalid option")
#print customers
for cust in customer:
    print(cust['fname'], cust['lname'])