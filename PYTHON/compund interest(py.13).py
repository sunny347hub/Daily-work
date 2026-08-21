print("____________________________ COMPOUND INTEREST CALCULATOR _____________________________")
principle = float(input("Enter the principle amount: "))
while principle < 0:
    print("You cannot enter a negative principle amount. Please try again.")
    principle = float(input("Enter the principle amount: "))

rate = float(input("Enter the interest rate (as a decimal): "))
while rate < 0:
    print("You cannot enter a negative interest rate. Please try again.")
    rate = float(input("Enter the interest rate (as a decimal): "))

time = float(input("Enter the time in years: "))
while time < 0:
    print("You cannot enter a negative time. Please try again.")
    time = float(input("Enter the time in years: "))

print(f"The principle amount is: {principle:,.2f}")
print(f"The interest rate is: {rate}")
print(f"The time is: {time} YEARS")

total_amount = principle * pow((1 + rate/100), time)
print(f"The balance after {time} years is: {total_amount:,.2f}")
