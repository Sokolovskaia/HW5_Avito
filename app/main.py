def create_product(name, area, price):
    return {
        'name': name,
        'area': area,
        'price': price
    }


def add_product(container, product):
    container.append(product)
    return container


products = []

product_1 = create_product("Квартира", "Советский", 1000)
product_2 = create_product("Квартира", "Советский", 500)
product_3 = create_product("Дача", "Авиастроительный", 100)
product_4 = create_product("Квартира", "Приволжский", 500)

add_product(products, product_1)
add_product(products, product_2)
add_product(products, product_3)
add_product(products, product_4)

print("Введите название товара/услуги: ")
request_name = input()


def search_name(container, request):
    result = []
    request_lowercased = request.strip().lower()
    for product in container:
        if request_lowercased in product['name'].lower():
            result.append(product)
            continue
    return result


result_request_name = search_name(products, request_name)

if len(result_request_name) > 0:
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


    def search_for_area(container, request):
        result = []
        if len(request) != 0:
            for area_name in request:
                for product in container:
                    if area_name in product['area']:
                        result.append(product)
                        continue
        else:
            result = result_request_name
        return result


    result_request_area = search_for_area(result_request_name, areas)

    if len(result_request_area) > 0:
        print("Введите максимальную цену: ")
        request_price = int(input())


        def search_price(container, request):
            result = []
            for product in container:
                if product['price'] <= request:
                    result.append(product)
                    continue
            return result


        result_request_price = search_price(result_request_area, request_price)

        if len(result_request_price) > 0:
            for product in range(len(result_request_price)):
                print(result_request_price[product])

        else:
            print("Товар в указанном ценовом диапазоне не найден")
    else:
        print("Товар в указанных районах не найден")

else:
    print("Товар не найден")
