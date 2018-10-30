# ADD an Item to a python LIST
#     1. .append()


# REMOVE an item from a python LIST
#     there is 3 differents ways:
#     1. .remove() - list Object's Remove method.     - remove by item
#     2. .pop()   - list Object's Pop method.         - remove by index
#     3. del      - operator DEL.                     - remove by index


myList = ["prem", 1, 2, 3, "sai,2,3,1"]

# 1) REMOVE()
myList.remove(2)  # by item
print(myList)
# >>> ["prem",1,3,"sai,2,3,1"]
myList.remove(4)
# ERRO!

# 2) POP()
myList.pop(1)  # by index
print(myList)
# >>> ["prem",3,"sai,2,3,1"]
myList.pop(7)
# ERRO!


# 3) DEL
del myList[2]
print(myList)
# >>> ["prem",3,2,3,1"]
del myList[7]
# ERRO!


# ---------- simple sample -------------
myList = ['f', 'a', 's']

# POP - always removes last element of the list
myList.pop()

# POP - pops item at index specified
myList.pop(1)

# DEL - remove item at index specified
del myList[0]

# REMOVE - remove item by value
myList.remove('f')
