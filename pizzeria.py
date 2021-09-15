import random

def main():
    pizzeria=Pizzeria()
    menu=pizzeria.get_menu()

    # test: add some orders to pizzeria
    nr_orders=2
    for o in range(nr_orders):
        pizzeria.add_new_order(create_order(menu))

    # test: prepare next order in the queue
    order=pizzeria.prepare_next_order()
    print(order)
    print(pizzeria.turnover)

def create_order(menu):
    nr_pizzas=3
    nr_toppings=2
    order=Order()
    for p in range(nr_pizzas):
        pizza=Pizza(random.sample(menu.get_pizza_bases(),1)[0])
        for i in range(nr_toppings):
            pizza.add_topping(random.sample(menu.get_toppings(),1)[0])
        order.add_pizza(pizza)
    return order

class Pizzeria:
    """ Pizzeria has a menu with what can be ordered and an order queue for pizza orders """

    def __init__(self):
        """ sets up the menu """
        self.turnover=0
        self._menu=Menu()
        self._menu.add_pizza_base(Pizza_Base("medium",7))
        self._menu.add_pizza_base(Pizza_Base("large",10))
        self._menu.add_topping(Topping("cheese",1))
        self._menu.add_topping(Topping("ham",1.5))
        self._menu.add_topping(Topping("salami",1.5))
        self._order_queue=Order_Queue()

    def __repr__(self):
        return f"Pizzeria(turnover:{self.turnover} _menu:{self._menu} _order_queue:{self._order_queue})"

    def get_menu(self):
        """ returns the menu """
        return self._menu

    def add_new_order(self,order):
        """ add new order to the back of the order queue """
        self._order_queue.add_to_back(order)

    def prepare_next_order(self):
        """ removes first order in the queue and returns it, it adds its cost to the turnover """
        order=self._order_queue.remove_from_front()
        self.turnover += order.get_total_cost()
        return order

class Menu:
    """ Holds the menu, different pizza bases and toppings that can be added on top """

    def __init__(self):
        self._pizza_bases=[]
        self._toppings=[]
    
    def __repr__(self):
        return f"Menu(_pizza_bases:{self._pizza_bases} _toppings:{self._toppings})"

    def add_pizza_base(self, pizza_base):
        """ adds a new pizza_base option to the menu """
        self._pizza_bases.append(pizza_base)

    def get_pizza_bases(self):
        """ returns all pizza_base options on the menu """
        return self._pizza_bases

    def add_topping(self, topping):
        """ adds a new topping option to the menu """
        self._toppings.append(topping)

    def get_toppings(self):
        """ returns all topping options on the menu """
        return self._toppings

class Pizza_Base:
    """ Pizza base with description of the size and cost """

    def __init__(self, size, cost):
        self.size=size
        self.cost=cost

    def __repr__(self):
        return f"Pizza_Base(size:{self.size} cost:{self.cost})"

class Topping:
    """ Pizza topping with a name and cost """

    def __init__(self, name, cost):
        self.name=name
        self.cost=cost

    def __repr__(self):
        return f"Topping(name:{self.name} cost:{self.cost})"

class Order_Queue:
    """ Order queue where orders get added to the back and removed from the front """

    def __init__(self):
        self.orders=[]

    def __repr__(self):
        return f"Order_Queue(orders:{self.orders})"

    def add_to_back(self, order):
        """ add order to the back of the queue """
        self.orders.append(order)

    def remove_from_front(self):
        """ removes order from the front of the queue and returns it """
        if len(self.orders)>0:
            return self.orders.pop(0)
        else:
            return None

class Order:
    """ An order can have multiple pizzas each with a pizza base and optional toppings """

    def __init__(self):
        self._pizzas=[]

    def __repr__(self):
        return f"Order(_pizzas:{self._pizzas})"

    def add_pizza(self, pizza):
        """ add pizza to the order """
        self._pizzas.append(pizza)

    def get_pizzas(self):
        """ returns a list of all pizzas in the order """
        return self.self._pizzas

    def get_total_cost(self):
        """ get total cost of all pizzas and toppings """
        cost=0
        for pizza in self._pizzas:
            cost+=pizza.get_total_cost()
        return cost

class Pizza:
    """ A pizza has a pizza base and optional toppings """
    
    def __init__(self, pizza_base):
        """ initialize a pizza with a pizza base """
        self.pizza_base=pizza_base
        self.toppings=[]

    def __repr__(self):
        return f"Pizza(pizza_base:{self.pizza_base} toppings:{self.toppings})\n"

    def add_topping(self, topping):
        """ add topping to the pizza """
        self.toppings.append(topping)

    def get_total_cost(self):
        """ get total cost of pizza base and all toppings """
        cost=self.pizza_base.cost
        for topping in self.toppings:
            cost+=topping.cost
        return cost

main()