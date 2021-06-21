from ctypes import *
import time
import random

valuta = "Rubles"
money = 0
startMoney = 0
playGame = True
defaultMoney = 10000
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

def pobeda(result):
    color(14)
    print(f"    Победа за тобой! Выигрыш составил: {result} {valuta}")
    print(f"    У тебя на счету: {money}")

def lost(result):
    color(12)
    print(f"    К сожалению, поражение: {result} {valuta}")
    print(f"    У тебя на счету: {money}")
    print("    Время отыграться и сыграть ещё!")

def getMaxCount(digit, v1, v2, v3, v4, v5):
    ret = 0
    if (digit == v1):
        ret += 1
    if (digit == v2):
        ret += 1
    if (digit == v3):
        ret += 1
    if (digit == v4):
        ret += 1
    if (digit == v5):
        ret += 1
    return ret

def getOHBRes(stavka):
    res = stavka
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0

    getD1 = True
    getD2 = True
    getD3 = True
    getD4 = True
    getD5 = True
    col = 10

    while (getD1 or getD2 or getD3 or getD4 or getD5):
        if (getD1):
            d1 += 1
        if (getD2):
            d2 += 1
        if (getD3):
            d3 += 1
        if (getD4):
            d4 += 1
        if (getD5):
            d5 += 1

        if (d1 > 9):
            d1 = 0
        if (d2 > 9):
            d2 = 0
        if (d3 > 9):
            d3 = 0
        if (d4 > 9):
            d4 = 0
        if (d5 > 9):
            d5 = 0

        if (random.randint(0, 38) == 1):
            getD1 = False
        if (random.randint(0, 20) == 1):
            getD2= False
        if (random.randint(0, 15) == 1):
            getD3 = False
        if (random.randint(0, 17) == 1):
            getD4 = False
        if (random.randint(0, 26) == 1):
            getD5 = False

        time.sleep(0.1)
        color(col)
        col += 1
        if col > 15:
            col = 10
        print("     " + "%" * 10)
        print(f"    {d1} {d2} {d3} {d4} {d5}")

    maxCount = getMaxCount(d1, d1, d2, d3, d4, d5)

    if (maxCount < getMaxCount(d2, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d2, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d3, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d4, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d5, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)

    color(14)
    if (maxCount == 2):
        print(f" Совпадение двух чисел! Твой выигрыш в размере ставки: {res}")
    elif (maxCount == 3):
        res *= 2
        print(f" Совпадение трёх чисел! Твой выигрыш в размере удвоенной ставки: {res}")
    elif (maxCount == 4):
        res *= 5
        print(f" Совпадение ЧЕТЫРЁХ чисел! Твой выигрыш в размере пяти ставок: {res}")
    elif (maxCount == 5):
        res *= 10
        print(f" Совпадение ВСЕХ чисел! ЭТО ДЖЕКПОТ! Твой выигрыш в размере десяти ставок: {res}")
    else:
        lost(res)
        res = 0

    color(11)
    print()
    input(" Нажми Enter для продолжения...")

    return res

def oneHandBandit():
    global money
    playGame = True
    while playGame:
        colorLine(3, "ПРИВЕТСТВУЮ ТЕБЯ ИГРОК НА ИГРЕ В ОДНОРУКОГО БАНДИТА!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}\n")
        color(5)
        print(" Правила игры: ")
        print("    1. При совпадении 2-х чисел ставка возвращается.")
        print("    2. При совпадении 3-х чисел ставка удваивается.")
        print("    3. При совпадении 4-х чисел ставка увеличивается в пять раз.")
        print("    4. При совпадении всех чисел ты получаешь ДЖЕКПОТ в размере десяти ставок.")
        print("    5. Введите ставку 0 для завершения игры\n")

        stavka = getIntInput(0, money, f"   Введи ставку от 0 до {money}: ")
        if (stavka == 0):
            return 0

        money -= stavka
        money += getOHBRes(stavka)

        if (money <= 0):
            playGame = False
def getDice()\
        :
    count = random.randint(3,8)
    sleep = 0
    while count > 0:
        color(count + 7)
        x = random.randint(1,6)
        y = random.randint(1,6)
        print("" * 10, "_____ _____")
        print("" * 10, f"| {x} | | {y} |")
        print("" * 10, "----- -----")
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1
        return x + y

def dice():
    global money
    playGame = True

    while(playGame):

        print()
        colorLine(3, "ПРИВЕТСТВУЮ ТЕБЯ ИГРОК НА ИГРЕ В КОСТИ!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}\n")

        color(7)
        stavka = getIntInput(0, money, f"   Сделай ставку в пределах {money} {valuta}:")
        if (stavka == 0):
            return 0

        playRound = True
        control = stavka
        oldResult = getDice()
        firstPlay = True

        while(playRound and stavka > 0 and money > 0):

            if (stavka > money):
                stavka = money
            color(11)
            print(f"\n  В твоём расположении {stavka} {valuta}")
            color(12)
            print(f"\n  Текущая сумма чисел на костях: {oldResult}")
            color(11)
            print(f"\n  Сумма чисел на гранях будет больше, меньше или равна предыдущей?")
            color(7)
            x = getInput("0123", "  Введи 1 - если больше, Введи 2 - если меньше, Введи 3 - если равна, Введи 0 - если хочешь выйти: ")

            if (x != "0"):
                firstPlay = False
                if (stavka > money):
                    stavka = money

                money -= stavka
                diseResult = getDice()

                win = False
                if (oldResult > diseResult):
                    if (x == "2"):
                        win = True
                elif (oldResult < diseResult):
                    if (x == "1"):
                        win = True

                if (not x == "3"):
                    if (win):
                        money += stavka + stavka // 5
                        pobeda(stavka // 5)
                        stavka += stavka // 5
                    else:
                        stavka = control
                        lost(stavka)
                elif (x == "3"):
                    if (oldResult == diseResult):
                        money += stavka * 3
                        pobeda(stavka * 2)
                        stavka *= 3
                    else:
                        stavka = control
                        lost(stavka)
                oldResult = diseResult
            else:
                if (firstPlay):
                    money -= stavka
                playRound = False

def getRoulette(visible):
    tickTime = random.randint(100, 200) / 10000
    mainTime = 0
    number = random.randint(0, 38)
    increaseTickTime = random.randint(100, 110) / 100
    col = 1

    while (mainTime < 0.7):

        col += 1
        if col > 15:
            col = 1

        mainTime += tickTime
        tickTime *= increaseTickTime

        color(col)
        number += 1
        if number > 38:
            number = 0
            print()

        printNumber = number
        if printNumber == 37:
            printNumber = "00"
        elif printNumber == 38:
            printNumber = "000"

        print(" Число >", printNumber, "*" * number, " " * (79 - number * 2), "*" * number)

        if visible:
            time.sleep(mainTime)
    return number

def roulette():
    global money
    playGame = True

    while (playGame and money > 0):
        colorLine(3, "ПРИВЕТСТВУЮ ТЕБЯ ИГРОК НА ИГРЕ В РУЛЕТКУ!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}\n")
        color(11)
        print(" Ставлю на... ")
        print("    1. Чётное (выигрыш 1:1)")
        print("    2. Нечётное (выигрыш 1:1)")
        print("    3. Дюжина (выигрыш 3:1)")
        print("    4. Число (выигрыш 36:1)")
        print("    0. Возврат в предыдущее меню")
        x = getInput("01234", "    Твой выбор? ")

        playRoulette = True
        if (x == "3"):
            color(2)
            print()
            print(" Выбери числа:...")
            print("    1. От 1 до 12")
            print("    2. От 13 до 24")
            print("    3. От 25 до 36")
            print("    0. Выйти назад")

            duzhina = getInput("0123", "    Твой выбор на игру? ")
            if duzhina == "1":
                textDuzhina = "от 1 до 12"
            elif duzhina == "2":
                textDuzhina = "от 13 до 24"
            elif duzhina == "3":
                textDuzhina = "от 25 до 36"
            elif duzhina == "0":
                playRoulette = False
        elif (x == "4"):
            chislo = getIntInput(0, 36, "   Введите число от 0 до 36, на которое хотите поставить ")
        color(7)
        if x == "0":
            return 0

        if playRoulette:
            stavka = getIntInput(0, money, f"   Сделай ставку в пределах {money} {valuta}:")
            if stavka == 0:
                return 0

            number = getRoulette(True)
            print()
            color(11)

            if number < 37:
                print(f"    Вам выпало число {number}!" + "*" * number)
            else:
                if number == 37:
                    printNumber = "00"
                elif number == 38:
                    printNumber = "000"
                print(f"    Вам выпало число {printNumber}" + "*" * number)

            if x == "1":
                print("    Ты ставил на ЧЁТНОЕ!")
                if (number < 37 and number % 2 == 0):
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    lost(stavka)
            elif x == "2":
                print("    Ты ставил на НЕЧЁТНОЕ!")
                if (number < 37 and number % 2 == 1):
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    lost(stavka)
            elif x == "3":
                print(f"    Ставка сделана на диапозон чисел {textDuzhina}.")
                if (number > 0 and number < 13):
                    winDuzhina = "1"
                elif (number > 12 and number < 25):
                    winDuzhina = "2"
                elif (number > 24 and number < 37):
                    winDuzhina = "3"
                if duzhina == winDuzhina:
                    money += stavka * 2
                    pobeda(stavka * 3)
                else:
                    money -= stavka
                    lost(stavka)
            elif x == "4":
                print(f"    Ставка сделана на число {chislo}.")
                if number == chislo:
                    money += stavka * 35
                    pobeda(stavka * 36)
                else:
                    money -= stavka
                    lost(stavka)

            print()
            input(" Нажмите Enter для продолжения...")

def loadMoney():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney} {valuta}")
        m = defaultMoney
    return m

def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except FileNotFoundError:
        print("Ошибка создания файла, наше казино закрывается, до свидания!")
        quit(0)

def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)

