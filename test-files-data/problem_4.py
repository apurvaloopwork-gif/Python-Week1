# ## Problem 4: API client (30 min)

# Use the free public API at `https://jsonplaceholder.typicode.com/users` (no auth needed, returns fake user data).

# Write a script `problem_04.py` that:

# 1. Fetches the list of users from the API.
# 2. Handles a non-200 response gracefully (print an error, don't crash).
# 3. For each user, extracts: `name`, `email`, `company.name`, `address.city`.
# 4. Saves the extracted fields to `users.csv`.
# 5. Prints a summary: `Saved N users to users.csv`.

# Then add a second function `fetch_user(user_id)` that fetches a single user by ID from `https://jsonplaceholder.typicode.com/users/{user_id}` and returns just their name. Test it by printing the name for IDs 1, 5, 9999 (the last one will 404, your function should return None, not crash).

import requests
import csv

url = "https://jsonplaceholder.typicode.com/users"
r = requests.get(url)

users=r.json()

# 1. Fetches the list of users from the API.
# print(users)


# 3. For each user, extracts: `name`, `email`, `company.name`, `address.city`.
#Saves the extracted fields to `users.csv`.
with open("test-files-data/users.csv","w") as f:
  writer=csv.writer(f)
  writer.writerow(["name","email","company","city"])
  for user in users:
   writer.writerow([user["name"],user["email"],user["company"]["name"],user["address"]["city"]])

print(f"saved {len(users)} users to users.csv") # Prints a summary: `Saved N users to users.csv`.

