# Complex Data Types

# Create a list of at  least 5 elements of mixed data types
list = [36, "Brandon", 36.5, True, [1, 2, 3]]
print(list)

# Replace a part of it with with something else
list[3] = 40
print(list)

# Append several more items
list.append("Laila")
list.append("Clarence")
print(list)

# Find and print list length
list_length = len(list)
print(list_length)

# Slice sub-section of list and print save to another list
second_list = list[0:3]

# print second list
print(second_list)

# exetend original list with 2nd list
list.extend(second_list)
print(list)

# Create new list called simList
simList = ["Stone Cold", "Scott Steiner", "Chris Jericho", "Undertaker", "Kane"]

# sort and print simList
simList.sort()
print(simList)

# Copy simList to another 3rd list
third_list = simList.copy()
print(third_list)

# Add 2nd and third list together
fourth_list = simList + third_list
print(fourth_list)
