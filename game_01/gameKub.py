import time
import random
Your_victory = 0
Dimas_victory = 0
# Имя
name = input("Введите ваш ник ")
# Правила
print("Привет " + name + ''' Твоя задача такова:
Ты должен бросать кубики
Против тебя играет другой апанент
Его зовут Дима Ахтыжтварьев
кто первый набьёт на кубиках 66, тот и победит''')
while Your_victory < 66 or Dimas_victory < 66:
    
    

    # Ты_бросаешь_кубики

    print("Ты бросаешь кубик и...")
    rand1 = random.randint(1,6)
    print("Ты бросаешь второй кубик и...")
    rand2 = random.randint(1,6)
    print("тебе выпало " + str(rand1))
    print("тебе выпало " + str(rand2))
    Your_victory += rand1 + rand2

    # Твой_апанент_бросает_кубики

    print("Он бросает кубик и...")
    rand1 = random.randint(1,6)
    print("Он бросает второй кубик и...")
    rand2 = random.randint(1,6)
    print("Ему выпало " + str(rand1))
    print("Ему выпало " + str(rand2))
    Dimas_victory += rand1 + rand2


if Your_victory > Dimas_victory:
    print("Ты победил!")
else:
    print("Победил Дима Ахтыжтварьев!")

print("Ты набрал" + str(Your_victory) + " очков")
print("Он набрал" + str(Dimas_victory) + " очков")
