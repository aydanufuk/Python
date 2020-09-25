lst=[10,20.5,"ufuk",-10.5,30]
print(lst)

print(lst[3])
print(lst[3:5])
print(lst*2)

print(len(lst))

"""adding and removing elements of list"""

lst.append(40)
print(lst)
lst.remove("ufuk")
print(lst)

"""inbuilt python function"""
del(lst[1])
print(lst)

"""remove all the elments of the list"""
lst.clear()
print(lst)

lst.append(1)
lst.append(10.5)
print(max(lst))
print(min(lst))
print(lst)

lst.insert(2,99)
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

