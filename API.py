size_input = input("size pls")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"{square_feet} square feet are {square_metres:.4f} square metres")

user_age = int(input("Enter your age"))
months = user_age * 12

print(f"Your age {user_age}, is equal to {months}.")
dicto = {1: 2, "b": 23}
print(dicto[1])


friends = ["A", "B", "C"]
letter_list = input("Letter please").upper()

print(letter_list in friends)