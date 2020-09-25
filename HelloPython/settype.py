st={10,20,30,"xyz"}
print(st)
print(type(st))

st.update([88,99])
print(st)

st.remove(30)
print(st)

"""set type does not allow indexing slicing, repetition"""

f=frozenset(st)

"""frozen set does not allow update and remove"""

