# ## Problem 3: Lead scorer (15 min)

# You're given a list of dictionaries representing gym leads:

# ```python
# leads = [
#     {"name": "Gold's Gym Andheri", "monthly_revenue": 250000, "has_website": False, "google_reviews": 12},
#     {"name": "Cult Fitness Powai", "monthly_revenue": 800000, "has_website": True, "google_reviews": 240},
#     {"name": "Local Gym Borivali", "monthly_revenue": 80000, "has_website": False, "google_reviews": 3},
#     {"name": "Anytime Fitness Bandra", "monthly_revenue": 500000, "has_website": True, "google_reviews": 90},
#     {"name": "Iron Paradise Vile Parle", "monthly_revenue": 180000, "has_website": False, "google_reviews": 28},
# ]
# ```

# Write a function `score_lead(lead)` that returns a score (0 to 100) based on:

# - +30 points if `monthly_revenue` is between 100000 and 600000 (sweet spot for our pricing)
# - +20 points if `has_website` is False (more upside)
# - +20 points if `google_reviews` is at least 10 (active business)
# - +30 points if `google_reviews` is between 10 and 100 (room to grow with our review tool)

# Then loop through `leads`, score each, and print only the leads with a score of 60 or higher, sorted by score (highest first). Format:

# ```
# [Score 80] Gold's Gym Andheri
# [Score 70] Iron Paradise Vile Parle
# ```


leads = [
    {"name": "Gold's Gym Andheri", "monthly_revenue": 250000, "has_website": False, "google_reviews": 12},
    {"name": "Cult Fitness Powai", "monthly_revenue": 800000, "has_website": True, "google_reviews": 240},
    {"name": "Local Gym Borivali", "monthly_revenue": 80000, "has_website": False, "google_reviews": 3},
    {"name": "Anytime Fitness Bandra", "monthly_revenue": 500000, "has_website": True, "google_reviews": 90},
    {"name": "Iron Paradise Vile Parle", "monthly_revenue": 180000, "has_website": False, "google_reviews": 28},
]

def score_lead(lead):
    score_counter = 0

    if 100000 <= lead["monthly_revenue"] <= 600000:
        score_counter += 30

    if lead["has_website"] == False:
        score_counter += 20

    if lead["google_reviews"] >= 10:
        score_counter += 20

    if 10 <= lead["google_reviews"] <= 100:
        score_counter += 30

    return score_counter

# print(score_lead(leads[0]))


already_scored = []

for lead in leads:
   score = score_lead(lead)

   if score >= 60:
      already_scored.append((score,lead["name"]))


# print(already_scored)


already_scored.sort(reverse=True)

# print(already_scored)

for score,name in already_scored:
    print(f"[{score}] {name}")