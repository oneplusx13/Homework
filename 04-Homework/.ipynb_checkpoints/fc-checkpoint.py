user_input = input("Please enter your age: " )
age = int(user_input)

if age >= 25:
  print("Renting a car is more affordable")
elif age <= 25 and age >= 18:
  print("Renting a car is very expensive")
elif age < 18:
  print("You cannot legally rent a car")
#else:
#  print("Renting a car is very expensive")
