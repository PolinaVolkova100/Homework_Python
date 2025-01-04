from datetime import datetime, timezone, timedelta
import urllib3
import geocoder


def api_input():
    try:
        API = input("Введите ваш API: ")  # 21ca8be42e78fa52b24a520882faca6a
        url_data = f"https://api.openweathermap.org/data/2.5/weather?q=москва&appid={API}&lang=ru&units=metric"
        http = urllib3.PoolManager()
        resp = http.request("GET", url_data).json()  # словарь с данными
        if resp["cod"] == 401:
            raise ValueError
    except ValueError:
        print("Введен некорректный API")
        API = api_input()
    return API


API = api_input()

history = []  # история запросов - список списков


def select_action():
    while True:
        print("")
        print("1 - Показать погоду в выбранном городе")  # +
        print("2 - Показать погоду по местоположению")  # +
        print("3 - Показать историю запросов")  # +
        print("4 - Завершить работу")  # +
        number = input("Выберите действие: ")
        if number == "4":
            history.clear()
            print("Работа программы завершена")
            break
        elif number not in "123":
            print("Неверный запрос, повторите попытку")
        elif number == "1":
            show_chosen_city_weather()
        elif number == "2":
            show_my_city_weather()
        elif number == "3":
            show_history()


def get_data(city):
    url_data = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&lang=ru&units=metric"
    http = urllib3.PoolManager()
    resp = http.request("GET", url_data).json()  # словарь с данными
    if resp["cod"] == 200:
        req = ["" for _ in range(6)]  # список для добавления в список history
        dev_utc = timedelta(hours=resp["timezone"] / 3600)
        req[0] = datetime.fromtimestamp(resp["dt"], timezone(dev_utc))
        req[1] = resp["name"]
        req[2] = resp["weather"][0]["description"]
        req[3] = resp["main"]["temp"]
        req[4] = resp["main"]["feels_like"]
        req[5] = resp["wind"]["speed"]
        history.append(req)  # добавили список с данными запроса в историю
        show_result(req)
    elif resp["cod"] == "404":
        print("Такой город не найден")


def show_chosen_city_weather():  # 1 - Показать погоду в выбранном городе
    city = input("Введите название города: ")
    get_data(city)


def show_my_city_weather():  # 2 - Показать погоду по метоположению
    city = geocoder.ip("me")
    get_data(city.city)


def show_history():  # 3 - Показать историю запросов
    try:
        n = int(input("Введите количество запросов: "))
        i = 1
        if 0 < n < len(history) + 1:
            while n:
                show_result(history[-i])
                i += 1
                n -= 1
        else:
            raise IndexError
    except IndexError:
        print("Введено некорректное количество запросов")
    except ValueError:
        print("Количество запросов должно быть целым положительным числом")


def show_result(lst: list):  # вывод результатов
    print("")
    print(f"Текущее время: {lst[0]}")
    print(f"Название города: {lst[1]}")
    print(f"Погодные условия: {lst[2]}")
    print(f"Текущая температура: {round(lst[3])} градусов по цельсию")
    print(f"Ощущается как: {round(lst[4])} градусов по цельсию")
    print(f"Скорость ветра: {lst[5]} м/c")


select_action()
