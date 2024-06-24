from stack import Stack

o_array = [0, 9, 4, 74, 51, 120, 66, 44, 77, 20]

print("Original list: ", o_array)
s = Stack(10)

for i in o_array:
    s.push(i)
    print(s)


r_array = []


while s.top != -1:
    r_array.append(s.pop())
    print(s)
    print(r_array)

print("Reverse list: ", r_array)