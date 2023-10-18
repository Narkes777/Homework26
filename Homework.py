# # Task1
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter_numbers = filter(lambda x: x % 2 == 0, numbers)

# squared_numbers = map(lambda x: x ** 2, filter_numbers)

# result = list(squared_numbers)

# print(result)

# # Task2
# strings = ["Apple", "Banana", "Cherry", "apricot", "Avocado", "grape"]

# filtered_strings = filter(lambda x: x[0] == 'A' and x[0].isupper(), strings)

# lowercase_strings = map(lambda x: x.lower(), filtered_strings)

# result = list(lowercase_strings)

# print(result)

# # Task3
# data = {
#     "a": 3,
#     "b": 7,
#     "c": 1,
#     "d": 10,
#     "e": 6
# }

# filtered_data = {k: v for k, v in data.items() if v > 5}

# cubed_values = {k: v**3 for k, v in filtered_data.items()}

# print(cubed_values)
