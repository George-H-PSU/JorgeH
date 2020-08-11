#Hsieh_Program8
#Yuan-Chih Hsieh
#CMPSC132 Program8


#the class that store the employee data
class EmployeeInfo:
    def __init__(self, number, name):
        self.number = number
        self.name = name
    
    #employee ID number getter
    def get_number(self):
        return self.number
    
    #employee name getter
    def get_name(self):
        return self.name



#the node that used in binary search tree
class node:
    def __init__(self, employee):
        self.data = employee
        self.parent = None
        self.left = None
        self.right = None
    
    #employee data getter
    def get_data(self):
        return self.data
    
    #node's parent getter
    def get_parent(self):
        return self.parent
    
    #node's left child getter
    def get_left(self):
        return self.left
    
    #node's right child getter
    def get_right(self):
        return self.right
    
    #parent setter
    def set_parent(self, new_parent):
        self.parent = new_parent
    
    #left chilf setter
    def set_left(self, new_left):
        self.left = new_left
    
    #right child setter
    def set_right(self, new_right):
        self.right = new_right
    


#binary search tree
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, new):
        curNode = self.root
        #check if this is an empty BST
        if curNode == None:
            self.root = new
        #this loop keeps going until it finds a spot that is availible for new node
        while curNode != None:

            #current node is larger than the new node
            if curNode.get_data().get_number() > new.get_data().get_number():
                new.set_parent(curNode)
                #check if there is a spot for new node at cureent node's left child
                if curNode.get_left() == None:
                    curNode.set_left(new)
                    curNode = None
                else:   #move to the left child node
                    curNode = curNode.get_left()

            #current node is smaller or equal to the new node
            elif curNode.get_data().get_number() <= new.get_data().get_number():
                new.set_parent(curNode)
                #check if there is a spot for new node at cureent node's right child
                if curNode.get_right() == None:
                    curNode.set_right(new)
                    curNode = None
                else:   #move to the right child node
                    curNode = curNode.get_right()
        print('Finished!')
        return
    
    def search(self, key):
        curNode = self.root
        if curNode == None:
            print('This is an empty list')
            return None
        #this loop keeps going until the key number is founded or a None node is founded
        while curNode != None:
            #key number founded
            if curNode.get_data().get_number() == key:
                return curNode.data.get_name()
            #move to left child 
            elif curNode.get_data().get_number() > key:
                curNode = curNode.get_left()
            #move to right child 
            elif curNode.get_data().get_number() < key:
                curNode = curNode.get_right()
        if curNode == None:
            print('Not found')
            return None
        


def main():
    tree = BST()
    tree.insert(node(EmployeeInfo(2932, 'Catelyn Stark')))
    tree.insert(node(EmployeeInfo(1034, 'Cersei Lannister')))
    tree.insert(node(EmployeeInfo(3493, 'Daenerys Targaryen')))
    tree.insert(node(EmployeeInfo(2293, 'Jon Snow')))
    tree.insert(node(EmployeeInfo(2497, 'Sansa Stark')))
    tree.insert(node(EmployeeInfo(5483, 'Arya Stark')))
    tree.insert(node(EmployeeInfo(3994, 'Tywin Lannister')))
    choice = ''
    while choice != '3':
        print('---------------')
        print('Menu')
        choice = input('1) Insert\n2) Search\n3) Quit\n')
        print('---------------')
        if choice == '1':
            ID = int(input('Please enter the ID number: '))
            name = input('Please enter the name: ')
            employee = EmployeeInfo(ID, name)
            tree.insert(node(employee))
            print('Done')
        elif choice == '2':
            key = int(input('Please enter the ID you want to search for: '))
            print('The person you are looking for is ', end='')
            print(tree.search(key))
            print('Done')
        elif choice == '3':
            print('Thank you!')
        else:
            print('Invalid input')
    return 



if __name__ == '__main__': main()

