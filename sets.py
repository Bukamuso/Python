#sets - useful when you need to work with a collection of unique elements
'''
my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#union adds both sets together and removes duplicate data
union_set = set1.union(set2)
print(union_set)

#intersection
inter_set = set1.intersection(set2)
print(inter_set)

#Difference - finds the elements present in one but not another
diff_set = set1.difference(set2)
print(diff_set)