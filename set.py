# Create a set of 3 elements
first_set = {"one", "two", "three"}

# add a list of fruits to set
first_list = ["apple", "Banana", "Orange"]
first_set.update(first_list)
print(first_set)

# add car element to set
car_element = ["Toyota"]
first_set.update(car_element)
print(first_set)

# Create second second
second_set = {"some", "odd", "items"}

# save union of first_set and second_set to third_set
third_set = first_set.union(second_set)
print(third_set)

# pop element from second_set
second_set.pop()
print(second_set)

# clear first_set
first_set.clear()
print(first_set)

# Discard and remove item from third_set
third_set.discard("odd")
third_set.remove("some")
print(third_set)
