import time
import random
egg = 0
milk = 0
vegetables = 0


fried_egg = {'name' : 'Яичница', 'egg' : 2, 'milk' : 1, 'vegetables' : 1}
salad = {'name' : 'Салат', 'egg' : 0, 'milk' : 0, 'vegetables' : 4}
stew = {'name' : 'Рагу', 'egg' : 2, 'milk' : 0, 'vegetables' : 3}




game = True
# print('''''')
def chiken():
    if game == True:
        global egg
        print("Ты кормишь кур... ")
        time.sleep(10)
        print("Ты покормил куриц и собрал 4 яйца")
        egg += 4


def cow():
    if game == True:
        global milk
        print("Ты кормишь корову...")
        time.sleep(10)
        print("Ты покормил корову и получил 1 литр молока")
        milk += 1


def kitchen_garden():
    if game == True:
        global vegetables
        print("Ты собираешь овощи...")
        time.sleep(20)
        print("Ты собрал овощи и получил 1 кг овощей")
        vegetables += 4




# while game:
    # choice = int(input("1 - яица, 2 - молоко, 3 - овощи, 4 - завершить игру: "))
    # if choice == 1:
    #     chiken()
    # elif choice == 2:
    #     cow()
    # elif choice == 3:
    #     kitchen_garden()
    # elif choice == 4:
    #     game = False


# print(fried_egg.get("name"))
rand_dish = random.randint(1,3)
if rand_dish == 1:
    print("клиентнт выбрал {}. ".format(fried_egg.get("name")))
elif rand_dish == 2:
    print("клиентнт выбрал {}. ".format(salad.get("name")))
else:
    print("клиентнт выбрал {}. ".format(stew.get("name")))