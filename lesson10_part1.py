pets = {}
name = {}
while (True):
    print("Введите имя питомца:")
    imya = input()
    if imya in pets:
        print("Это", name["Вид"], "его зовут", imya, "его возраст", name["Возраст"], god, "его владелец", name["Владелец"])
        break
    else:
        print("Животное не найдено! Желаете добавить? Нажмите Y если да и N если нет")
        y = input()
        if y == "Y":
            print("Нужна дополнительная информация")
            
            print("Введите вид питомца:")
            vid = input()
            
            print("Введите возраст питомца:")
            age = int(input())

            god = ''
            if (age % 10 == 1) and (age != 11) and (age % 100 != 11):
                god = 'год'
            elif (1 < age % 10 <= 4) and (age != 12) and (age != 13) and (age != 14):
                god = 'года'
            else:
                god = 'лет'
            
            print("Введите имя владельца:")
            own = input()
            
            name = {"Вид":vid, "Возраст":age, "Владелец":own}
            pets[imya] = name
            
            print("Добавлено!")
            print("Это", name["Вид"], "его зовут", imya, "его возраст", name["Возраст"], god, "его владелец", name["Владелец"])
        
        elif y == "N":
            print("Выход")
            continue
        
        else:
            print("Вводите только Y или N")
            continue