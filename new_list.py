class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self):
        name = input("What would you like to add? ")
        number = int(input("How many? "))
        price = input("price? ")

        new_item = Item(name, number, price)
        self.items.append(new_item)

    def remove_item(self):
        remove_item = input('Which item would you like to remove? ')
        remove_number= input('How many? ')
        for i in range(len(self.items)):
            if self.items[i].name.lower() == remove_item.lower():
                if remove_number.isdigit():
                    remove_number = int(remove_number)
                    self.items[i].number -= remove_number
                    print(f'{remove_number} {remove_item} were removed.')
                    if self.items[i].number < 1:
                        self.items.pop(i)
                        print(f'{remove_item} was removed')
                        break
                    else:
                        break
                print('Please enter number in digits')
            else:
                print(f'{remove_item} not found')

    
    def view_items(self):
        for item in self.items:
            print(f'{item.number} {item.name} at ${item.price}')

    def run(self):
        while True:
           while True:
            user_choice = input("What would you like to do? (add/remove/view/quit)").lower()
            
            if user_choice == 'add':
                self.add_items()
            elif user_choice == 'remove':
                self.remove_item()
            elif user_choice == 'view':
                self.view_items()
            elif user_choice == 'quit':
                self.view_items()
                return
            else:
                print('input unsupported, please try again') 



class Item:
    def __init__(self, name, number, price):
        self.name = name
        self.number = number
        self.price = price

shop = ShoppingCart()

shop.run()