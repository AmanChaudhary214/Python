# Write a Python function that checks whether two given words are anagrams.
"""
Input: "cinema", "iceman"
Output: "True"
"""

str1 = "cinema"
str2 = "iceman"

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    return sorted(str1) == sorted(str2)

result = is_anagram(str1, str2)
print(result)  
