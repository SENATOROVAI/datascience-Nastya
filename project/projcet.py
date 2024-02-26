data_base = {'login':'Sheca', 'password':'12345'}
def login():
    print()
def sign_up():
    work_with_login = True
    work_with_password = True
    while work_with_login is True:
        register_login = input('Введите логин для регистрации\n')
        if register_login == '':
            print('Логин не может быть пустой строкой')
            continue
        elif register_login in data_base:
            check_account = input('Такой логин существует. Это ваш аккаунт? (Да/Нет)\n')
            if check_account.lower() == 'да':
                work_with_login = False
            elif check_account.lower() == 'нет':
                continue
            else:
                print('Ошибка, попробуйте еще раз')
                continue

        elif register_login not in data_base:
            while work_with_password is True:
                register_password = int(input('Введите пароль для регистрации\n'))
                if register_password == '':
                    print('Пароль не может быть пустым')
                    continue

                check_register_password = int(input('Введите пароль повторно\n'))
                if register_password == check_register_password:
                    print('Регистрация прошла успешно!\n')
                    data_base[register_login] = register_password
                    work_with_password = False
                    work_with_login = False
                else:
                    print('Пароли не совпадают')
                    continue

        else:
            print('Error')
            exit(0)

def sign_in():
    attempts = 0
    while True:
        if attempts == 3:
            print('Чтобы избежать взлома, мы заблокируем Ваш аккаунт. Обратитесь в поддержку, чтобы восстановить аккаунт.')
            exit(0)
        else:
            password = int(input('Введите пароль\n'))
            if data_base['login'] == password:
                print('Вы успешно вошли в систему\n')
                break
            else:
                print('Неправильный пароль')
                attempts = attempts + 1
def sign_jn():
    attempts = 0
    while True:
        if attempts == 3:
            print('Чтобы избежать взлома, мы заблокируем Ваш аккаунт. Обратитесь в поддержку, чтобы восстановить аккаунт.')
            exit(0)
        else:
            password = int(input('Введите пароль\n'))
            if data_base[login] == password:
                print('Вы успешно вошли в систему\n')
                break
            else:
                print('Неправильный пароль')
                attempts = attempts + 1
def sign_ul():
    work_with_login = True
    work_with_password = True
    while work_with_login is True:
        register_login = input('Введите логин для регистрации\n')
        if register_login == '':
            print('Логин не может быть пустой строкой')
            continue
        elif register_login in data_base:
            check_account = input('Такой логин существует. Это ваш аккаунт? (Да/Нет)\n')
            if check_account.lower() == 'да':
                work_with_login = False
            elif check_account.lower() == 'нет':
                continue
            else:
                print('Ошибка, попробуйте еще раз')
                continue

        elif register_login not in data_base:
            while work_with_password is True:
                register_password = int(input('Введите пароль для регистрации\n'))
                if register_password == '':
                    print('Пароль не может быть пустым')
                    continue

                check_register_password = int(input('Введите пароль повторно\n'))
                if register_password == check_register_password:
                    print('Регистрация прошла успешно!\n')
                    data_base[register_login] = register_password
                    work_with_password = False
                    work_with_login = False
                else:
                    print('Пароли не совпадают')
                    continue
def Kadzuha_menu():
    while True:
        a = int(input("Что хотите, 1- оружие 2- регион 3- стехия 4- история 5- артефакты"))
        if a == 1:
            print("Он одноручник, Лучшее для него оружие это 'Клятва свободы' или 'Меч Фавония' ")
        if a == 2:
            print("Он проживает в Инадзуме")
        if a == 3:
            print("Анемо")
        if a == 4:
            print("Перейдите по этой ссылке чтобы узнать его историю ")
        if a == 5:
            print("Лучшие артефакты для него это сэт 'Изумрудная тень' или сэт 'Инструктор' ")
        if a == 0:
            break

def Sao_menu():
    while True:
        a = int(input("Что хотите, 1- оружие 2- регион 3- стехия 4- история 5- артефакты"))
        if a == 1:
            print("Лучшее для него оружие это 'Нефритовый коршун' или 'Посох Хомы ")
        if a == 2:
            print("Он проживает в Ли Юэ ")
        if a == 3:
            print("Анемо")
        if a == 4:
            print("Перейдите по этой ссылке чтобы узнать его историю ")
        if a == 5:
            print("Лучшие артефакты для него это сэт 'Киноварное загробье' или 2 'Изумрудной тени' и 2 'Конец гладиатора'  ")
        if a == 0:
            break

def Ganu_menu():
    while True:
        a = int(input("Что хотите, 1- оружие 2- регион 3- стехия 4- история 5- артефакты"))
        if a == 1:
            print("Она  лучница, Лучшее для неё оружие это 'Охотничья тропа' или 'Лук амоса' ")
        if a == 2:
            print("Она проживает в Ли Юэ ")
        if a == 3:
            print("Крио")
        if a == 4:
            print("Перейдите по этой ссылке чтобы узнать его историю ")
        if a == 5:
            print("Лучшие артефакты для него это сэт 'Воспоминания Сименавы' или сэт 'Странствующий ансамбль' ")
        if a == 0:
            break

