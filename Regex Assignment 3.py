#!/usr/bin/env python
# coding: utf-8

# # Assigment -3 Regex 

# 1. Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text- 'Python Exercises, PHP exercises.'
# Expected Output: Python:Exercises::PHP:exercises:
# 

# In[1]:


import re
Sample_Text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", Sample_Text))


# 2. Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
# Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
# 

# In[2]:


import pandas as pd
import re

data = {"SUMMARY": ['hello, world!', 'XXXXX test', '123four, five:; six...']}

df = pd.DataFrame(data)

df['SUMMARY'] = df['SUMMARY'].str.replace('[^a-zA-Z\s]', '', regex=True)

print(df)


# In[ ]:





# 3. Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

# In[4]:


import re
text = "The concept of electric cars is relatively new in the automotive industry."
pattern= re.compile(r"\b\w{4,}\b")
matches = pattern.findall(text)
print("Print All Word With at least 4 char string ::", matches)


# In[ ]:





# 4.Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

# In[8]:


import re
text = "The concept of electric cars is relatively new in the automotive industry.An electric vehicle (EV) is one that operates on an electric motor, instead of an internal-combustion engine that generates power by burning a mix of fuel and gases. "
pattern= re.compile(r"\b\w{3,5}\b")
matches = pattern.findall(text)
print("Print All three four and five character string ::", matches)


# In[ ]:





# 5. Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# 

# In[27]:


import re
Sample_Text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)",  "Hello (Data Science World)", "Data (Scientist)"]
for item in Sample_Text:
    rem_paren=re.compile(r" ?\(| ?\)")
    words=re.sub(rem_paren, "", item)
    print(words)




# In[ ]:





# 6. Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# 

# In[30]:


import re
Sample_Text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)",  "Hello (Data Science World)", "Data (Scientist)"]
for item in Sample_Text:
    rem_paren=re.compile(r"\s*\([^)]*\)")
    words=re.sub(rem_paren, "", item)
    print(words)


# In[ ]:





# 7.Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# 

# In[32]:


import re
Sample_Text = "ImportanceOfRegularExpressionsInPython"
pattern=r"[A-Z][a-z]*"
spllit=re.findall(pattern,Sample_Text)
print(spllit)


# 
# 

# 8.Create a function in python to insert spaces between words starting with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# 

# In[55]:


import re
Sample_Text = "RegularExpression1IsAn2ImportantTopic3InPython"
pattern=r"(\d+)([A-Za-z]+)"
space=re.sub(pattern,r" \1\2",Sample_Text)
print(space)


# In[ ]:





# 9.Create a function in python to insert spaces between words starting with capital letters or with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# 

# In[59]:


import re
Sample_Text = "RegularExpression1IsAn2ImportantTopic3InPython"
pattern=r"(\d+)([A-Za-z]+)"
space=re.sub(pattern,r" \1 \2",Sample_Text)
print(space)


# In[ ]:





# 10.Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv
# 

# In[60]:


import pandas as pd
import re

url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)

df['first_five_letters'] = df['Country'].apply(lambda x: x[:6])


# In[61]:


df['first_five_letters']


# In[ ]:





# 11.Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[71]:


import re

string=input("Enter the string ::")
patterns = "^[a-zA-Z0-9_]*$"
if re.search(patterns,string):
  print("Found a match!")
else:
  print('Not matched!')




# In[ ]:





# 12.Write a Python program where a string will start with a specific number. 

# In[74]:


import re
string=input("Enter the string with number::")
text = re.compile(r"^5")
if text.match(string):
 print("Found a match!")
else:
 print("Found not match!")



# 13.Write a Python program to remove leading zeros from an IP address

# In[79]:


import re
ip_address = "006.080.084.190"
string = re.sub(r"\b0+(\d)", r"\1", ip_address)
print(string)


# 14.Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
# 

# In[100]:


import re

Sample_text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."
pattern = r"\b([A-Z][a-z]+) \d{1,2}(?:st|nd|rd|th)? \d{4}\b"
string= re.findall(pattern,Sample_text)
print(string)


# In[ ]:





# 15.- Write a Python program to search some literals strings in a string. 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
# 

# In[101]:


import re

search_words = [ 'fox', 'dog', 'horse' ]
Sample_text = 'The quick brown fox jumps over the lazy dog.'

for pattern in search_words:
    print('Searching for "%s" in "%s" ->' % (pattern, Sample_text),)
    if re.search(pattern,Sample_text):
        print('Matched!')
    else:
        print('Not Matched!')


# In[ ]:





# 16. Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
# 

# In[107]:


