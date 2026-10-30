
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time in Years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)

total_amount = principal + simple_interest
print("Total Amount:", total_amount)
