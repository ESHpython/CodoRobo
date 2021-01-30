import random
myself = True



def fride():
    global myself
    if myself == True:
        fride = int(input('Вы хотите открыть хранителя жратвы? (1 - да 2 - нет)'))
        if fride == 1:
            momo()

def momo():
    momo = random.randint(1,1000)
    if momo <= 500:
        print("ты открыл хранителя и он дал тебе огромный дар под названием дошик")
    else:
        allarm()
def allarm ():
    global myself
    allarm = int(input('О нет, сработала сигнальная ракетка! Она ударила маму по морде и та сразу проснулась.ты спрячешся? (1 - нет 2 - да)'))
    if allarm == 1:
        print("мама взяла ракетку и пошла разбиратся и она тебя нашла")
        myself = False
    else:
        dad()
def dad():
    global myself
    dad = random.randint(1,1000)
    if dad <= 500:
        print("ты спрятался в туалете а тебя нашёл батя")
        myself = False 
    else:
        fride()
    
        


def end():
    global myself
    end = int(input("ты продолжишь играть или нет? 1 - да 2 - неа "))
    if end == 1:
        myself = True
    else:
        print('ты просто снова нажмёшь f5')
        myself = False




while myself:
    fride()
    end()