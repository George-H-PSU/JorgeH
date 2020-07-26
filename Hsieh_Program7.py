#Hsieh_Program7
#Yuan-Chih Hsieh
#CMPSC132 Program7


class inventory_item:
    def __init__(self, upc, price, cost, quantity):
        self.upc = upc
        self.price = price
        self.cost = cost
        self.quantity = quantity

    #UPC getter
    def get_upc(self):
        return self.upc

    #price getter
    def get_price(self):
        return self.price

    #cost getter
    def get_cost(self):
        return self.cost

    #quantity getter
    def get_quantity(self):
        return self.quantity

    #UPC setter
    def set_upc(self, new):
        self.upc = new

    #price setter
    def set_price(self, new):
        self.price = new

    #cost setter
    def set_cost(self, new):
        self.cost = new

    #quantity setter
    def set_quantity(self, new):
        self.quantity = new

    #call this method when using print
    def __str__(self):
        return str(self.upc)+' / '+str(self.price)+' / '+str(self.cost)+' / '+str(self.quantity)


def main():
    store = {} #the dictionary that stores inventory_items
    choice = 0 #choice the user choose on the menu
    while choice != 5:
        print('Menu')
        print('------------------------------------')
        choice = int(input('1) Add\n2) Delete\n3) Modify\n4) Display\n5) Exit\n'))
        print('------------------------------------')
        
        if choice == 1: #add
            upc = input('Please enter UPC number: ')
            while upc in store.keys():  #check if the upc number is unique
                print('Invalid input')
                upc = input('Please enter UPC number: ')
            price = input('Please enter the price: ')
            cost = input('Please enter the cost: ')
            quantity = input('Please enter the quantity: ')
            store[upc] = inventory_item(upc, price, cost, quantity) #Since the upc number is unique, let it be the key in the dictionary
            print('Finished!')

        elif choice == 2: #delete
            kill = input('Please enter the upc number of the item you want to delete: ')
            while kill not in store.keys(): #check if the number is in the dictionary or not
                print('Invalid input')
                kill = input('Please enter the upc number of the item you want to delete: ')
            if kill in store.keys():
                del store[kill] #delete the inventory_item from the list
            print('Finished!')

        elif choice == 3: #modify
            modify = input('Please enter the upc number of the item you want to modify: ')
            while modify not in store.keys():
                print('Invalid input')
                modify = input('Please enter the upc number of the item you want to modify: ')
            item = store[modify]    #find the inventory_item that the user want to modify
            new_price = input('Please enter the price: ')
            new_cost = input('Please enter the cost: ')
            new_quantity = input('Please enter the quantity: ')
            #use the setter to modify the changes
            item.set_price(new_price)
            item.set_cost(new_cost)
            item.set_quantity(new_quantity)
            print('Finished!')

        elif choice == 4: #display
            print('UPC / Price / Cost / Quantity')
            for i in store: #print every inventory_item's attribute 
                print(store[i])

        elif choice == 5: #quit
            print('Thank you! Program closed.')

        else:
            print('Invalid input')

if __name__ == '__main__': main()