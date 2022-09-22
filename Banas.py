# Receive miles and convert to km
# 1 km = miles * 1.60934
miles = input('Enter miles: ')

#Convert string to integer
miles = int(miles)

#calculation
km = miles * 1.60934

#print results
print('{} miles eq {} kilometres'.format(miles, km))