print (str("Project 1"))

# Value assignations
number = int(input("What is your number?: "))

# Calculations
value = number % 2
# Value check
if value == 0:
    decision = "even"
    print ("Your number " + str(number) + " is an " + decision + " number ")
else:
    decision = "odd"
    print ("Your number " + str(number) + " is an " + decision + " number ")