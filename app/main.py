from app.lib import create_product, add_product, search_by_name, search_for_area, search_price

products = []

flat_1 = create_product("Квартира", "Советский", 1000)
flat_2 = create_product("Квартира", "Советский", 500)
dacha_1 = create_product("Дача", "Авиастроительный", 100)
flat_3 = create_product("Квартира", "Приволжский", 500)

add_product(products, flat_1)
add_product(products, flat_2)
add_product(products, dacha_1)
add_product(products, flat_3)

print("Введите название товара/услуги: ")
request_name = input()

result_request_name = search_by_name(products, request_name)

if len(result_request_name) == 0:
    print("Товар не найден")
else:
    areas = []
    request_area = -1
    while request_area not in (0, 6):
        print("Выберите район поиска(введите цифру):\n"
              "(1) Авиастроительный \n"
              "(2) Ново-Савиновский\n"
              "(3) Приволжский\n"
              "(4) Вахитовский\n"
              "(5) Советский\n"
              "(6) Искать во всех районах\n"
              "(0) Завершить выбор районов\n")

        request_area = int(input())

        if request_area == 1:
            area = "Авиастроительный"
            areas.append(area)
        elif request_area == 2:
            area = "Ново-Савиновский"
            areas.append(area)
        elif request_area == 3:
            area = "Приволжский"
            areas.append(area)
        elif request_area == 4:
            area = "Вахитовский"
            areas.append(area)
        elif request_area == 5:
            area = "Советский"
            areas.append(area)
        elif request_area == 6:
            areas = []

    result_request_area = search_for_area(result_request_name, areas)

    if len(result_request_area) > 0:
        print("Введите максимальную цену: ")
        request_price = int(input())

        result_request_price = search_price(result_request_area, request_price)

        if len(result_request_price) > 0:
            print(result_request_price)

        else:
            print("Товар в указанном ценовом диапазоне не найден")

    else:
        print("Товар в указанных районах не найден")