def colorLine(c, s):
    for i in range(30):
        print()
    color(c)
    print("*" * (len(s) + 2))
    print(" " + s)
    print("*" * (len(s) + 2))

def getIntInput(minimum, maximum, message):
    color(7)
    ret = -1
    while (ret < minimum or ret > maximum):
        st = input(message)
        if st.isdigit():
            ret = int(st)
        else:
            print("     Введите целое число, пожалуйста!!!")
    return ret

def getInput(digit, message):
    color(7)
    ret = ""
    while (ret == "" or not ret in digit):
        ret = input(message)
    return ret

def main():
    global money, playGame

    money = loadMoney()
    startMoney = money

    while (playGame and money > 0):
        colorLine(10, "Приветствую тебя в нашем казино, игрок!")
        color(14)
        print(f" У тебя на счету {money} {valuta}")

        color(6)
        print(" Ты можешь сыграть в: ")
        print("     1. Рулетку")
        print("     2. Кости")
        print("     3. Однорукого бандита")
        print("     0. Выход, Ставка 0 в играх также означает выход")
        color(7)

        x = getInput("0123", "  Твой выбор ? ")

        if x == "0":
            print("123" * 4)
            playGame = False
        elif x == "1":
            roulette()
        elif x == "2":
            dice()
        elif x == "3":
            oneHandBandit()

    colorLine(12, "Жаль, что ты покидаешь нас! Но возвращайся скорей!")
    color(13)
    if money <= 0:
        print(" Упси, кажется, что ты остался без денег. Возьми быстрый кредит и возвращайся")

    color(11)
    if money > startMoney:
        print(" Ну что ж, поздравляю тебя с прибылью!")
        print(f" На начало игры у тебя было {startMoney} {valuta}")
        print(f" Сейчас у тебя уже {money} {valuta}! Играй ещё и побеждай больше!")
    else:
        print(f" К сожалению, ты проиграл {startMoney - money} {valuta}")
        print(" В следующий раз обязательно получится!")

    saveMoney(money)

    color(7)
    quit(0)

main()
