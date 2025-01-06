nums = [0,1,2,3,4,]

# find range of lists

print(nums[1:4])

# list functions


# extend adds list to another list

newnums = [5,6,7,8]
nums.extend(newnums)

# append adds one varible to the end of a list

nums.append(1)

# insert adds varible to a specific index (index, value) pushes all index over
nums.insert(0,69)

# pop removes item from end of a list
nums.pop()

# remove removes specific varible
nums.remove(69)

# clear removes all elements in list
# nums.clear()

# index finds specific index of a value in list 
nums.index(2)

# count returns how many times the value is in list
print(nums.count(1))

# sort returns list sorted in accending order
nums.sort()

# reverse returns reverse of current list state
nums.reverse()

# copy returns a copy of the list
nums2 = nums.copy()

# Tuple similar to list but is immutable (cant be changed or modified)