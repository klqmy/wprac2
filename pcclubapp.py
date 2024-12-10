from datetime import datetime

users = [
    {
        'username': 'admin',
        'password': 'zxc',
        'role': 'admin',
        'created_at': '2024-12-10'
    },
    {
        'username': 'user1',
        'password': 'qwe',
        'role': 'user',
        'subscription_type': 'Standard',
        'history': [],
        'created_at': '2024-12-01'
    }
]

services = [
    {'name': 'Игровая зона (1 час)', 'price': 200, 'added_date': '2024-12-05'},
    {'name': 'ВИП-комната (1 час)', 'price': 500, 'added_date': '2024-12-07'},
    {'name': 'Напитки', 'price': 50, 'added_date': '2024-12-03'}
]

def main():
    def login():
        print("\nДобро пожаловать в компьютерный клуб!")
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        for user in users:
            if user['username'] == username and user['password'] == password:
                return user
        print("Неверное имя пользователя или пароль.")
        return None

    def user_menu(user):
        while True:
            print("\nПользовательское меню:")
            print("1. Просмотреть доступные услуги")
            print("2. Купить услугу")
            print("3. Просмотреть историю покупок")
            print("4. Сортировать услуги")
            print("5. Обновить профиль")
            print("6. Выйти")

            choice = input("Введите номер действия: ")
            if choice == '1':
                view_services()
            elif choice == '2':
                buy_service(user)
            elif choice == '3':
                view_history(user)
            elif choice == '4':
                sort_services(user)  # Передаем пользователя для сортировки
            elif choice == '5':
                update_profile(user)
            elif choice == '6':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def admin_menu(user):
        while True:
            print("\nАдминистраторское меню:")
            print("1. Управлять услугами")
            print("2. Управлять пользователями")
            print("3. Просмотреть статистику")
            print("4. Выйти")

            choice = input("Введите номер действия: ")
            if choice == '1':
                manage_services()
            elif choice == '2':
                manage_users()
            elif choice == '3':
                view_statistics()
            elif choice == '4':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def view_services():
        print("\nДоступные услуги:")
        for idx, service in enumerate(services, start=1):
            print(f"{idx}. {service['name']} - {service['price']} руб.")

    def buy_service(user):
        view_services()
        try:
            choice = int(input("Введите номер услуги для покупки: ")) - 1
            if 0 <= choice < len(services):
                selected_service = services[choice]
                current_date = datetime.now().strftime('%Y-%m-%d')  # Получение текущей даты
                user['history'].append({'name': selected_service['name'], 'price': selected_service['price'], 'date': current_date})
                print(f"Услуга '{selected_service['name']}' добавлена в вашу историю покупок.")
            else:
                print("Неверный выбор номера услуги.")
        except ValueError:
            print("Пожалуйста, введите корректный номер.")

    def view_history(user):
        print("\nВаша история покупок:")
        if user['history']:
            for idx, item in enumerate(user['history'], start=1):
                print(f"{idx}. {item['name']} - {item['price']} руб. (Дата покупки: {item['date']})")
        else:
            print("История пуста.")

    def sort_services(user):
        print("\n1. Сортировать по цене")
        print("2. Сортировать по дате добавления")

        choice = input("Выберите действие: ")
        if choice == '1':
            sorted_services = sorted(services, key=lambda x: x['price'])
        elif choice == '2':
            sorted_services = sorted(services, key=lambda x: x['added_date'])
        else:
            print("Неверный выбор.")
            return

        print("\nОтсортированные услуги:")
        for service in sorted_services:
            # Проверка, была ли куплена услуга
            purchase_date = None
            for item in user['history']:
                if item['name'] == service['name']:
                    purchase_date = item['date']
                    break
            
            if purchase_date:
                print(f"{service['name']} - {service['price']} руб. (Дата добавления: {service['added_date']}, Дата покупки: {purchase_date})")
            else:
                print(f"{service['name']} - {service['price']} руб. (Дата добавления: {service['added_date']})")

    def update_profile(user):
        print("\nОбновление профиля:")
        new_password = input("Введите новый пароль: ")
        user['password'] = new_password
        print("Пароль успешно обновлен.")

    def manage_services():
        print("\n1. Добавить услугу")
        print("2. Удалить услугу")
        print("3. Изменить услугу")

        choice = input("Выберите действие: ")
        if choice == '1':
            name = input("Введите название услуги: ")
            price = int(input("Введите цену услуги: "))
            added_date = input("Введите дату добавления (ГГГГ-ММ-ДД): ")
            services.append({'name': name, 'price': price, 'added_date': added_date})
            print("Услуга добавлена.")
        elif choice == '2':
            view_services()
            try:
                service_index = int(input("Введите номер услуги для удаления: ")) - 1
                if 0 <= service_index < len(services):
                    deleted_service = services.pop(service_index)
                    print(f"Услуга '{deleted_service['name']}' удалена.")
                else:
                    print("Неверный номер услуги.")
            except ValueError:
                print("Пожалуйста, введите корректный номер.")
        elif choice == '3':
            view_services()
            try:
                service_index = int(input("Введите номер услуги для изменения: ")) - 1
                if 0 <= service_index < len(services):
                    service = services[service_index]
                    service['price'] = int(input("Введите новую цену: "))
                    print("Услуга обновлена.")
                else:
                    print("Неверный номер услуги.")
            except ValueError:
                print("Пожалуйста, введите корректный номер.")
        else:
            print("Неверный выбор.")

    def manage_users():
        global users
        print("\n1. Добавить пользователя")
        print("2. Удалить пользователя")
        print("3. Изменить данные пользователя")

        choice = input("Выберите действие: ")
        if choice == '1':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            role = input("Введите роль (user/admin): ")
            created_at = input("Введите дату создания (ГГГГ-ММ-ДД): ")
            users.append({'username': username, 'password': password, 'role': role, 'created_at': created_at})
            print("Пользователь добавлен.")
        elif choice == '2':
            username = input("Введите имя пользователя для удаления: ")
            users[:] = [u for u in users if u['username'] != username]
            print("Пользователь удален.")
        elif choice == '3':
            username = input("Введите имя пользователя для изменения: ")
            for user in users:
                if user['username'] == username:
                    user['password'] = input("Введите новый пароль: ")
                    print("Данные пользователя обновлены.")
                    return
            print("Пользователь не найден.")
        else:
            print("Неверный выбор.")

    def view_statistics():
        print("\nСтатистика:")
        print(f"Всего пользователей: {len(users)}")
        print(f"Всего услуг: {len(services)}")

    # Основной цикл приложения
    while True:
        user = login()
        if user:
            if user['role'] == 'user':
                user_menu(user)
            elif user['role'] == 'admin':
                admin_menu(user)

if __name__ == "__main__":
    main()
