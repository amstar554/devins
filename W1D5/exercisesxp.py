# ex1
# def FindMax(a):
#     display = max(a)
#     print(display)
#
# a = [0,2,3,5,7,8,9]
# FindMax(a)

# ex2

# def Factorial(n):
#     factorial = 1
#     if int(n) >= 1:
#         for i in range(1,n+1):
#             factorial = factorial * i
#     print("Factorial of ",n , " is : ",factorial)
#
# Factorial(5)

# ex3

# def MySum(a):
#     sum = 0
#     for i in range(0, len(a)):
#         sum = i + sum
#     print(sum)
# b = [1,2,3,4,5,6]
# MySum(b)

# ex4

##count list elements in list without using count

# ex5

# import math
# def L2(a,b,c):
#     sum = 0
#     sumofsquares = a**a+b**b+c**c
#     result = math.sqrt(sumofsquares)
#     print(result)
# L2(1,2,2)

# ex6

# b = [1, 2, 84, 4, 8, 9, 88]
# c = [1, 2, 4, 8, 9, 84, 88]
# sortedb = sorted(b)
#
# def isMono(a):
#     mono = False
#     nmistake, rmistake = 0, 0
#     sortlist = (sorted(a))
#     rsortlist = (sorted(a, reverse=True))
#
#     print(f"Your list: {a}")
#     print(f"Your list in normal sort: {sortlist}")
#     print(f"Your list in normal sort: {rsortlist}")
#
#     for x in range(len(a)):
#         if sortlist[x] != a[x]:
#             nmistake += 1
#         if rsortlist[x] != a[x]:
#             rmistake += 1
#     if nmistake == 0 or rmistake == 0:
#         mono = True
#     print(f"There are {nmistake} normal sort mistakes.")
#     print(f"There are {rmistake} reverse sort mistakes.")
#     print(f"This list is monotonic: {mono}.")
#
# isMono(c)

#ex7
# b = "racecar"
#
# def isPalindrome(a):
#     mistake = 0
#     startcount = 0
#     for letter in a:
#         endcount = len(a) -1 - startcount
#         print("endcount: ", a[startcount], ": startcount: ", a[endcount])
#         if letter != a[endcount]:
#             mistake += 1
#         endcount += 1
#         startcount += 1
#     if mistake == 0:
#         print("Excellent! PALINDROME!")
#     else:
#         print(f"{mistake} mistakes, NOT a palindrome")
#
# isPalindrome(b)

#ex8

# k = 4
# kwords = []
# sentence = "it's wonderful 2 see how wonderful the world is, especially today"
# sentence = sentence.split()
#
# for x in sentence:
#     if len(x) > k:
#         kwords.append(x)
# print("Words with length > k: ", kwords)

#ex9

# b = {'a': 1, 'b': 2, 'c': 8, 'd': 1}
#
# def DicAvg(a):
#     import math
#     print(sum((a.values()))/len(a))
# DicAvg(b)

#ex10
# Write a function that returns common divisors of 2 numbers:

def CommonDiv(a, b):
    adivisors = []
    bdivisors = []
    divisor = 1
    divisor2 = 1
    while divisor +1 < a:
        if a % divisor == 0:
            adivisors.append(divisor)
        divisor += 1
    while divisor2 +1 < b:
        if b % divisor2 == 0:
            bdivisors.append(divisor2)
        divisor2 += 1
    adivisors.append(a)
    bdivisors.append(b)
    print("dividers of the first number: ", adivisors)
    print("dividers of the second number: ", bdivisors)

    def common_elements(adivisors, bdivisors):
        print("here are the common dividers: ", [element for element in adivisors if element in bdivisors])
    common_elements(adivisors, bdivisors)

CommonDiv(27, 81)
