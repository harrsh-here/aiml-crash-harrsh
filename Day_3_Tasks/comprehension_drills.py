# Solves list comprehension drills alongside examples of dictionary and set comprehensions.
numbers = list(range(1, 21))
div_by_three = [num for num in numbers if num % 3 == 0]
print(div_by_three)

words = ["apple", "pear", "banana", "kiwi", "papaya", "orange"]
long_title_words = [word.title() for word in words if len(word) > 4]
print(long_title_words)

celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0]
fahrenheit_temps = [(c * 9/5) + 32 for c in celsius_temps]
print(fahrenheit_temps)

nested_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)

square_dict = {x: x**2 for x in range(1, 6)}
print(square_dict)

unique_lengths_set = {len(word) for word in words}
print(unique_lengths_set)