#Hsieh_Program4
#Yuan-Chih Hsieh
#CMPSC132 Program4


lst = []
class assignment:
    def __init__(self, name, grade):
        self.name = name
        self.grade = int(grade)
        lst.append(self.grade)

    def get_name(self): #name accessor
        return self.name

    def get_grade(self): #grade accessor
        return self.grade
    
    def set_name(self, new_name): #name mutator
        self.name = new_name

    def set_grade(self, new_grade): #grade mutator
        global lst
        lst.remove(self.grade) #delete the old grade
        self.grade = int(new_grade)
        lst.append(self.grade)

    def print(self): #print out the grades
        global lst
        print(lst)

    def sort(self): #sort the grades in lst
        global lst
        lst = mergesort(lst)
        return lst


def mergesort(x):   #using mergesort algorithms
    if len(x) <= 1:
        return x
    
    mid = len(x) // 2
    left = x[:mid]  #left part of the list
    right = x[mid:]  #right part of the list
    left = mergesort(left)
    right = mergesort(right)

    liist = []
    while len(left) > 0 and len(right)>0:   #if left and right is not an empty list
        if left[0] <= right[0]:
            liist.append(left[0])
            left = left[1:]
        elif right[0] < left[0]:
            liist.append(right[0])
            right = right[1:]
    liist.extend(left)    #extend the rest of the elements to the list
    liist.extend(right)   #extend the rest of the elements to the list

    return liist


def main():
    sample1 = assignment('George', 87)
    sample2 = assignment('Charles', 99)
    sample3 = assignment('Miller', 60)
    sample4 = assignment('Zachary', 45)
    sample5 = assignment('Jessica', 100)
    sample6 = assignment('Ray', 69)
    sample7 = assignment('Joseph', 89)
    sample8 = assignment('Tim', 72)
    sample9 = assignment('Darren', 31)
    sample10 = assignment('Arthur', 58)
    sample1.print()
    sample2.sort()
    sample5.print()

if __name__ == '__main__': main()