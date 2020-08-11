#Hsieh_Program9
#Yuan-Chih Hsieh
#CMPSC132 Program9

import matplotlib.pyplot as plt


class sales:
    def __init__(self, dollars, date):
        self.dollars = dollars
        self.date = date

    #dollars getter
    def get_dollars(self):
        return self.dollars

    #data getter
    def get_date(self):
        return self.date

    #dollars setter
    def set_dollars(self, new):
        self.dollars = new

    

def menu():
    choice = ''
    #use hash table to store the data
    table = dict()
    while choice != '6':    #quit if choice equals 6
        print('----------')
        print('Menu')
        print('----------')
        print('1) Add\n2) View\n3) Delete\n4) Modify\n5) Plot\n6) Quit')
        print('----------')
        choice = input('Enter your choice: ')

        #Add
        if choice == '1':
            try:
                dollars = float(input('Please enter the amount of dollars: '))
                date = int(input('Enter the date(MMDD): '))
                table[date] = sales(dollars, date)      #use the date as the key for dictionary
            except ValueError:
                print('Invalid input')

        #View
        elif choice == '2':     
            for _ in table:     #goes through all the elements in the dictionary
                print('Dollars: {}     Date: {}'.format(table[_].get_dollars(), table[_].get_date()))

        #Delete
        elif choice == '3':
            try:
                key = int(input('Enter the date of data you want to delete: '))
                while key not in table.keys():      #if the user enter a key value that is not a dictionary key
                    print('Invalid input')
                    key = int(input('Enter the date of data you want to delete: '))
                del table[key]      #find the data and delete by using the dictionary key
            except ValueError:
                print('Invalid input')
   
        #Modify
        elif choice =='4':      
            try:
                key = int(input('Enter the date of data you want to modify: '))
                while key not in table.keys():      #if the user enter a key value that is not a dictionary key
                    print('Invalid input')
                    key = int(input('Enter the date of data you want to delete: '))
                dollars = float(input('Please enter the amount of dollars: '))
                table[key].set_dollars(dollars)     #use the dollars setter
            except ValueError:
                print('Invalid input') 
   
        #Plot
        elif choice =='5':
            xaxis = sorted(table.keys())            #sort the date in a list
            yaxis = []
            for i in xaxis:
                yaxis.append(table[i].get_dollars())    #match the date to the dollars
            plt.plot(xaxis, yaxis, 'ro-', linewidth=5, markersize=5, alpha=0.35)
            plt.title('Sales')
            plt.xlabel('Date (MMDD)')
            plt.ylabel('Amount of Dollars')
            plt.show()
  
        #Quit
        elif choice == '6':
            print('Thank you!')
 
        else:
            print('Invalid input')
    return 

if __name__ == '__main__': menu()