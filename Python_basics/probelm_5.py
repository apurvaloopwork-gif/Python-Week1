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

lower_para=para.lower()

for ch in [".", ","]:
    lower_para = lower_para.replace(ch, "")

words = lower_para.split()


#convert into lowercase
#Stopword being treated as a set

stopwords= ["the", "is", "a", "and", "or", "for", "to", "of", "in", "will","as"]
stopword_set=set(stopwords) 

filtered_words=[]

for word in words:
  if word not in stopword_set:
    filtered_words.append(word)
    
    
print(filtered_words)
# ['apoorva', 'joining', 'loopwork', 'founders', 'office.', 'loopwork', 'builds', 'websites', 'whatsapp', 'automation', 'gyms', 'clinics.', 'loopwork', 'also', 'build', 'dsa', 'agent', 'gig', 'proofer.', 'apoorva', 'own', 'client', 'websites', 'apoorva', 'help', 'build', 'agency.']
#This are the filtered words

#apoorva,joining,loopwork,office,builds,websites,whatsapp,automation,gyms,clinics,also,build,dsa,agent,gig,proofer,own,client,agency

# ac = filtered_words.count('apoorva')
# print(ac)

# for word in filtered_words:
#   ac=filtered_words.count('apoorva')
#   print("apoorva =",ac)
# 


already_printed =[]  #Another list to store already printed words

counted_words=[] #List to store counted words


#What this loop will do, loop through filtered words and append the and count of the word in another list ie already printed[] 
for word in filtered_words:
  if word not in already_printed:
    count = filtered_words.count(word)
    print(f"{word} = {count}")
    counted_words.append((word,count))
    already_printed.append(word)


print(counted_words)

rank =1
while rank<=5 and len(counted_words)>0 :
  max_word = counted_words[0]
  
  for item in counted_words:
    if item[1]>max_word[1]:
      max_word=item  
          
  print(f"{rank}.{max_word[0]} :{max_word[1]}")
  counted_words.remove(max_word)
    
  rank+=1
  
