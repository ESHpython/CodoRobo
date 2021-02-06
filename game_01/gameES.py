import time
egg = 0
milk = 0
woll = 0
vegetables = 0
coin = 0

game = True
# print('''''')
def chiken():
    if game == True:
        global egg
        print("Ты кормишь кур... ")
        time.sleep(10)
        print("Ты покормил куриц и собрал 1 десяток яиц")
        egg += 1


def cow():
    if game == True:
        global milk
        print("Ты кормишь корову...")
        time.sleep(10)
        print("Ты покормил корову и получил 1 литр молока")
        milk += 1

def ship():
    if game == True:
        global woll
        print("Ты кормишь овцу...")
        time.sleep(30)
        print("Ты покормил овцу и получил 1 кг шерсти")
        woll += 1


def kitchen_garden():
    if game == True:
        global vegetables
        print("Ты собираешь овощи...")
        time.sleep(20)
        print("Ты собрал овощи и получил 1 кг овощей")
        vegetables += 1

def trade():
    if game == True:
        global egg, milk, woll, vegetables, coin
        tradeEgg = egg * 30
        tradeMilk = milk * 50
        tradeWoll = woll * 100
        tradeV = vegetables * 80
        coin = tradeEgg + tradeMilk + tradeWoll + tradeV
        print("Прибыли от продажи составила: {} рублей.".format(coin))


while game:
    choice = int(input("1 - яица, 2 - молоко, 3 - шерсть, 4 - овощи, 5 - продать, 6 - завершить игру: "))
    if choice == 1:
        chiken()
    elif choice == 2:
        cow()
    elif choice == 3:
        ship()
    elif choice == 4:
        kitchen_garden()
    elif choice == 5:
        trade()
    elif choice == 6:
        game = False