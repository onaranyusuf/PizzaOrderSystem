import csv
import datetime

#Print PizzaOrderSystem text
print(""" 
  _____  _                    ____            _             
 |  __ \(_)                  / __ \          | |            
 | |__) |_  ____ ____ __ _  | |  | | _ __  __| |  ___  _ __ 
 |  ___/| ||_  /|_  // _` | | |  | || '__|/ _` | / _ \| '__|
 | |    | | / /  / /| (_| | | |__| || |  | (_| ||  __/| |   
 |_|   _|_|/___|/___|\__,_|  \____/ |_|   \__,_| \___||_|   
      / ____|            | |                                
     | (___   _   _  ___ | |_  ___  _ __ ___                
      \___ \ | | | |/ __|| __|/ _ \| '_ ` _ \               
      ____) || |_| |\__ \| |_|  __/| | | | | |              
     |_____/  \__, ||___/ \__|\___||_| |_| |_|              
               __/ |                                        
              |___/           
""")
#Print author name
print('\033[4;31m' + "Made by Yusuf Onaran" + '\033[0;0m\n')

#Creates a .txt file and writes the entries into it.
with open("menu.txt", "w") as f:
    f.write("* Please select a pizza:\n"
           " 1: KlasikPizza         79.99 ₺\n"
           " 2: MargaritaPizza      69.99 ₺\n"
           " 3: TurkPizza           99.99 ₺\n"
           " 4: SadePizza           89.99 ₺\n"
           " * and additional toppings:\n"
           " 11: Zeytin             5.45  ₺\n"
           " 12: Mantar             7.99  ₺\n"
           " 13: Keçi Peyniri       14.75 ₺\n"
           " 14: Et                 21.95 ₺\n"
           " 15: Soğan              4.50  ₺\n"
           " 16: Mısır              3.95  ₺\n"
           " * Thank you!"
           )
#Function to print the menu
def print_menu():
  with open("menu.txt", "r") as f:
    menu = f.read()
    print(menu)

#Creates a class. The class has three other methods (description, cost, contents).
class Pizza:
  def __init__(self, description, cost, contents):
    self._description = description
    self._cost = cost
    self._contents = contents
  def get_description(self):
    return self._description
  def get_cost(self):
    return self._cost
  def get_contents(self):
    return self._contents

#Creates the subclass. We determine the values in the superclass.
class KlasikPizza(Pizza):
  def __init__(self):
    super().__init__(
      "Klasik Pizza", 79.99,
      "Domates Sosu, Mozeralla Peyniri, Zeytin, Mantar, Sucuk, Sosis ")
class MargaritaPizza(Pizza):
  def __init__(self):
    super().__init__(
      "Margarita Pizza", 69.99,
      "Domates Sosu, Mozeralla Peyniri, Fesleğen ")
class TurkPizza(Pizza):
  def __init__(self):
    super().__init__(
      "Türk Pizza", 99.99,
      "Domates Sosu, Mozeralla Peyniri, Kıyma, Yeşil Biber, Domates, Soğan ")
class SadePizza(Pizza):
  def __init__(self):
    super().__init__(
      "Sade Pizza", 89.99,
      "Domates Sosu, Mozeralla Peyniri, Sucuk ")

#Creates the Decorator class. It is used to change or add pizza properties.
class Decorator(Pizza):
  def __init__(self, component):
    self.component = component
  def get_cost(self):
    return self.component.get_cost() + Pizza.get_cost(self)
  def get_description(self):
    return self.component.get_description() + ' ' + Pizza.get_description(self)

class Zeytin(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self._description = "Zeytin"
    self._cost = 5.45
class Mantar(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self._description = "Mantar"
    self._cost = 7.99
class KeciPeyniri(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self._description = "Keçi Peyniri"
    self._cost = 14.75
class Et(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self._description = "Et"
    self._cost = 21.95
class Sogan(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self._description = "Soğan"
    self._cost = 4.50
class Misir(Decorator):
  def __init__(self, pizza):
    super().__init__(pizza)
    self._description = "Mısır"
    self._cost = 3.95

#Main function.
def main():
  #Print menu
  print_menu()
  while True:
    try:
      pizza_type = int(input("\nPlease select a pizza: "))
      if pizza_type not in [1, 2, 3, 4]:
        raise ValueError
      break
    except ValueError:
      print("Invalid input, please try again.")

  if pizza_type == 1:
    pizza = KlasikPizza()
  elif pizza_type == 2:
    pizza = MargaritaPizza()
  elif pizza_type == 3:
    pizza = TurkPizza()
  elif pizza_type == 4:
    pizza = SadePizza()

  print("\nPizza type: ", pizza.get_description())
  print("Ingredients of Pizza: ", pizza.get_contents(), "\n")

  while True:
    try:
      optional_toppings = int(
        input(
          "\nPlease select optional toppings: \n(Press 0 to view and pay the total price!) "
        ))
      if optional_toppings == 0:
        break
      elif optional_toppings not in [11, 12, 13, 14, 15, 16]:
        raise ValueError
    except ValueError:
      print("Invalid input, please try again.")

    if optional_toppings == 11:
      pizza = Zeytin(pizza)
    elif optional_toppings == 12:
      pizza = Mantar(pizza)
    elif optional_toppings == 13:
      pizza = KeciPeyniri(pizza)
    elif optional_toppings == 14:
      pizza = Et(pizza)
    elif optional_toppings == 15:
      pizza = Sogan(pizza)
    elif optional_toppings == 16:
      pizza = Misir(pizza)

    print("\nOrder: ", pizza.get_description())
  print("\nTotal Price: ", pizza.get_cost(), "₺")

  #User information requested.
  name = input("\nName: ")
  ID_No = input("ID Number: ")
  card_num = input("Credit Card Number: ")
  card_pass = input("Card Password: ")

  #Giving order description and calculating total price.
  order = pizza.get_description()
  price = pizza.get_cost()
  price = round(price, 3)
  if isinstance(pizza, KlasikPizza):
    order = "Klasik Pizza"
    price = pizza.get_price()
  elif isinstance(pizza, MargaritaPizza):
    order = "Margarita Pizza"
    price = pizza.get_price()
  elif isinstance(pizza, TurkPizza):
    order = "Türk Pizza"
    price = pizza.get_price()
  elif isinstance(pizza, SadePizza):
    order = "Sade Pizza"
    price = pizza.get_price()

  #Order time.
  time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  #Adding order information to the Orders Database.csv file.
  with open("Orders_Database.csv", mode="a", newline="") as orders_file:
    fieldnames = [
      "name", "ID_No", "card_num", "card_pass", "order", "price",
      "time"
    ]
    writer = csv.DictWriter(orders_file, fieldnames=fieldnames)

    #Print headers if file is empty.
    if orders_file.tell() == 0:
      writer.writeheader()

    #Print order information to file.
    writer.writerow({
      "name": name,
      "ID_No": ID_No,
      "card_num": card_num,
      "card_pass": card_pass,
      "order": order,
      "price": price,
      "time": time
    })
  print("Your order has been received. Thank you!")

if __name__ == '__main__':
  main()
