import random
def fride():
    fride = int(input('Вы хотите открыть хранителя жратвы? (1 - да 2 - нет)'))
    if fride == 1:
        momo()
    else:
        print("The end")
        fride = False
def momo():
    momo = random.randint(1,1000)
    if momo <= 500:
        print("ты открыл хранителя и он дал тебе огромный дар под названием дошик")
    else:
        allarm()
def allarm ():
    allarm = int(input('О нет, сработала сигнальная ракетка! Она ударила маму по морде и та сразу проснулась.ты спрячешся? (1 - нет 2 - да)'))
    if allarm == 1:
        print("мама взяла ракетку и пошла разбиратся и она тебя нашла")
    else:
        dad()
def dad():
    dad = random.randint(1,1000)
    if dad <= 500:
        print("ты спрятался в туалете а тебя нашол батя")
    else:
        fride()




fride()
