#ex1

eytanfavbook = "1984"
def favorite_book(a):
    print('my favorite book is ', a)

favorite_book(eytanfavbook)

#ex2

# eytansize = 'MEDIUM'
# eytanmessage = 'Cello World'
#
# def make_shirt(size, message):
#     print(f"The size of the shirt is {size} and message is {message}.")
#
# def make_shirt1(size = 'XL',message = 'Livin lifeeeee'):
#     print(f"The size of the shirt is {size} and message is {message}.")
#
# make_shirt(eytansize, eytanmessage)
# make_shirt1()

#ex3

# magicians = ["Wizboi", "kenny", "lenny", "benwiz"]
#
# def show_magicians():
#     for i in magicians:
#         print(i)
# show_magicians()

#ex4

# magicians = ["Wizboi", "kennywiz", "lennywiz", "benwiz", "wizwoz"]
# great_list =[]
#
# def show_magicians():
#     for i in magicians:
#         print((i))
# show_magicians()
#
# def make_great():
#     for i in magicians:
#         great_list.append(f"The Great {i}")
#     print(", ".join(great_list))
# make_great()

#ex5
def checkDriverAge(age):
    #age = input("What is your age?: ")

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(9)