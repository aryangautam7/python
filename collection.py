l=["ManU","Juve","Sporting"]
t=("ManU","Juve","Sporting")
s={"ManU","Juve","Sporting"}
for x in l:
    print(x)
print("l[1]="+l[1])
if "ManU" in l:
    print("Yes")
print(len(l))
l.append("Ronaldo")
print(l)
l.insert(3,"RMadrid")
print(l)
l.remove("Sporting")
print(l)
l.pop()
print(l)
x=l.copy()
print(x)
print(type(x))
print(l.count("Juve"))
l1=["Porugal"]
l=["ManU","Juve","Sporting"]
l.sort()
print(l)
l.extend(l1)
print(l)
del l[0]
print(l)
l=["ManU","Juve","Sporting"]
del l
print(l)
l.clear()
print(l)


##s.add("Ronaldo")
##print(s)
##s.remove("Sporting")
##print(s)


