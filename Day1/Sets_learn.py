##Sets - unordered collection of unique values
s = { 10, 20, 30, 40 , 50 , 60, 70 , 80}
print(type(s))
print(len(s))

print(30 in s) #fast membership testing
print(88 in s)

t = { 30 , 40 , 50 , 60, 90}
print(s.union(t))
print(s.intersection(t))
print(t.difference())


#using operator

print(s|t)  #pipe is "or"--->union
print(s&t) # & is intersection
print(s-t) # minus ---->difference

