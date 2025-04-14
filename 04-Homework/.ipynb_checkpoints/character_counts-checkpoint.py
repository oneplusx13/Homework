def count_characters(input_string):

  char_counts = {}

  for char in input_string:
      if char in char_counts:
          char_counts[char] += 1
      else:
          char_counts[char] = 1

  return char_counts

my_string = input("Enter string: ")
character_counts = count_characters(my_string)
print(character_counts)
