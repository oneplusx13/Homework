# Create dictionary
dict1 = {
  "first" : "Stone Cold",
  "second" : "Scott Steiner",
  "third" : "Chris Jericho",
  "fourth" : "Alexa Bliss",
  "Fifth" : "Charlotte" }

# print out value
print(dict1.get("first"))

# replace value with name
dict1["first"] = "Brandon"

# add favorite color
dict1["Favorite Color"] = "Green"

# add list to dictionary
dict1["list"] = ["this", "is", "a", "list"]

# print all keys
for key in dict1.keys():
  print(key)

# print all values
for value in dict1.values():
  print(value)

# Copy dictionary into second dictionary
dict2 = dict1.copy()

# pop item
print(dict2.pop("first"))
print(dict2)

# Remove all elements rom dict2
dict2.clear()
print(dict2)
