first_array = [-123, 9, 9, 8, 1, 20, 20,  -25123, 4, 6, 8, 10]
second_array = [i + 2 for i in first_array]
third_array = [i for i in second_array if i > 5]
print(set(third_array))
