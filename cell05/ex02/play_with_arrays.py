first_array = [-123, 0, 1, 20, -25123, 4, 6, 8, 10]
second_array = [i + 2 for i in first_array]
third_array = [i for i in second_array if i > 5]
print(third_array)
