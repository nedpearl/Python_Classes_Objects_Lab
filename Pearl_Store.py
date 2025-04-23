class Items:
    menu_list = []
    
    # To create an item, it must be provided with a name, type, and price.
    def __init__(self, name, type, price, stocks = 10):
        self.name = name
        self.type = type
        self.price = price
        self.stocks = stocks
        Items.menu_list.append(self)

    def __repr__(self):
        return "{type}: {name} - P{price}".format(type = self.type, name = self.name, price = self.price)

    def menu():
        for item in Items.menu_list:
            print(item)
    
    #def purchase(self):
    
    #def restock(self):

    #def stats(self):


class Customers:
    # A customer has a list of items to purchase, a payment method, where they will take their order, and a name.
    def __init__(self, name, purchase_list, is_cashless = True, for_here = True):
        self.purchase = purchase_list
        self.payment = is_cashless
        self.location = for_here

    #def display_order(self):

    #def total_bill(self):

    #def payment(self):

#Sample Items
meal_one = Items('Pesto Pasta', 'meal', 150)
meal_two = Items('Cajun Shrimp', 'meal', 190)
pastry_one = Items('Croissant', 'pastry', 120)
pastry_two = Items('Ube Cheese Pandesal', 'pastry', 80)
drink_one = Items('Iced Latte', 'drink', 100)
drink_two = Items('Cucumber Lemon Iced Tea', 'drink', 90)

customer_one = input("Welcome to Pearl Store! Please enter your name and hit enter. ")

print("Hi, " + str(customer_one) + "! Here's our menu for today: ")
Items.menu()
will_order = input('Would you like to order ? (Yes/No) ')

if will_order == 'Yes' or will_order == 'yes':
    orders = []
    counter = 0
    order_qty = int(input('How many orders would you like to enter? '))
    while counter < order_qty:
        item_choice = input('Enter item to order: ')
        item_qty = input('Enter quantity for {item}: '.format(item = item_choice))
        order = [item_choice, item_choice]
        counter += 1
else:
    exit

print(orders)
#if choice == 'meal':
    #meal_choice = input("Would you like " + meal_one.name + " or " + meal_two.name + " ? ")
    #if meal_choice == meal_one.name:
        #meal_one_quantity = input("How many would you like to order? ")

