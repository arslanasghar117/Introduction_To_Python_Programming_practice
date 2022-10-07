print("hello world")

x = 1
y = 2
z = x + y

print(x, y, z)


fname = "arslan"
lname = "asghar"
fullname = fname + " " + lname

print(fname + lname)
print(fname + " " + lname)
print(fullname)


sentence = " ali is very good in programming"
sent = "%s %d is very noughty boy"

print(sentence)
print(sent)
print(sent%("jake", (8)))

shoppinglist = ["kella", "amroode", "syab"]
shoppinglist2 = ["jam", "cream", "juice"]

print(shoppinglist + shoppinglist2)
shoppinglist.append("moli")
print(shoppinglist)
del shoppinglist[0]
print(shoppinglist)
print(len(shoppinglist))
