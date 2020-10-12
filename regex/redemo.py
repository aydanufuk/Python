import re

str = "take 1 up one 23 idea. one idea 45 at a time"

result = re.search(r'o\w',str)

print(result.group())

result = re.findall(r'o\w\w',str)

print(result)

result = re.match(r't\w\w',str)

print(result.group())

result = re.findall(r'o\w{1,2}',str)

print(result)

result = re.split(r'\d+',str)
print(result)

result = re.sub(r'one','X',str)
print(result)

result = re.findall(r'o\w{1,2}',str)

print(result)