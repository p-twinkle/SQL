# Intersection of Lists/Sets
def intersection(a, b):
  return list(set(a) & set(b))

# --------------------------------------------------------------------------------------------------------
# Weakest Strong Link : Find weakest in each row, but strongest in each column
# I/P: strength = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# O/P: 7 : Weakest in [7, 8, 9]; Strongest in [1, 4, 7]

def weakest_strong_link(strength):
    rows = len(strength)
    cols = len(strength[0])
    
    for i in range(rows):
        for j in range(cols):
            if strength[i][j] == min(strength[i]) & strength[i][j] == max([row[j] for row in strength]):
                return strength[i][j]

    return -1
  
# --------------------------------------------------------------------------------------------------------
# Example #1
# Input: digits = [1, 2, 3]
# Output: [1, 2, 4]
# Example #2
# Input: digits = [6, 9]
# Output: [7, 0]

def another_one(digits):
  num = ''.join(str(d) for d in digits)
  op_num = int(num) + 1
  return [int(d) for d in str(op_num)]

# --------------------------------------------------------------------------------------------------------
# Write a function fizz_buzz_sum to find the sum of all multiples of 3 or 5 below a target value.
# For example, if the target value was 10, the multiples of 3 or 5 below 10 are 3, 5, 6, and 9.
# Because 3+5+6+9=23, our function would return 23.

def fizz_buzz_sum(target):
  ls = [i for i in range(1,target) if (i%3 == 0) or (i%5 ==0)]
  return sum(ls)
  
# --------------------------------------------------------------------------------------------------------
# Check if input list contains duplicates
def contains_duplicate(input)-> bool:
  return len(input) != len(set(input))

# --------------------------------------------------------------------------------------------------------
# Anagram

s = "listen"
t = "silent"

# Solution 1 
from collections import Counter
def is_anagram(s, t):
  ds = Counter(list(s))
  dt = Counter(list(t))
  return sorted(ds) == sorted(dt)

# Solution 2
def is_anagram(s, t):
    ds = {}
    for i in list(s):
        ds[i] = ds.get(i, 0) + 1
    dt = {}
    for i in list(t):
        dt[i] = dt.get(i, 0) + 1
        
    return sorted(ds) == sorted(dt)

is_anagram(s, t)
# --------------------------------------------------------------------------------------------------------
# Palindrome
phrase = "Taco cat."

def isPalindrome(phrase):
    clean = [i.lower() for i in list(phrase) if i.isalnum()]
    rev = clean[::-1]
    return clean == rev
  
isPalindrome(phrase)
# --------------------------------------------------------------------------------------------------------
# Longest consecutive
nums = [100, 4, 200, 1, 3, 2]

def longest_consecutive(nums):
    num = sorted(nums)
    seq = []
    for i in range(len(num)-1):
        if (num[i+1]- num[i]) == 1:
            seq.append(num[i])
            seq.append(num[i+1])
    return len(set(seq))
longest_consecutive(nums)
# --------------------------------------------------------------------------------------------------------
# Length of longest substring - Sliding window
def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set() 
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len,(right - left + 1))
        return max_len
# --------------------------------------------------------------------------------------------------------
# Roman to Integer
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

ip = 'MCMXCIV'
int_ls = [d[roman] for roman in list(ip)]
num = 0
prev = 0
for i in reversed(int_ls):
    curr = i
    if prev > curr:
        num -= curr
    else:
        num += curr
    prev = curr
print(num)
# --------------------------------------------------------------------------------------------------------
# Pangram
def is_pangram(s):
    ls = {c.lower() for c in s if c.isalpha()}
    return len(ls) == 26

is_pangram("The quick brown fox jumps over a lazy dog")
# --------------------------------------------------------------------------------------------------------
# Write a function that removes consecutive duplicates from a list.

def remove_consecutive_duplicates(ls):
    op = [ls[0]]
    op += [ls[i] for i in range(1,len(ls)) if ls[i] != ls[i-1]]
    return op

remove_consecutive_duplicates([1, 2, 2, 3, 3, 3, 4])
# --------------------------------------------------------------------------------------------------------
def group_by_length(word_ls):
    d = {}
    for word in word_ls:
        if len(word) in d.keys():
            val_to_update = d[len(word)] 
            val_to_update.append(word)
        else:
            d[len(word)] = [word]
    return d

group_by_length(["cat", "dog", "elephant", "bat"])
# Output: {3: ['cat', 'dog', 'bat'], 8: ['elephant']}
# --------------------------------------------------------------------------------------------------------
# Top k most frequent words, sorted by frequency (descending), and alphabetically if frequencies match.

words_ls = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

def top_k_frequent_words(words_ls,k):
    d = {}
    for word in words_ls:
        d[word] = d.get(word, 0) + 1
    sorted_words = sorted(d.items(), key = lambda x: (-x[1], x[0]))                    
    return [w for w,c in sorted_words[:k]]
top_k_frequent_words(words_ls, k)

# --------------------------------------------------------------------------------------------------------
