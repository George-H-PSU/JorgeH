#Hsieh_Program3
#Yuan-Chih Hsieh
#CMPSC132 Program3

class PersonData:
    def __init__(self, lastName, firstName, address, city, state, zipp, phone):
        self.lastName = lastName
        self.firstName = firstName
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipp
        self.phone = phone
    
    def get_lastname(self): #lastName accessor
        return self.lastName
    
    def get_firstname(self): #firstName accessor
        return self.firstName
    
    def get_address(self): #address accessor
        return self.address

    def get_city(self): #city accessor
        return self.city

    def get_state(self): #state accessor
        return self.state

    def get_zip(self): #zip address
        return self.zip

    def get_phone(self): #phone accessor
        return self.phone
    
    def set_lastname(self, new_last): #lastname mutator
        self.lastName = new_last

    def set_firstname(self, new_first): #firstname mutator
        self.firstName = new_first
    
    def set_address(self, new_address): #address mutator
        self.address = new_address

    def set_city(self, new_city): #city mutator
        self.city = new_city

    def set_state(self, new_state): #state mutator
        self.state = new_state

    def set_zip(self, new_zip): #zip mutator
        self.zip = new_zip

    def set_phone(self, new_phone): #phone mutator
        self.phone = new_phone


lst = list() #list for customer numbers

class CustomerData(PersonData):
    def __init__(self, lastName, firstName, address, city, state, zipp, phone, customerNumber, mailingList):
        global lst
        super().__init__(lastName, firstName, address, city, state, zipp, phone)
        while customerNumber in lst: #check if this number is an unique one
            try:
                customerNumber = int(input('Please enter another number: '))
            except ValueError:
                print('Invalid input')
        lst.append(customerNumber)
        self.customerNumber = customerNumber
        self.mailingList = bool(mailingList)         
            
    def get_customerNumber(self): #customerNumber accessor
        return self.customerNumber

    def get_mailingList(self): #mailingList accessor
        return self.mailingList
    
    def set_customerNumber(self, new_number): #customerNumber mutator
        global lst
        lst.remove(self.customerNumber)
        while new_number in lst: #check if the new number is an unique one
            try:
                new_number = int(input('Please enter another number: '))
            except ValueError:
                print('Invalid input')
        lst.append(new_number)
        self.customerNumber = int(new_number)

    def set_mailingList(self, new_mail): #mailingList mutator
        try:
            self.mailingList = bool(new_mail) 
        except ValueError: #error if the imput isnt a true/false
            print('Invalid input')

def main():
    last = input('Enter lastname: ')
    first = input('Enter firstname: ')
    address = input('Enter address: ')
    city = input('Enter city: ')
    state = input('Enter state: ')
    zipp = input('Enter zip code: ')
    phone = input('Enter phone number: ')
    number = ''
    while number == '':
        try:
            number = int(input('Enter a customer number: '))            
        except ValueError:
            print('Invalid input')          
    mail = ''
    while mail == '':
        try:
            mail = bool(input('Mailing List? (True/False) : '))
        except ValueError:
            print('Invalid input')
    sample = CustomerData(last, first, address, city, state, zipp, phone, number, mail)
    print('First name:', sample.get_firstname())
    print('Last name:', sample.get_lastname())
    print('Address:', sample.get_address())
    print('City:', sample.get_city())
    print('State:', sample.get_state())
    print('Zip:', sample.get_zip())
    print('Phone:', sample.get_phone())
    print('Customer number:', sample.get_customerNumber())
    print('Mailing list:', sample.get_mailingList())


if __name__ == '__main__': main()