def Aola_menu():
    while True:
        a = int(input("Что хотите, 1- оружие 2- регион 3- стехия 4- история 5- артефакты"))
        if a == 1:
            print("Она двухручница, Лучшее для неё оружие это 'Песнь разбитых сосен' или 'Волчья погибель ")
        if a == 2:
            print("Она проживает в Мондштате  ")
        if a == 3:
            print("Крио")
        if a == 4:
            print("Перейдите по этой ссылке чтобы узнать его историю ")
        if a == 5:
            print("Лучшие артефакты для неё это сэт 'Бледного огня' или 2 'Бледного огня' и 2 'Рыцаря крови'  ")
        if a == 0:
            break

def Laila_menu():
    while True:
        a = int(input("Что хотите, 1- оружие 2- регион 3- стехия 4- история 5- артефакты"))
        if a == 1:
            print("Она одноручница, Лучшее для неё оружие это 'Драгоценный омут' или 'Рассекающий туман' ")
        if a == 2:
            print("Она проживает в Инадзуме")
        if a == 3:
            print("Крио")
        if a == 4:
            print("Перейдите по этой ссылке чтобы узнать его историю ")
        if a == 5:
            print("Лучшие артефакты для неё это сэт 'Эмблема рассечённой судьбы' или 2 'церемониальной древней знати' и 2 'заблудшей в метели'  ")
        if a == 0:
            break

def Shen_He_menu():
    while True:
        a = int(input("Что хотите, 1- оружие 2- регион 3- стехия 4- история 5- артефакты"))
        if a == 1:
            print("Она копейщица, лучшее для неё оружие это 'Усмиритель бед' или 'Сияющая жатва ")
        if a == 2:
            print("Она проживает в Ли Юэ ")
        if a == 3:
            print("Крио")
        if a == 4:
            print("Перейдите по этой ссылке чтобы узнать его историю ")
        if a == 5:
            print("Лучшие артефакты для неё это сэт 'Церемония древней знати' или 2 'Конец гладиатора' и 2 'Эмблема рассечённой судьбы'  ")
        if a == 0:
            break

def Hu_Tao_menu():
    while True:
        a = int(input("Что хотите, 1- оружие 2- регион 3- стехия 4- история 5- артефакты"))
        if a == 1:
            print("Она копейщица, лучшее для неё оружие это 'Посох Хомы' или 'Посох алых песков' ")
        if a == 2:
            print("Она проживает в Ли Юэ ")
        if a == 3:
            print("Пиро")
        if a == 4:
            print("Перейдите по этой ссылке чтобы узнать его историю ")
        if a == 5:
            print("Лучшие артефакты для неё это сэт 'Горящая алая ведьма' или сэт 'Воспоминания Симэнавы' ")
        if a == 0:
            break

def Banet_menu():
    while True:
        a = int(input("Что хотите, 1- оружие 2- регион 3- стехия 4- история 5- артефакты"))
        if a == 1:
            print("Он одноручник, Лучшее для него оружие это 'Рассекающий туман' или 'Меч сокола' ")
        if a == 2:
            print("Он проживает в Мондштате")
        if a == 3:
            print("Пиро")
        if a == 4:
            print("Перейдите по этой ссылке чтобы узнать его историю ")
        if a == 5:
            print("Лучшие артефакты для него это сэт 'Церемония древней знати' или сэт 'Эмблема рассечённой судьбы' ")
        if a == 0:
            break

def Djun_Li_menu():
    while True:
        a = int(input("Что хотите, 1- оружие 2- регион 3- стехия 4- история 5- артефакты"))
        if a == 1:
            print("Он копейщи, лучшее для не оружие это 'Чёрная кисть' или 'Копьё Фавония' ")
        if a == 2:
            print("Он проживает в Ли Юэ ")
        if a == 3:
            print("Гео")
        if a == 4:
            print("Перейдите по этой ссылке чтобы узнать его историю ")
        if a == 5:
            print("Лучшие артефакты для не это сэт 'Стойкости Миллелита' ")
        if a == 0:
            break

def Sin_Cu_menu():
    while True:
        a = int(input("Что хотите, 1- оружие 2- регион 3- стехия 4- история 5- артефакты"))
        if a == 1:
            print("Он одноручник, Лучшее для него оружие это 'Драгоценный омут' или 'Рассекающий туман ")
        if a == 2:
            print("Он проживает в Ли Юэ ")
        if a == 3:
            print("Гидро")
        if a == 4:
            print("Перейдите по этой ссылке чтобы узнать его историю ")
        if a == 5:
            print("Лучшие артефакты для него это сэт 'Эмблема Рассечённой судьбы' или 2 'Церемонии древней знати' и 2 'Сердца глубин' ")
        if a == 0:
            break
def Menu():
    while True:
        a = int(input("Кого бы вы хотели посмотреть, 1- Кадзуха, 2- Сяо, 3- Ганьюй, 4- Эола, 5- Лайла, 6- Шень Хэ, 7- Ху тао, 8- Бенет, 9- Джун Ли, 10- Синь Цу"))
        if a == 1:
            Kadzuha_menu()
        if a == 2:
            Sao_menu()
        if a == 3:
            Ganu_menu()
        if a == 4:
            Aola_menu()
        if a == 5:
            Laila_menu()
        if a == 6:
            Shen_He_menu()
        if a == 7:
            Hu_Tao_menu()
        if a == 8:
            Banet_menu()
        if a == 9:
            Djun_Li_menu()
        if a == 10:
            Sin_Cu_menu()
sign_up()
sign_in()
sign_jn()
sign_ul()
Menu()

