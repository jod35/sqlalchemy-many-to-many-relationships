from main import session,Product,Customer

# customer=Customer(name="customer 1")
# customer2=Customer(name="customer 2")
# customer3=Customer(name="customer 3")

customer=session.query(Customer).filter(Customer.id==1).first()
customer2=session.query(Customer).filter(Customer.id==1).first()


product=Product(name="Chicken",price=2000)
product2=Product(name="Bread",price=1000)
product3=Product(name="Milk",price=500)

customer2.products.append(
    product2
)
customer2.products.append(
    product3
)

session.commit()


print(customer.products)



# session.add_all(
#     [customer,customer2,customer3]
# )
# session.commit()