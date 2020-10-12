import re

str = "follow string 22-12-2012"

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)