lst=[20,30,40,100,235]
print(type(lst))

b=bytes(lst)
print(type(b))

"""bytes doe not perform adding/modify"""

b1=bytearray(lst)
print(type(b1))

"""bytesarray can be modifiable"""

b1[2]=33
print(b1)