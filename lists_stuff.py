our_list = [1, 3, 4, 5]

print(our_list)

print(type(our_list))

new_list = ["a", "b", "c", 1, 2, 3, True, False]

print(new_list)

print(new_list[6])
print(new_list[-2])
print(new_list[3:6:])
print(new_list[:5:-1])
print(new_list[6::])

our_list = [1, 2, [3, 4, 5], [6, 7]]
print(our_list)
print(our_list[2])
print(our_list[2][1])
print(our_list[3][1])
our_list.append("new item")
print(our_list)
our_list.pop()
print(our_list)
print(our_list.pop(1))
print(our_list)
print(len(our_list))
print(len(our_list[2]))


