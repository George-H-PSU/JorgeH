#Hsieh_Program5
#Yuan-Chih Hsieh
#CMPSC132 Program5

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, new):       #this function occurs whenever the next data changes
        self.next = new

    def set_prev(self, new):       #this function occurs whenever the previous data changes
        self.prev = new


class LinkedList:                  #every elements in this linked list would be a node
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def insert(self, CurNode, new): #this is an insert function rather than an insert-after
        newNode = Node(new)
        if self.get_length() == 0:            #check if it is an empty list or not
            self.head = newNode
            self.tail = newNode
        elif self.head == CurNode:  #the case if the current node is at the head position
            temp_prev = CurNode.get_prev()
            CurNode.set_prev(newNode)
            newNode.set_prev(temp_prev)
            newNode.set_next(CurNode)
            self.head = newNode
        else:
            temp_prev = CurNode.get_prev()
            temp_prev.set_next(newNode)
            newNode.set_prev(temp_prev)
            newNode.set_next(CurNode)
            CurNode.set_prev(newNode)

    def deleting(self, item):
        temp = self.head            #search for the item for list head
        deleted = False
        temp_next = None
        temp_prev = None
        while deleted == False and temp != None:
            if temp.get_data() == item:
                temp_next = temp.get_next()
                temp_prev = temp.get_prev()
                temp_next.set_prev(temp_prev)
                temp_prev.set_next(temp_next)
                deleted = True
            else:
                temp = temp.get_next()
        if deleted == False:
            print('The item you want to delete is not in this list.')

    def searching(self, key):
        temp = self.head            #search for the item for list head
        found = False
        while found == False and temp != None:  #temp would be None if it is out of the list
            if temp.get_data() == key:
                found = True
                return temp          #return the key node
            else:
                temp = temp.get_next()
        if found == False:
            print('The item you are searching for is not in this list.')
            return 

    def append(self, new):          #add the new value at the end of this list
        newNode = Node(new)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.set_prev(self.tail)     
            self.tail.set_next(newNode)     #no need to set newNode's next, because the default is None
            self.tail = newNode

    def get_length(self):           #get the length of the list
        i = self.head 
        cnt = 0
        while i != None:
            cnt += 1
            i = i.get_next()
        return cnt 



def main():
    sample = LinkedList()
    grade = 0
    i = 0
    while i < 10:
        try:
            grade = int(input('Please enter a grade: '))
            sample.append(grade)
            i += 1
        except ValueError:
            print('Please enter an integer!')

    '''
    x = sample.searching(10)        #using the searching method
    sample.insert(x, 110)           #using the insert method
    sample.deleting(20)             #using the deleting method
    '''

    #print all the grades in the following for loop
    temp = None
    total = 0
    print('Grades: ', end='')             
    for i in range(sample.get_length()):            
        if temp == None:
            temp = sample.get_head()
        else:
            temp = temp.get_next()
        print(temp.get_data(), end=' ')
        total += temp.get_data()
    print('')
    print('Average:', '{:.2f}'.format(total/sample.get_length()))



if __name__ == "__main__": main()