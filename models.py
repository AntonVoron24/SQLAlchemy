from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Publisher(Base):
    __tablename__ = "publisher"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=40), unique=True)

    def __repr__(self):
        return f'id:{self.id} ' \
               f'name:{self.name}'


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String(length=40), nullable=False)
    id_publisher = Column(Integer, ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="books")

    def __repr__(self):
        return f'id:{self.id} ' \
               f'title:{self.title} ' \
               f'id_publisher:{self.id_publisher}'


class Shop(Base):
    __tablename__ = "shop"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=40), unique=True)

    def __repr__(self):
        return f'id:{self.id} ' \
               f'Name_shop:{self.name}'


class Stock(Base):
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True)
    id_book = Column(Integer, ForeignKey("book.id"), nullable=False)
    id_shop = Column(Integer, ForeignKey("shop.id"), nullable=False)
    count = Column(Integer)

    book = relationship(Book, backref="stocks")
    shop = relationship(Shop, backref='shops')

    def __repr__(self):
        return f'id:{self.id} ' \
               f'id_book:{self.id_book} ' \
               f'id_shop:{self.id_shop} ' \
               f'count:{self.count}'


class Sale(Base):
    __tablename__ = "sale"
    id = Column(Integer, primary_key=True)
    price = Column(Numeric, nullable=False)
    date_sale = Column(DateTime)
    id_stock = Column(Integer, ForeignKey("stock.id"))
    count = Column(Integer)
    stock = relationship(Stock, backref="sales")

    def __repr__(self):
        return f'id:{self.id} ' \
               f'price:{self.prise} ' \
               f'data_sale:{self.date_sale} ' \
               f'id_stok:{self.id_stock} ' \
               f'count:{self.id_stock}'
