#ZyLabs 10.19 Jai Kapoor 1901832

class ItemToPurchase:
    def __init__(self):
        self._name = "none"
        self._price = 0
        self._quantity = 0
        self._description = "none"

    def item_name(self, name):
        self._name = name

    def item_price(self, price):
        self._price = price

    def item_quantity(self, quantity):
        self._quantity = quantity

    def item_description(self, description):
        self._description = description

    def print_item_description(self):
        print(self.item_name, ": ", self.item_description)

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(int(self.item_price)) + " = $" +
              str(int(self.item_price * self.item_quantity)))


class ShoppingCart:
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2016"
        self.cart_items = []

    def add_item(self, noo_item):
        self.cart_items.append(noo_item)
      

    def remove_item(self, unwanted_item):
        self.cart_items.remove(self)
        found = 0
        cart_directory = self.cart_items[:]
        for x in range(len(cart_directory)):
            item = cart_directory[x]
            if item._name == unwanted_item:
                del self.cart_items[x]
                found += 1

        if found == 0:
            print()
            print('Item not found in cart. Nothing removed.')


    def modify_item(self, itemtochange):
        if itemtochange.item_name not in self.cart_items:
            print('Item not found in cart. Nothing modified.')
        else:
            cart_directory = self.cart_items[:]
            for y in range(len(cart_directory)):
                item = cart_directory[y]
                if item.name == itemtochange.name:
                    mod = ItemToPurchase()
                    mod.name = item.name
                    mod.description = item.description
                    mod.price = item.price
                    mod.quantity = itemtochange.quantity
                    self.cart_items[y] = mod


    def get_num_items_in_cart(self):
        cart_count = 0
        for w in self.cart_items:
            cart_count += w.quantity
            return cart_count


    def get_cost_of_cart(self):
        cart_total = 0
        for z in self.cart_items:
            item_total = z.item_quantity * z.item_price
            cart_total += item_total
            return cart_total


    def print_total(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        count = len(self.cart_items)
        if count == 0:
            print()
            print('SHOPPING CART IS EMPTY')
            return 0

        print('Number of Items:' + count)
        print()

        for item in self.cart_items:
            item.print_item_cost()

        total = self.get_cost_of_cart()
        print('Total: $' + str(total))

        if object_total == 0:
            print("SHOPPING CART IS EMPTY")

    def print_descriptions(self):

        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print()
        print('Item Descriptions')
        for element in self.cart_items:
            print(element.item_name, ": ", element.item_description)

if __name__ == '__main__':

  def print_menu(ShoppingCart):
      print()
      print('MENU')
      print('a - Add item to cart')
      print('r - Remove item from cart')
      print('c - Change item quantity')
      print("i - Output items' descriptions")
      print('o - Output shopping cart')
      print('q - Quit')
      print()

  def main():
      cart = ShoppingCart()
      cart.customer_name = input("Enter customer's name:\n")
      cart.current_date = input("Enter today's date:\n")
      print()
      print("Customer name:", cart.customer_name)
      print("Today's date:", cart.current_date)

      menu_choice = ''

      print_menu(cart)
      while menu_choice != 'q':
          menu_choice = input('Choose an option:\n').lower()
          if menu_choice == 'o':
              cart.print_descriptions()
          elif menu_choice == 'a':
              print('ADD ITEM TO CART')
              new_name = input('Enter the item name: ')
              new_description = input('Enter the item description: ')
              new_price = int(input('Enter the item price: '))
              new_quantity = int(input('Enter the item quantity: '))
              print()
              noo_item = ItemToPurchase()
              noo_item.item_name(new_name)
              noo_item.item_description(new_description)
              noo_item.item_price(new_price)
              noo_item.item_quantity(new_quantity)
              cart.add_item(noo_item)
          elif menu_choice == 'r':
              print('REMOVE ITEM FROM CART')
              unwanted_item = input('Enter name of item to remove: ')
              cart.remove_item(unwanted_item)
          elif menu_choice == 'c':
              print('CHANGE ITEM QUANTITY')
              itemtochange = ItemToPurchase(input('Enter the item name: '))
              itemtochange.item_quantity(int(input('Enter the new quantity: ')))
              cart.modify_item(itemtochange)
main()
