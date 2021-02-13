# Модули
import time
import random
 
# Переменные
hpuser = 100
hpshot = 50
key = coins = 0
patrons = 2
Circle = True
name = ''
congra = open('congratulations.txt', encoding='utf-8').read().split('\n')
congraLen = len(congra)


# Игровые функции

# Стартовые значения
def reloadGame():
    global hpuser, key, coins, patrons
    hpuser = 100
    key = coins = 0
    patrons = 2
# Стражник
def guard():
    global hpuser, hpshot, Circle
    if Circle == True:
        print("Стражник видит Вас и стреляет")
        time.sleep(5)
        hpuser -= hpshot
        print("Наносит 50 урона ")
        if hpuser <= 0:
            print("Последний выстрел убивает тебя ! THE END !")
            Circle = False
        else:
            shot()
# Сундук
def chase():
    global key, hpuser, coins, Circle
    if Circle == True:
        print(name +''' Осматривает комнату и видит сундук ...
Открывает ...
И получает ... ''')
        time.sleep(3)
        randChase = random.randint(1,3)
        if randChase == 1:
            key += 1
            time.sleep(3)
            print("1 ключ")
        elif randChase == 2:
            hpuser += 30
            time.sleep(3)
            print("30 hp")
        elif randChase == 3:
            coins += 30
            time.sleep(3)
            print("30 монет")
# Закрытый сундук
def closeChase():
    global key, Circle
    if Circle == True:
        if key > 0:
            print(name +''' Осматривает комнату и видит сундук ...
Открывает ...
И получает Письмо ... ''')
    else:
        Circle = False
        print(name +'''[{} проверяет карманы......] Ну что со сной не так ? ...
Не выпало не одного ключа !!!!!! ...
Старик будет расстроен ... '''.format(name))
# Выстрел
def shot():
    global patrons, Circle
    if Circle == True:
        userShot = int(input("Выстрелить в отет или убежать из комнаты ? [1 - Выстрелить, 2 - Убежать]: "))
        if userShot == 1 and patrons > 0:
            print("Ты выстрелил(а) и убил(а) охранника? УРА!")
            time.sleep(5)
            patrons -= 1
            chase()
        else:
            if patrons <= 0:
                print('ШЕЛК!!! ШЕЛК!!! ' + name + ': Ну почему со мной всегда какие-то неприятности? Пистолет не стреляет, это осечка или кончились патроны?')
                guard()
            else:
                print('' + name + ' убегает из комнаты роняя собственное достоинство')
# Комната
def room():
    global Circle, congra, congraLen
    if Circle == True:
        enter = int(input('{} Ты видешь комнату. Желаешь ли ты туда зайти [1 - Да 2 - Нет]: '.format(name)))
        if enter == 1:
            rand = random.randint(1,2)
            if rand == 1:
                guard()
            else:
                chase()
    if Circle == True:
        randCong = random.randint(1,congraLen-1)
        print(congra[randCong])
        time.sleep(5)
# Последняя комната с письмом
def endRoom():
    global Circle, key, hpuser
    if Circle == True:
        enter = int(input('{} Ты видешь последнюю комнату. Желаешь ли ты туда зайти [1 - Да 2 - Нет]: '.format(name)))
        if enter == 1:
            if key > 0:
                key -= 1
                print(key)
                rand = random.randint(1,2)
                if rand == 1:
                    guard()
                    closeChase()
                else:
                    closeChase()
            else:
                Circle = False
                print(name +'''[{} проверяет карманы......] Как так? ...
        Нет ключей !!!!!! ...
        Старик будет расстроен ... '''.format(name))
                hpuser = 0
#     time.sleep(5)
# Конец игры
def endGame():
    global hpuser, name, Circle

    if hpuser > 0:
        print('Старец: Поздравляю ' + name + ' ты смог(ла) найти письмо и выполнил(а) мое задание! Ты прошел(ла) игру!')
    else:
        print('Старец: Не расстраивайся ' + name + ' я уверен тебе повезет в следующий раз!')

    cont = int(input(name + ' Сыграем еще разок? [1 - Да 2 - Нет]: '))
    if cont == 1:
        Circle = True
    else:
        Circle = False
# Интро
input('Приветствую тебя, странник (сидя на ступеньках дома промолвил старец) [Enter - далее >>>]')
input('Старец: Я верю, что тебя мне послала сама судьба! [Enter - далее >>>]')
input('Старец: Мне неоткуда больше ждать помощи ... помоги моему горю ... я вижу по твоим глазам, что ды добрый малый. [Enter - далее >>>]')
input('Неизвесный игрок: Какое горе приключилось с тобой почтенный старец? И чем я могу тебе помочь? [Enter - далее >>>]')
name = input('Старец: Прежде чем я расскажу тебе о своей проблеме, назови мне свое имя странник [Введите Ваше имя]: ')
input('Старец: Рад познакомится с тобой ' + name + '. Моя дочь прислала мне очень важное письмо... [Enter - далее >>>]')
input('Старец: Но когда я доставал его из ящика, подбежал стражник, ударил меня и отобрал письмо... [Enter - далее >>>]')
input('Стрик засмеялся ... Наверное думал что в конверте деньги ...... [Enter - далее >>>]')
input('Старец: Я бы убил его !!!! Но при падении сильно ударился головой и не могу идти [Enter - далее >>>]')
input('Старец: {}, прошу тебя... найди письмо моей дочери и принеси его мне . Я не остановь в долгу пред тобой! [Enter - далее >>>]'.format(name))
input('Старец: Но будь осторожен, стражники вооружены... [Enter - далее >>>]')
input('Возьми с собой мой старый пистолет, в нем всего 2 патрона и иногда он дает осечку, но я все-же думаю что лучше с ним, чем без него! [Enter - начать игру>>>]')

# Начало игрового цикла
while Circle:    
    print('''
--------------------------------------------- Начало игры ------------------------------------------------

{}, перед тобой  коридор с 4 дверьми, в комнатах ты найдешь 2 ключа что-бы отворить последнюю дверь и ящик с письмом
    
'''.format(name))
    room()
    room()
    room()
    endRoom()
    endGame()
    reloadGame()