# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]


sample_list = [4, 5, 2, 9]
res = list(map(lambda x : x ** 2 , sample_list))
print(f"The Square of the sample list :  {res}")