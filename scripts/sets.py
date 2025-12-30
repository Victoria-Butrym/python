my_set = {1, 4, 5, 6, 6, 3, 4, 1, 3, 7}
# print(my_set)

my_set.add(43) # adds one item
my_set.update([False, 'new item', 81]) # adds multiple items
my_set.pop()
my_set.remove(81)
# my_set.clear()

print('my set: ', my_set)

list = [1, 3, 4, 5, 78, 4, 2, 4, 2]
unique_list = set(list)

print('list: ', list)
print('unique list: ', unique_list)

my_frozen_set = frozenset([2, 3, 7, 5, 7, 9, 2, 9, 'False', False, 'False'])
print('my frozen set: ', my_frozen_set)
