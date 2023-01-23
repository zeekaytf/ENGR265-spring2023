principal = 1000  # initial amount to be deposited
rate = 1  # interest rate applied to deposit (will be divided by 100)
n = 10  # number of years to compound deposit

# must cast n as 'string' so it can be printed in print()
print("Initial principal is $" + str(principal))
print("Interest rate is " + str(rate / 100))
print("Hold for " + str(n) + " years")

# calculate the eventual result
final = principal * ((1 + (rate / 100)) ** n)

# fancy print the output with two decimal places for floating number
print(f"Final value after is ${final:.2f}")

