
## Problem 2: Lead scoring + pricing recommendation (30 min)

# Re-use your `score_lead` function from Test 1 Problem 3 (or rewrite).

# Now load `pricing.json` and recommend a package for each lead:

# | Score | Recommendation |
# |-------|----------------|
# | 90 to 100 | `website_plus_bot'|
# | 70 to 89 | `full_website`|
# | 60 to 69 | `basic_website`|
# | Below 60 | Skip (don't recommend)|

# Apply the `first_client_in_area` discount (10%) if the gym is the *first* one in its city (from the cleaned CSV).

# Output a new CSV `gyms_recommendations.csv` with columns:

# ```
# name, city, score, package, base_price, discount_applied, final_price
# ```

# Also print a summary to console:
# ```
# Total leads: 7
# Worth pitching (score >=60): 5
# Skipped: 2
# Total pipeline value: Rs. XXXXX
# ```
# ---

import csv
import json


def score_lead(lead):
    score_counter = 0

    if 100000 <= int(lead["monthly_revenue"]) <= 600000:
        score_counter += 30

    if lead["has_website"] == "False":
        score_counter += 20

    if int(lead["google_reviews"]) >= 10:
        score_counter += 20

    if 10 <= int(lead["google_reviews"]) <= 100:
        score_counter += 30

    return score_counter



with open("test-files-data/pricing.json", "r") as f:
    pricing = json.load(f)

recommendations = []


cities_seen = set()

total_leads = 0
worth_pitching = 0
pipeline_value = 0



with open("test-files-data/gyms_cleaned.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:

        total_leads += 1

        score = score_lead(row)
        
        if score >= 90:
            package = "website_plus_bot"

        elif score >= 70:
            package = "full_website"

        elif score >= 60:
            package = "basic_website"

        else:
            continue

        worth_pitching += 1

       
        base_price = pricing[package]

        
        discount = 0

        if row["city"] not in cities_seen:
            discount = 10
            cities_seen.add(row["city"])

      
        final_price = base_price - (base_price * discount / 100)

       
        pipeline_value += final_price

        recommendations.append({
            "name": row["name"],
            "city": row["city"],
            "score": score,
            "package": package,
            "base_price": base_price,
            "discount_applied": f"{discount}%",
            "final_price": int(final_price)
        })


with open("gyms_recommendations.csv", "w", newline="") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "name",
            "city",
            "score",
            "package",
            "base_price",
            "discount_applied",
            "final_price"
        ]
    )

    writer.writeheader()
    writer.writerows(recommendations)


print("Total leads:", total_leads)
print("Worth pitching:", worth_pitching)
print("Skipped:", total_leads - worth_pitching)
print("Total pipeline value: Rs.", int(pipeline_value))