
## Problem 1: CSV cleaning pipeline (25 min)

# Read `gyms_input.csv`. For each gym:

# 1. Clean the phone number to 10 digits using the same logic as Test 1, Problem 4 (you can copy-paste it).
# 2. Drop rows where the phone number is invalid (your function returns None).

# 3. Convert `has_website` from "yes"/"no" string to True/False boolean.
# 4. Convert `monthly_revenue` and `google_reviews` from string to int.
# Write the cleaned data to `gyms_cleaned.csv` with the same columns. Also print to console:

# ```
# Loaded 8 rows from gyms_input.csv
# Cleaned 7 rows (dropped 1 with invalid phone)
# Saved to gyms_cleaned.csv
# ```
import csv
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


loaded = 0
cleaned = []

with open("test-files-data/gyms_input.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        loaded += 1

        phone = clean_phone(row["phone"])

        if phone is None:
            continue

        row["phone"] = phone
        row["has_website"] = row["has_website"].lower() == "yes"
        row["monthly_revenue"] = int(row["monthly_revenue"])
        row["google_reviews"] = int(row["google_reviews"])

        cleaned.append(row)

with open("gyms_cleaned.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=cleaned[0].keys())
    writer.writeheader()
    writer.writerows(cleaned)

print(f"Loaded {loaded} rows from gyms_input.csv")
print(f"Cleaned {len(cleaned)} rows (dropped {loaded - len(cleaned)} with invalid phone)")
print("Saved to gyms_cleaned.csv")
  

