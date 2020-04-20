#ex0
#
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# apple_count = basket.count("Apples")
#
# print("my basket: ", basket, "apple count: ", apple_count)
#
# basket.clear()
# print("here's your empty basket sir: ", basket)

#ex1
# my_fav_numbers = {23, 7, 1994}
# my_fav_numbers.update([43, 71])
# my_fav_numbers.pop()
#
# friend_fav_numbers = {1,2,3,4,5}
#
# our_fav_numbers = my_fav_numbers | friend_fav_numbers
# print(our_fav_numbers)

#ex2
# my_fav_numbers = (23, 7, 1994)
# my_fav_numbers = my_fav_numbers + (43, 71,)
#
# listx = list(my_fav_numbers)
# listx.pop()
# my_fav_numbers = tuple(listx)
# print("my fav numbers: ", my_fav_numbers)
#
# friend_fav_numbers = (1, 2, 3, 4, 5)
# print("friend fav numbers: ", friend_fav_numbers)
#
# listy = list(friend_fav_numbers)
# our_fav_numbers = tuple(listx + listy)
#
# print("our fav numbers: ", our_fav_numbers)
# print(type(our_fav_numbers))

#ex3
# list = [2 ,1.5, 2.5, 3.5, 3, 4, 2.1, 5]
# list = sorted(list, key = float)
# print(list)

#ex4
# ordercontinue = "no toppings"
#
# while(ordercontinue):
#     answer = input("What else?: ")
#     if (answer == "quit"):
#         print("thank you come again")
#         ordercontinue = False


#ex5 & 7 & 8
#
# print("Welcome to the movie theater, tell me your age and I will add to your total. if you're done, enter 99.")
# ordercontinue = True
# total = []
# order = None
# banned = []
#
# while(ordercontinue):
#     order = input("Who else? Tell me their ages --> ")
#     order = int(order)
#
#     if (3 > order):
#         print("children go free, lucky!")
#     elif (3 < order < 12):
#         total.append(10)
#         print("a kid! that's 10 bucks!")
#     elif(16 < order < 21):
#         print("you can't get in! We hate this age!")
#         banned_name = input("what is your name!? I will ban you!: ")
#         banned.append(banned_name)
#     elif (order > 12 and order != 99):
#         total.append(15)
#         print("an adult! that's 15 bucks!")
#     if (order == 99):
#         ordercontinue = False
#
# print("That's ", total.count(15), " adults, ", total.count(10)," kids and ", total.count(0), " babies.", "Your total is: $", sum(total))
# print("Banned people names: ", banned)

#ex8

# nums = [99,1,2,3,4,5,6,7,8,9,10]
#
# for num in nums:
#     if (num % 2 == 0):
#         print(num)

#ex10

users = ["John", "Kerry", "Lenny", "Benny", "Jenny"]

for name in users:
    print("User name: ", name)
    age = input("Age?: ")
    age = int(age)
    if (age < 16):
        users.remove(name)
        print(name, " is removed")
print(users)