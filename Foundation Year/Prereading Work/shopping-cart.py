flowerpot = 4
seeds = 1
soil = 5
tax = 1.06

potask = int(input("How many flowerpots? "))
seedask = int(input("How many seeds? "))
soilask = int(input("How many soil? "))

cost = potask * flowerpot + seeds * seedask + soilask * soil
total = cost * tax
print(total)

#print((potask * flowerpot + seedask * seeds + soilask * soil) * tax)
