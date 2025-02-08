# Завдання 2

# Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7 заняття курсу Python
# Starter так, щоб він зберігав базу посилань на диску і не «забув» при перезапуску.
# За бажанням можете ознайомитися з модулем shelve (https://docs.python.org/3/library/shelve.html),
# який у даному випадку буде дуже зручним та спростить виконання завдання.

import shelve

menu = "1. Створити посилання\n2.Отримати посилання\n3.Вихід"
links =[]



while True:
    choise = input(f"Виберіть пункт меню:\n{menu}\n>: ")


    match choise:
        case '1':
            name = input("Введіть коротку назву для посилання (не більше 15 символів): ").strip()

            while len(name) > 15 or not name:
                print("Помилка! Назва повинна бути непустою та не перевищувати 15 символів.")
                name = input("Введіть коротку назву для посилання (не більше 15 символів): ").strip()

            text = input("Введіть посилання: ").strip()

            while not text:
                print("Помилка! Посилання не може бути порожнім.")
                text = input("Введіть посилання: ").strip()

            with shelve.open("links") as db:
                if name in db:
                    print("Помилка! Така назва вже існує. Спробуйте іншу.")
                else:
                    db[name] = text
                    print(f"\nДодано: {name} → {text}")

            with shelve.open("links") as db:
                print("\nЗбережені посилання:")
                for key in db:
                    print(f"{key}: {db[key]}")
                print("===========================================")

            # links.append({'name': name, 'text': text})

            # print("links: ", links)

            # for i in range(len(links)):
            #     print(f"\n{i + 1}. {links[i]['name']}: {links[i]['text']}")
            #     print("===========================================")
        case '2':
            # if len(links) == 0:
            #     print("У вас ще немає збережених посилань. Оберіть пункт меню 1 для створення нового.")
            #     continue

            with shelve.open("links") as db:
                if len(db) == 0:
                    print("У вас ще немає збережених посилань. Оберіть пункт меню 1 для створення нового.")
                    continue

            choise_name = input(f"Напишіть коротку назву для посилання: ").lower()


            if choise_name != '':
                with shelve.open("links") as db:
                    found_name = False
                    print("\nНеобхідне посилання:")
                    for key in db:
                        if key.lower() == choise_name:
                            print(f"\n{key}: {db[key]}\n")
                            found_name = True
                            break
                    if not found_name:
                        print(f'\nНевірна назва {choise_name}! Спробуйте ще раз.\n')

                # for i in range(len(links)):
                #     if links[i]['name'] == choise_name:
                #         print(links[i]['text'])
            else:
                print("Помилка! Ви не ввели назву для пошуку.")
                continue
        case '3':
            break
        case '':
            choise = input(f"Виберіть пункт меню:\n{menu}\n>: ")
