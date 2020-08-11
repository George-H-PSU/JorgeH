#Hsieh_Program2
#Yuan-Chih Hsieh
#CMPSC132 Program2

class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class ProductionWorker(Employee): #inheritance from Employee class
    def __init__(self, name, number, shift, pay):
        Employee.__init__(self, name, number)
        self.shift = int(shift) #shift number
        self.pay = float(pay) #Hourly pay rate

def main():
    sample = ProductionWorker(input('Name: '), input('Number: '), input('Shift number: '), input('Pay: '))
    choice = input('Select Name(na), Number(nu), Shift number(s), Pay rate(p), Quit(q): ')
    while choice != 'q':
        if choice == 'na':  #when the user accesses name
            print(sample.name)
        elif choice == 'nu': #when the user accesses number
            print(sample.number)
        elif choice == 's': #when the user accesses shift number
            print(sample.shift)
        elif choice == 'p': #when the user accesses pay rate
            print(sample.pay)
        elif choice == 'q': #when the user wants to quit
            break
        else:
            print('Invalid input')
        
        choice = input('Select Name(na), Number(nu), Shift number(s), Pay rate(p), Quit(q): ')
    print('Program Ended')
    
if __name__ == '__main__': main()