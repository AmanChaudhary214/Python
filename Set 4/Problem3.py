# Given a list of strings, find the longest common prefix.
"""
Input: ["flower","flow","flight"]
Output: "fl"
"""

list = ["flower","flow","flight"]


def longest_common_prefix(list):
    if not list:
        return ""
    
    shortest = min(list, key=len)
    
    common_prefix = ""

    for i in range(len(shortest)):
        char = list[0][i]
        if all(s[i] == char for s in list):
            common_prefix += char
        else:
            break

    return common_prefix


result = longest_common_prefix(list)
print(result)
