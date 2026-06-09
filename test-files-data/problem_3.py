# ## Problem 3: JSON config + nested data (20 min)

# Create a config file `agency_config.json` with this structure (you write it by hand or via Python, your choice):

# ```json
# {
#   "agency_name": "Loopwork",
#   "team": [
#     {"name": "Vishwajeet", "role": "Designated Partner", "active": true},
#     {"name": "Apoorva", "role": "Founders Office", "active": true}
#   ],
#   "services": [
#     {"name": "Websites", "active": true, "price_range": [8000, 18000]},
#     {"name": "WhatsApp Bots", "active": true, "price_range": [18000, 25000]},
#     {"name": "Lead Gen", "active": false, "price_range": [15000, 50000]}
#   ],
#   "internal_products": ["DSA Agent", "Gig Proofer"]
# }
# ```

# Write a script that:

# 1. Loads the config.
# 2. Prints the agency name.
# 3. Prints the names of all **active** team members.
# 4. Prints the names of all **active** services and their max price.
# 5. Adds a new internal product `"Agency Website Builder"` to the list.
# 6. Saves the modified config back to `agency_config.json` (same file).


import json

# 1. Loads the config.
config_file = "test-files-data/agency_config.json"

with open(config_file,"r") as f:
  aconfig =json.load(f)
 
 # 2. Prints the agency name. 
print("Agency name :",aconfig["agency_name"])
 
 
# 3. Prints the names of all **active** team members.
print("\nActive members are:")
for member in aconfig["team"]:
  if member["active"]:
    print(member["name"])
    
    
# 4. Prints the names of all **active** services and their max price.
print("Active services and their max prices")

for active_services in aconfig["services"]:
  if active_services["active"]:
   max_price = active_services["price_range"][1]
  print("active service name:",active_services["name"],",","Maxium price:",max_price)
  
# 5. Adds a new internal product `"Agency Website Builder"` to the list.

aconfig["internal_products"].append("agency website Builder")
print("Internal products:",aconfig["internal_products"])

# 6. Saves the modified config back to `agency_config.json` (same file).
with open(config_file,"w") as f:
  json.dump(aconfig,f)

