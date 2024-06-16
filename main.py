import re

nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}

"""
Advent of Code Part 1 simply comment out the word_idx for loop 
Advent of Code Part 2 uncomment the word_idx for loop
"""
# Look through transmission data
with open('data.txt', 'r') as transmission:
    grand_total = 0
    # Begin decoding algorithm
    for line in transmission:
        answers = {}
        for n in nums:
            # Create two regex patterns based on nums
            digit = re.compile(nums.get(n))
            word = re.compile(n)
            # Look for all instances of nums in string line and return their indexes
            for word_idx in word.finditer(line):
                # Insert location and int value of substring
                answers[word_idx.start()] = nums.get(n)
            for digit_idx in digit.finditer(line):
                # Insert location and int substring
                answers[digit_idx.start()] = digit_idx.group()
        # Sort keys (index locations)
        answers = dict(sorted(answers.items()))
        # Add to the grand total the decoded values
        grand_total = grand_total + int(''.join(list(answers.values()))[:1] + ''.join(list(answers.values()))[-1:])
    print(grand_total)
