# ## Problem 5: Build the lead message generator (15 min)

# This is a real tool you'll use for client outreach.

# Read `gyms_recommendations.csv` from Problem 2. For each gym with a score >= 60, generate a personalised WhatsApp message using this template:

# ```
# Hi {gym_name} team,

# I'm Apoorva from Loopwork. We help gyms in {city} get more trial bookings and reduce no-shows.

# For your size, we'd recommend our {package_friendly_name} package at Rs. {final_price}. {discount_note}

# 15 minutes this week to show you how it works?

# - Apoorva
# ```

# Where:

# - `package_friendly_name` is "Website + WhatsApp Bot" / "Full Website" / "Basic Website" (not the raw key from pricing.json).
# - `discount_note` is "First gym in {city} gets 10% off." if discount applied, else "" (empty string).

# Save each message to a separate text file: `outreach/{gym_slug}.txt` where `gym_slug` is the gym name lowercased with spaces replaced by underscores. Example: `outreach/gold_s_gym_andheri.txt`.

# Print to console:

# ```
# Generated 5 outreach messages in outreach/
# ```

# ---
import csv
import os

count=0

with open("test-files-data\gyms_recommendations.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:

        if row["package"] == "website_plus_bot":
            package_name = "Website + WhatsApp Bot"

        elif row["package"] == "full_website":
            package_name = "Full Website"

        else:
            package_name = "Basic Website"

        
        if row["discount_applied"] == "10%":
            discount_note = (
                f"First gym in {row['city']} gets 10% off."
            )
        else:
            discount_note = ""

        
        message = f"""Hi {row['name']} team,

I'm Apoorva from Loopwork. We help gyms in {row['city']} get more trial bookings and reduce no-shows.

For your size, we'd recommend our {package_name} package at Rs. {row['final_price']}. {discount_note}

15 minutes this week to show you how it works?

- Apoorva
"""


       
        gym_slug = row["name"].lower().replace(" ", "_")

       
        with open(f"test-files-data/outreach/{gym_slug}.txt", "w", encoding="utf-8") as file:
            file.write(message)

        count += 1

print(f"Generated {count} outreach messages in outreach/")