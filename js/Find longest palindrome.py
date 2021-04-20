# Find longest palindrome
# Given a list of strings as an input to a function, return the length of the string that is the longest palindrome
# Examples
# Input: [‘dad’, ‘racecar’, ‘baseball’]
# Output: 7
# Explanation: racecar is the longest string that is also a palindrome
# Input: [‘rad’, ‘fad’, ‘summer’]
# Output: 0
# Explanation: The list of strings does not contain a palindrome

def longest_palindrome(string_list): 
    longest = 0
    for i in string_list:
        if i == i[::-1] and len(i) > longest:
            longest = len(i)
    return longest
print(longest_palindrome(['dad', 'racecar', 'baseball']))

print(longest_palindrome(['rad', 'fad' , 'summer']))




