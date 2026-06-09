# ## Problem 5: Word frequency (15 min)

# Given this paragraph (paste it as a multi-line string):

# ```
# Apoorva is joining Loopwork as Founders Office. Loopwork builds websites and WhatsApp automation for gyms and clinics. Loopwork will also build DSA Agent and Gig Proofer. Apoorva will own client websites and Apoorva will help build the agency.
# ```

# Write code that:

# 1. Counts how many times each word appears (case-insensitive, ignore punctuation).
# 2. Prints the top 5 most common words with their counts.
# 3. Excludes common stopwords: `["the", "is", "a", "and", "or", "for", "to", "of", "in", "will"]`.

# Format:

# ```
# Top 5 words:
# 1. loopwork: 3
# 2. apoorva: 3
# 3. build: 2
# ...
# ```


para= """ Apoorva is joining Loopwork as Founders Office. Loopwork builds websites and WhatsApp automation for gyms and clinics. Loopwork will also build DSA Agent and Gig Proofer. Apoorva will own client websites and Apoorva will help build the agency. """

stopwords= ["the", "is", "a", "and", "or", "for", "to", "of", "in", "will"]
words = para.split()

for i in words:
  if stopwords[0]==i:
    words.remove(i)
    
    
print(words)