import re
Sample_text  = 'The quick brown fox jumps over the lazy dog.'
word='\Wfox\W'
match = re.search(word, Sample_text)
s=match.start()
e=match.end()
if m:
    print('it\'s a match, starts on %d to %d::',s,e)
else:
    print('no match found')


# In[ ]:





# 17.- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'.
# 

# In[115]:


import re
Sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in Sample_text:
    mt=re.findall(pattern, Sample_text)
    
print(mt)  




# In[ ]:





# 18.Write a Python program to find the occurrence and position of the substrings within a string.

# In[125]:


import re
String= 'The concept of electric cars is relatively new in the automotive industry'
sub_string = 'electric'
for matches in String:
    mt=re.finditer(sub_string, String)
    s = m.start()
    e = m.end()
    
print('Found  at %d:%d', s, e)


# In[ ]:





# 19. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[130]:


import re
dt=input("Enter date in yyyy-mm-dd ::")
New_Date=re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

print("Original date in YYY-MM-DD Format: ",dt)
print("New date in DD-MM-YYYY Format: ",New_Date)


# In[ ]:





# 20. Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
# Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
# 

# In[147]:


import re

Sample_Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
pattern = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")

decimal_numbers = pattern.findall(Sample_Text)
print(decimal_numbers)
 


# In[ ]:





# In[ ]:


21. Write a Python program to separate and print the numbers and their position of a given string.


# In[171]:


import re

Sample_text = "we estimate that 18% of new cars sold in 2023 will be electric."  

for m in re.finditer("\d+", Sample_text):
    print(m.group(0))
    print("Index position:", m.start())


# In[ ]:





# 22.- Write a regular expression in python program to extract maximum/largest numeric value from a string.
# Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
# 

# In[172]:


import re

Sample = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

pattern = re.findall(r'\d+', Sample)
num_values = [int(value) for value in pattern]

maximum = max(num_values)

print(maximum)


# 23. Create a function in python to insert spaces between words starting with capital letters.
# Sample Text: “RegularExpressionIsAnImportantTopicInPython"
# 

# In[177]:


import re
Sample_Text= "RegularExpressionIsAnImportantTopicInPython"

space=re.sub(r"(\w)([A-Z])", r"\1 \2", Sample_Text)

print(space)




# In[ ]:





# 24.Python regex to find sequences of one upper case letter followed by lower case letters

# In[179]:


import re
text = "Python Regex to find Sequences Of One Upper case letter Followed by Lower case Letters."
pattern = re.compile(r'\b[A-Z][a-z]+')
matches = pattern.findall(text)
print(matches)



# In[ ]:





# 25.Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# Sample Text: "Hello hello world world"
# 

# In[181]:


import re
Sample_Text="Hello hello world world"
pattern = r'\b(\w+)(\s+\1\b)+'
result = re.sub(pattern, r'\1', Sample_Text)
print(result)




# In[ ]:





# 26. Write a python program using RegEx to accept string ending with alphanumeric character.

# In[185]:


import re

def check(string):
  pattern = r"\w$"
  match = re.search(pattern, string)
  if match:
    return True
  else:
    return False

alphanum="agjaha12"

check(alphanum)


# In[ ]:





# 27.Write a python program using RegEx to extract the hashtags.
# Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# 

# In[186]:


import re

def extract(text):
  hashtags = re.findall(r'#\w+', text)
  return hashtags

Sample_Text= """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <U+00A0><U+00BD><U+00B1><U+0089> "acquired funds" No wo"""

hashtags = extract(Sample_Text)
print(hashtags)



# In[ ]:





# 28. Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
# Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
# 

# In[188]:


import re

Sample_text =  "@Jags123456 Bharat band on 28??<U+00A0><U+00BD><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

pattern = r"<U\+\w{4}>"
result = re.sub(pattern, "", Sample_text)

print(result)



# In[ ]:





# 29.Write a python program to extract dates from the text stored in the text file.
# Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
# 

# In[198]:


import re


Sample_Text=" Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
pattern = r'\d{2}-\d{2}-\d{4}'

dates = re.findall(pattern,Sample_Text)
for d in dates:
  print(d)


# In[ ]:





# In[ ]:


30. Create a function in python to remove all words from a string of length between 2 and 4.
The use of the re.compile() method is mandatory.


# In[199]:


import re

def remove_words(string):
  pattern = re.compile(r'\b\w{2,4}\b')
  modified_string = re.sub(pattern, '', string)
  return modified_string

Sample_text = "we estimate that 18% of new cars sold in 2023 will be electric."
New_string=remove_words(Sample_text)
print(New_string)


# In[ ]:




