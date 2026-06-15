
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

  
  
  
  
  
def clean_phone(raw):
  phone = raw.replace(" ","").replace("-","").replace("+","")
  
  if phone[:2] == "91":
    phone = phone[2:]
    
  if len(phone) == 11 and phone[0]:
    phone = phone[1:]
    
  if len(phone) != 10:
    return None
  
  if phone[0] not in "6789":
    return None 
  
  return phone 


# print(clean_phone( "+91 98765 43210"))

test_inputs = [
    "+91 98765 43210",
    "9876543210",
    "098765-43210",
    "+91-98765 43210",
    "12345",
    "1234567890",
    "+91 8765432109",
    "abc",
    "",
]

for phone in test_inputs:
    result = clean_phone(phone)

    if result:
        print(f"Input: '{phone}' -> {result}")
    else:
        print(f"Input: '{phone}' -> None")