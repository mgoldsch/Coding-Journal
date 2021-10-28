list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = list1 + list2
print(list3)

list_loop = []
for i in range(10):
    list_loop.append(i)
print(list_loop)

input1 = int(input("a number "))
if input1 % 2 == 0:
    print("the number you entered is even")
else:
    print("the number you entered is odd")

dict1 = {'key1':'value1',
         'key2':'value2'}
print(dict1)
print(dict1['key2'])