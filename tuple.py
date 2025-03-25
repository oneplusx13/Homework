# Create a tuple of 5 elements
first_tuple = ("Charlotte", "Mercedez Mone", "Roxane Perez", "Alexa Bliss", "Rhea Ripley")
print(first_tuple)

# Multiply tuple by 3 and save it to second tuple
second_tuple = first_tuple * 3
print(second_tuple)

# Sort second_tuple and print
convertTupleToList = list(second_tuple)
convertTupleToList.sort()
sortedTuple = tuple(convertTupleToList)
print(sortedTuple)

# Copy 4 specific elements from your 2nd tuple to a new 3nd tuple
third_tuple = second_tuple[:4]
print(third_tuple)

# unpack tuple into 4 variables
(first, second, third, fourth) = third_tuple
print(first)
print(second)
print(third)
print(fourth)

# create fourth tuple
fourth_tuple = (50)
print(fourth_tuple)

# Add second and third tuple together into a 5th tuple
fifth_tuple = second_tuple + third_tuple
print(fifth_tuple)
