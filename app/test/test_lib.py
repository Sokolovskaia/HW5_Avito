from app.lib import create_product, add_product, search_by_name, search_for_area, search_price


def test_create_product():
    assert {'name': 'Квартира', 'area': 'Советский', 'price': 1000} == create_product("Квартира", "Советский", 1000)


def test_add_product():
    assert [{'name': 'Квартира', 'area': 'Советский', 'price': 1000}] == add_product([], {'name': 'Квартира', 'area': 'Советский', 'price': 1000})



def test_search_by_name():
    assert [{'name': 'Квартира', 'area': 'Советский', 'price': 1000}] == search_by_name([{'name': 'Квартира', 'area': 'Советский', 'price': 1000}, {'name': 'Дача', 'area': 'Советский', 'price': 1000}], "Квартира")



def test_search_for_area():
    assert [{'name': 'Квартира', 'area': 'Приволжский', 'price': 1000}] == search_for_area([{'name': 'Квартира', 'area': 'Приволжский', 'price': 1000}, {'name': 'Квартира', 'area': 'Советский', 'price': 1000}], ["Приволжский"])


def test_search_for_area_all():
    assert [{'name': 'Квартира', 'area': 'Приволжский', 'price': 1000}, {'name': 'Квартира', 'area': 'Советский', 'price': 1000}] == search_for_area([{'name': 'Квартира', 'area': 'Приволжский', 'price': 1000}, {'name': 'Квартира', 'area': 'Советский', 'price': 1000}], [])


def test_search_price():
    assert [{'name': 'Квартира', 'area': 'Советский', 'price': 100}] == search_price([{'name': 'Квартира', 'area': 'Советский', 'price': 1000}, {'name': 'Квартира', 'area': 'Советский', 'price': 100}], 500)

