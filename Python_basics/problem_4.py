
# ## Problem 4: String cleaning (10 min)

# Phone numbers in our database come in many formats. Write a function `clean_phone(raw)` that takes a string and returns just the 10-digit number, or `None` if it's not a valid Indian mobile.

# A valid Indian mobile is 10 digits starting with 6, 7, 8, or 9.

# Test cases (use these exact inputs):

# ```python
# test_inputs = [
#     "+91 98765 43210",
#     "9876543210",
#     "098765-43210",
#     "+91-98765 43210",
#     "12345",
#     "1234567890",
#     "+91 8765432109",
#     "abc",
#     "",
# ]
# ```

# For each input, print:

# ```
# Input: '+91 98765 43210' -> 9876543210
# Input: '12345' -> None (too short)
# Input: '1234567890' -> None (invalid start digit)
# ```

# ---

def clean_phone(raw):
  if(raw[0]==6 or 7 or 8 or 9):
    print(f"Input:{raw} is valid ")


