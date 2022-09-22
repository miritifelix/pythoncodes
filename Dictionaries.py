#special structure that allows info to be stored in key value pairs
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    #numbers can also be used
    12 : "December"
}

print(monthConversions["Jan"])
#alternatively
print(monthConversions.get("Jan"))
print(monthConversions[12])