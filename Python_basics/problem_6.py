# ## Problem 6: Bug hunt (15 min)

# Each snippet below has exactly one bug. Identify the bug, fix it, and run the corrected version. Save as `problem_06.py` with all six fixed snippets in order, separated by `# --- Snippet N ---` comments.

# **Snippet A:**
# ```python
# def greet(name):
#     print(f"Hello {name}")
#     return
# greeting = greet("Apoorva")
# print(greeting.upper())
# ```

# **Snippet B:**
# ```python
# gyms = ["Gold's", "Anytime", "Cult"]
# for gym in gyms:
#     print(gym)
# print(f"Last gym: {gym}")
# ```
# (Hint: this one might *look* correct. Run it. Does the output match what you'd expect?)

# **Snippet C:**
# ```python
# income = 25000
# expenses = 18000
# savings_rate = expenses / income
# print(f"Savings rate: {savings_rate}%")
# ```

# **Snippet D:**
# ```python
# def add_tax(price, rate=0.18):
#     return price + price * rate

# invoice = add_tax(1000)
# print(f"With tax: {invoice}")
# print(f"With tax: {add_tax(rate=0.05, 2000)}")
# ```

# **Snippet E:**
# ```python
# nums = [1, 2, 3, 4, 5]
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         nums.remove(nums[i])
# print(nums)
# ```

# **Snippet F:**
# ```python
# def calculate_discount(price, discount_pct):
#     final = price - (price * discount_pct / 100)
#     print(f"Final price: Rs. {final}")

# result = calculate_discount(1000, 20)
# print(result * 2)
# ```

# For Snippet B, write a comment above your fix explaining the *behavior* difference, not just "no bug".

#-------------------------------------------------Solutions-----------------------------------------------------------------#

# **Snippet A:**

def greet(name):
  return f"Hello {name}" #return value was empty and there was no need for print function
  
  
greeting = greet("Apurva")
# print(greeting.upper())


# **Snippet B:**

gyms = ["Gold's", "Anytime", "Cult"]
for gym in gyms:
    print(gym)
print(f"Last gym: {gym}") #items are iterated using for loop in list and last item iterated was cult so after exiting the loop variable stores cult 

# (Hint: this one might *look* correct. Run it. Does the output match what you'd expect?)


# **Snippet C:**

income = 25000
expenses = 18000
savings_rate = round(((income-expenses)/income) * 100)
print(f"Savings rate: {savings_rate}%")


# **Snippet D:**

def add_tax(price,rate):
    return price + price * rate

invoice = add_tax(1000,0.18)
print(f"With tax: {invoice}")
print(f"With tax: {add_tax(2000,0.05)}")


#**Snippet E:**

# nums = [1, 2, 3, 4, 5]

# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         nums.remove(nums[i])


# for i in range(0,6):
#     if nums[i] % 2 == 0:
#         nums.remove(nums[i])

# **Snippet F:**

def calculate_discount(price, discount_pct):
    final = price - (price * discount_pct / 100)
    return final 


result = calculate_discount(1000, 20)
print(result * 2)

