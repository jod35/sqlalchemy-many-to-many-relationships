from itertools import product
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    ForeignKey,
    column,
    create_engine,
    Column,
    Integer,
    String,
    Table

)
from sqlalchemy.orm import (
    relationship,
    sessionmaker
)


BASE_DIR=os.path.dirname(os.path.realpath(__file__))

connection_str='sqlite:///'+os.path.join(BASE_DIR,'site.sqlite3')

engine=create_engine(connection_str)

Base=declarative_base()

"""

table association:
    product_id: int fk(products.id)
    cutomer_id: int fk(customers.id)


class Customer:
    id : int pk
    name : str 


class Product:
    id : int pk
    name: str
    price : int
"""

association_table=Table(
    'association',
    Base.metadata,
    Column('customer_id',ForeignKey('customers.id')),
    Column('product_id',ForeignKey('products.id'))

)


class Customer(Base):
    __tablename__='customers'
    id=Column(Integer(),primary_key=True)
    name=Column(String(),nullable=False)
    products=relationship('Product',
        secondary=association_table,
        back_populates='customers'
    )

    def __repr__(self):
        return f"<Customer {self.name}>"

class Product(Base):
    __tablename__='products'
    id=Column(Integer(),primary_key=True)
    name=Column(String(),nullable=False)
    price=Column(Integer(),nullable=False)
    customers=relationship(
        'Customer',
        secondary=association_table,
        back_populates='products'
    )

    def __repr__(self):
        return f"<Product {self.name}>"


Base.metadata.create_all(engine)

session=sessionmaker()(bind=engine)



