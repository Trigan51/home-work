#fruits = ["яблоко ", "банан", "киви", "арбуз"]
#right_objekt =len(max(fruits, key=len))
#for inex, item in enumerate(fruits, start=1):
#    print('{}. {}.'.format(inex, item.rjust(right_objekt)))
list_a = [1, 2, 3, 4, 4, 5, 6]
list_b = [3, 4, 5, 6, 7, 8]

for b in list_b:
    while b in list_a:
        list_a.remove(b)
print(list_a)