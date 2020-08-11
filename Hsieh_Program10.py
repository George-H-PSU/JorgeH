#Hsieh_Program10
#Yuan-Chih Hsieh
#CMPSC132 Program10

import random
import time


def timer(f, arg):      ## using this function to calculate the runtime of
    t1 = time.time()    ## a specific function f for the argument arg
    f(arg)
    t2 = time.time()
    return t2 - t1


def merge_sort(lst):    ## first sorting algorithms: merge sort(my favorite)
    if len(lst) <= 1:   ## time complexity: O(N*logN)
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    merge_sort(left)
    merge_sort(right)
    merge = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merge.append(left[0])
            del left[0]
        else:
            merge.append(right[0])
            del right[0]
    merge.extend(left)  ## add the remaining elements in the left and right 
    merge.extend(right) ## list to the end of merge list
    return merge


def selection_sort(lst):    ## second sorting algorithms: selection sort
    ans = []                ## time complexity: O(N^2)
    while len(lst) > 0:
        minn = lst[0]
        for i in range(1, len(lst)):
            if lst[i] < minn:
                minn = lst[i]
        ans.append(minn)
        lst.remove(minn)
    return ans


def main():
    list1 = list(random.sample(range(1, 10000), 1000))      ## generate a random list 
    list2 = list1
    print("Merge sort runtime: ", end="")
    print("%.5f"%timer(merge_sort, list1), "s")             ## calculate the merge sort runtime to the fifth decimal place
    print("Selection sort runtime: ", end="")
    print("%.5f"%timer(selection_sort, list2), "s")         ## calculate the selection sort runtime to the fifth decimal place

    return 


if __name__ == "__main__": main()