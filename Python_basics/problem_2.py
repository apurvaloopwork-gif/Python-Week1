# ## Problem 2: EMI calculator (15 min)

# Write a function `calculate_emi(principal, annual_rate, months)` that returns the monthly EMI (a number). Formula:

# ```
# monthly_rate = annual_rate / 12 / 100
# EMI = principal * monthly_rate * (1 + monthly_rate)^months / ((1 + monthly_rate)^months - 1)
# ```

# Test it with these values and print results:

# - Principal: 100000, Rate: 12%, Months: 24
# - Principal: 500000, Rate: 10.5%, Months: 60
# - Principal: 25000, Rate: 18%, Months: 6

# Loan 1: Principal Rs. 100000, Rate 12%, Tenure 24 months -> EMI Rs. XXXX

def calculate_emi(principal,annual_rate,months):
  monthly_rate=annual_rate /12 /100
  Emi = principal * monthly_rate *(1+monthly_rate)**months / ((1+monthly_rate)**months-1)
  return round(Emi,2)

pr = int(input("Enter the principle:"))

ar = int(input("Enter the annual rate:"))

months = int(input("Enter the months:"))

emi = calculate_emi(pr,ar,months)

print(f"Loan 1: Principal:Rs{pr},Rate:{ar},Months:{months}-->Rs{emi}")
