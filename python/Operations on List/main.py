lst = ["apple","guava","mango","banana","kiwi"]

# 1. Using for loop
print("Length of list:",len(lst))
print("First Element:",lst[0])
print("Last Element:",lst[-1])

lst.append("Papaya")
print("updatd list:",lst)

lst.remove("guava")
print("updated list:",lst)

lst.sort()
print("sorted list:",lst)

lst.pop(1)
print("Updated list",lst)

lst.reverse()
print("Reversed list:",lst)

print("Multiplication of list:",lst*2)

lst = lst[:4]
print("Sliced list:",lst)

lst.clear()
print("Updated list:",lst)