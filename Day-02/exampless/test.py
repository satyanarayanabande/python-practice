str1 = "Hello"
str2 = "World"
result = str1+ " MY " +str2
print (result)


#Lenth of the string
text = "python is awsome"
length = len (text)
print ("length of the string:",length)

#string-lowercase.py
text = "python is awsome"
uppercase = text.upper()
lowercase = text.lower()

print("uppercase:",uppercase)
print("lowercase:",lowercase)

#string-replace
text = "python is awsome"
new_text = text.replace ("awsome", "great")

print ("modified text:", new_text)

# string-split
text = "python is awsome"
words = text.split()

print ("words:", words)


#string-strip
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

#string-substring
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")

#Float
# Float variables
num1 = 5.0
num2 = 2.5

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)

output:
Addition: 7.5
Subtraction: 2.5
Multiplication: 12.5
Division: 2.0
Rounded: 3.14

#int
num1= 10
num2= 5

# Integer variables
num1 = 10
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)

#regex-findall
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

output: Pattern found: brown



#regress-match
import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

utput: No match

#import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)

Output: Modified text: The quick red fox jumps over the lazy red dog

#import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

Output: Pattern found: brown
import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)

Output: Split result: ['apple', 'banana', 'orange', 'grape']

#
#





