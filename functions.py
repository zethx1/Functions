import itertools

# Grams to ounces
# grams = 200
# def grams_to_ounces(grams):
#     ounces = grams / 28.3495231
#     return ounces
# ounces = grams_to_ounces(grams)
# print (ounces)

#Fahrenheit to Celsium
# F = 200
# def F_to_C(F):
#     C = (5 / 9) * (F - 32)
#     return C
# C = F_to_C(F)
# print (C)

#Heads and legs
# def solve(numheads, numlegs):
#     rabbits = (numlegs - 2 * numheads) / 2
#     chickens = numheads - rabbits
#     if rabbits.is_integer() and chickens.is_integer() and rabbits >= 0 and chickens >= 0:
#         return int(chickens), int(rabbits)
#     else:
#         return "No valid solution"
# numheads = 35
# numlegs = 94
# result = solve(numheads, numlegs)
# if isinstance(result, tuple):
#     chickens, rabbits = result
#     print(f"Number of chickens: {chickens}")
#     print(f"Number of rabbits: {rabbits}")
# else:
#     print(result)

#Prime numbers
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# def filter_prime(numbers):
#     return [num for num in numbers if is_prime(num)]
# numbers = [10, 15, 3, 7, 11, 19, 23, 29, 30]
# prime_numbers = filter_prime(numbers)
# print(prime_numbers)


#Permutations
# def print_permutations(s):
#     permutations = itertools.permutations(s)
#     for p in permutations:
#         print(''.join(p))
# user_input = input("Enter a string: ")
# print_permutations(user_input)

#Sentense reverser
# string = "time to study fast"
# s = string.split()[::-1]
# l = []
# for i in s:
#     l.append(i)
# print(" ".join(l))

#33
# def has_33(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] == 3 and nums[i + 1] == 3:
#             return True
#     return False
# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3])) 
# print(has_33([3, 1, 3]))  

#007
# def spy_game(nums):
#     code = [0, 0, 7]
#     code_index = 0
#     for num in nums:
#         if num == code[code_index]:
#             code_index += 1
#         if code_index == len(code):
#             return True
#     return False
# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))