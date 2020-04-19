# num = 0

# while (num < 100):
#     num = num + 1
#     if (num % 3 == 0 and num % 5 == 0):
#         print("fizzbuzz")
#     elif (num % 3 == 0):
#         print("fizz")
#     elif (num % 5 == 0):
#         print("buzz")
#     else: 
#         print(num)
    
num = 0

for num in range(101):
    if (num % 3 == 0 and num % 5 == 0):
        print("fizzbuzz")
    elif (num % 3 == 0):
        print("fizz")
    elif (num % 5 == 0):
        print("buzz")
    else:
        print(num)
#range([start], end, [step]) []'s are optional
#step leaves gaps