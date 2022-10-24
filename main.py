import json
from models import *
from database import *


session = Session()
create_db()


with open('tests_data.json', encoding='utf-8') as f:
    for data in json.load(f):
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[data.get('model')]
        session.add(model(id=data.get('pk'), **data.get('fields')))
        session.commit()
        session.close()


def get_shops():
    search = input('Введите имя или идентификатор издателя --> ')
    shops = session.query(Shop).join(Stock.shop).join(Book).join(Publisher)
    if search.isnumeric():
        for result in shops.filter(Publisher.id == search).all():
            print(result)
    else:
        for result in shops.filter(Publisher.name.like(f'%{search}%')).all():
            print(result)


get_shops()
