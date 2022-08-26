import json
from json.decoder import JSONDecodeError
from time import strftime
from settings import DB
from datetime import datetime


def create_data():
    id_ = datetime.now().strftime('%H%M%S')
    data = {
        'id': id_,
        'title': input('Введите название товара: '),
        'price': int(input('Введите цену товара: ')),
        'date_created': datetime.now().strftime('%d.%m.%y. %H:%M'),
        'date_updated': 'Еще не обновлен',
        'description': input('Введите описание товара: '),
        'status': input('Введите статус товара: ')
    }
    json_data: list = get_all_data()
    json_data.append(data)
    with open(DB, 'w') as f:
        json.dump(json_data, f, indent=4)


def get_all_data():
    with open(DB) as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return []


def get_data_by_id():
    id_ = input('Введите id: ')
    for obj in get_all_data():
        if obj['id'] == id_:
            return obj
    return 'Not found'


def update():
    id_ = input('Введите id: ')
    data = get_all_data()
    for obj in data:
        if obj['id'] == id_:
            obj['title'] = input('Введите новое название: ') or obj['title']
            try:
                obj['price'] = int(input('Введите новую цену: ')) or obj['price']
            except:
                obj['price']
            obj['date_updated'] = datetime.now().strftime('%d.%m.%y %H:%M') or obj['date_updated']
            obj['description'] = input('Введите новое описание: ') or obj['description']
            break
    with open(DB, 'w') as f:
        json.dump(data, f, indent=4)


def delete_data():
    id_ = input('Введите id: ')
    data = get_all_data()
    for obj in data:
        if obj['id'] == id_:
            data.remove(obj)
            break
    with open(DB, 'w') as f:
        json.dump(data, f, indent=4)


def clear():
    with open(DB, 'w') as f:
        f.write('')


def info():
    print(' ')
    while True:
        print("""
    Введите операцию, которую хотите совершить:
    1. create - создать новый продукт
    2. delete - удалить продукт по id 
    3. list - получить сипсок всех продуктов
    4. retrieve - получить продукт по id
    5. clear - очистить базу данных
    6. update - изменить данные
    7. exit - выйти из программы
    """)
        inp = input('Введите операцию: ')
        if inp == 'create':
            inp = create_data()
        if inp == 'delete':
            inp = delete_data()
        if inp == 'list':
            inp = print(get_all_data())
        if inp == 'retrieve':
            inp = print(get_data_by_id())
        if inp == 'clear':
            inp = clear()
        if inp == 'update':
            inp = update()
        if inp == 'exit':
            print('Операция завершена!')
            break
    

""" Фильтрация по цене(дороже) """      
def filter_price_expensive():
    price = int(input('Введите цену: '))
    data = get_all_data()
    for obj in data:
        if price < obj['price']:
            print(obj)

""" Фильтрация по цене(дешевле) """        
def filter_price_cheaper():
    price = int(input('Введите цену: '))
    data = get_all_data()
    for obj in data:
        if price > obj['price']:
            print(obj)

""" Фильтрация по статусу(продан) """
def filter_status_sold():
    with open(DB) as f:
        python_obj = json.load(f)
        for obj in python_obj:
            if obj['status'] == 'продан':
                print(obj)


""" Фильтрация по статусу(продается) """
def filter_status__for_sale():
    with open(DB) as f:
        python_obj = json.load(f)
        for obj in python_obj:
            if obj['status'] == 'продается':
                print(obj)

""" EXTRA """

""" Фильтрация по дате создания """
def filter_data_created():
    time = input('Введите время: ')
    data = get_all_data()
    for obj in data:
        if time == obj['date_created']:
            print(obj)



""" Пагинация """
def pagination():
    count = int(input('Введите количество товаров: '))
    data = get_all_data()
    c = 0
    for i in data:
        if c < count:
            print(i)
        c +=1

