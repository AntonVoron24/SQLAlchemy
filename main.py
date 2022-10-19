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


def get_publisher():
    search = input('Введите имя или идентификатор издателя --> ')

    if search.isnumeric():
        for result in session.query(Publisher).filter(Publisher.id == int(search)).all():
            print(result)
    else:
        for result in session.query(Publisher).filter(Publisher.name.like(f'%{search}%')).all():
            print(result)


get_publisher()
