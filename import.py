import csv
import os

from django.db import models, connection

from orders.models import Pizza
from .models import Orders, Pizza

# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("pizza.csv")
    reader = csv.reader(f)
    for pizza_name, category, small, large, ToppingCost in reader:
        # db.execute("INSERT INTO orders_pizza (pizza_name, category, small, large, ToppingCost) VALUES (:pizza_name, :category, :small, :large, :ToppingCost)", {"pizza_name": pizza_name, "category": category, "small": small, "large": large, "ToppingCost": ToppingCost})
        query = ("INSERT INTO orders_pizza (pizza_name, category, small, large, ToppingCost) VALUES (:pizza_name, :category, :small, :large, :ToppingCost)", {"pizza_name": pizza_name, "category": category, "small": small, "large": large, "ToppingCost": ToppingCost})
        Pizza.objects.raw(query)
        print(f"Added pizza {pizza_name}  {category}")
    #db.commit()

if __name__ == "__main__":
    main()
