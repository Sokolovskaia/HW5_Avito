def create_product(name, area, price):
    return {
        'name': name,
        'area': area,
        'price': price
    }


def add_product(container, product):
    container.append(product)
    return container


def search_by_name(container, request):
    result = []
    request_lowercased = request.strip().lower()
    for product in container:
        if request_lowercased in product['name'].lower():
            result.append(product)
            continue
    return result


def search_for_area(container, request):
    result = []
    if len(request) != 0:
        for area_name in request:
            for product in container:
                if area_name in product['area']:
                    result.append(product)
                    continue
    else:
        result = container
    return result


def search_price(container, request):
    result = []
    for product in container:
        if product['price'] <= request:
            result.append(product)
            continue
    return result
