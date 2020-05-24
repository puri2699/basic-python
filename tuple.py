tuple=(['a','b','c','d','e'],['f','g','h','i'])
print(len(tuple))
print(max(tuple))
print(min(tuple))

tuple1=('b','d','a','e','c','z')
print(sorted(tuple1))
print(tuple1[::-1])

print('z'in tuple)
print('z'in tuple1)

# tuple2= tuple+tuple1
print(tuple[0][0:4])

tuple[1][2]=90
print(tuple)