#ex1
#
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# cat1 = Cat('whiskers', 9)
# cat2 = Cat('puss', 2)
# cat3 = Cat('keto', 3)
#
# def oldestCat():
#     print("oldest cat's age is: ", max(cat1.age, cat2.age, cat3.age))
# oldestCat()

#ex2

# class Dog:
#     def __init__(self, nameDog, heightDog):
#         self.nameDog = nameDog
#         self.heightDog = heightDog
#     def talk(self):
#         print("Woof!")
#     def jump(self):
#         return (self.heightDog * 2)
#
# def biggest_dog(dog1, dog2):
#     biggestdogheigth = max(dog1.heightDog, dog2.heightDog)
#     print("biggest dog height is: ", biggestdogheigth)
#     if biggestdogheigth == dog1.heightDog:
#         dog1.winner = True
#         dog2.winner = False
#     else:
#         dog2.winner = True
#         dog1.winner = False
#
#
# #return -> makes the result of my calculation outside of the function
# davids_dog = Dog("Rex", 50)
# a = davids_dog.jump()
# print(f"Davids doga name is: {davids_dog.nameDog}, and it is {davids_dog.heightDog} cm tall.")
# print(f"{davids_dog.nameDog} can jump {a} cm tall!")
#
# sarahs_dog = Dog("Teacup", 200)
# print(f"sarahs dogs name is: {sarahs_dog.nameDog}, and it is {sarahs_dog.heightDog} cm tall.")
# print(f"{sarahs_dog.nameDog} can jump {sarahs_dog.jump()} cm tall!")
#
# biggest_dog(sarahs_dog, davids_dog)
# print("Davids dog is the biggest: ", davids_dog.winner)
# print("Sarahs dog is the biggest: ", sarahs_dog.winner)

#ex3

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal in self.animals:
            return
        else:
            self.animals.append(new_animal)
    def get_animals(self):
        print(self.animals)

    def sell_animals(self, animals_sold):
        self.animals.remove(animals_sold)
        print(f"Goodbye {animals_sold}!")

sfzoo = Zoo('san francisco zoo')
sfzoo.add_animal("cat")

#missing steps 6,7