#Hsieh_Program6
#Yuan-Chih Hsieh
#CMPSC132 Program6

class inventory:
    def __init__(self, serialNum=None, manufactDate=None, lotNum=None):
        self.serialNum = serialNum
        self.manufactDate = manufactDate
        self.lotNum = lotNum
        self.next = None

    def get_serialNum(self):
        return self.serialNum

    def get_manufactDate(self):
        return self.manufactDate

    def get_lotNum(self):
        return self.lotNum

    def get_next(self):
        return self.next
    
    def set_serialNum(self, newNum):
        self.serialNum = newNum
    
    def set_manufactDate(self, newDate):
        self.manufactDate = newDate

    def set_lotNum(self, newNum):
        self.lotNum = newNum
    
    def set_next(self, new):
        self.next = new



class stack:
    def __init__(self):
        self.top = None
        self.bot = None

    def push(self, new: inventory):
        if self.get_length() == 0:       #if this is an empty stack
            self.bot = new
        else:    
            new.set_next(self.top)
        self.top = new

    def pop(self):
        if self.get_length() > 1:    #check if there are more than one elements
            temp = self.top
            self.top = temp.get_next()
        elif self.get_length() == 0:
            print('You cannot take a part from an empty list.')
            return 
        else:          #top equals to bot when there is only one elements in the stack
            temp = self.top
            self.top = None
            self.bot = None    
        return temp

    def peek(self):
        return self.top

    def is_empty(self):
        if self.get_length() == 0:
            return True
        else:
            return False

    def get_length(self):
        temp = self.top
        cnt = 0
        while temp != None:
            cnt += 1
            temp = temp.get_next()
        return cnt

    def display(self):
        temp = self.top
        while temp != None:
            print('Serial num:', temp.get_serialNum(), end=' ')
            print('Manufact date:', temp.get_manufactDate(), end=' ')
            print('Lot num:', temp.get_lotNum())
            temp = temp.get_next()

def main():
    sample = stack()

    #the loop
    done = False
    ask = ''
    serial = 0
    date = ''
    lot = 0
    while done == False:
        ask = input('Add(a) , Take(t) , Quit(q): ')
        if ask == 'a':
            serial = int(input('Please type the serial number: '))
            date = input('Please type the manufacted date: ')
            lot = int(input('Please type the lot number: '))
            sample.push(inventory(serial, date, lot))
        elif ask == 't':
            sample.pop()
        elif ask == 'q':
            done = True
        else:
            print('Invalid input')
    
    #display the contents
    sample.display()
    return 


if __name__ == '__main__': main()