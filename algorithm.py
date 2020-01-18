from timeit import time
from random import randrange

#Create a Random List of integers
my_list = [randrange(1000) for _ in range(10)]

# ------ BubbleSort Algorithm ------

def OwnBubbleSort(_list):
    start_time = time.time() 

    limit = len(_list) - 1
    while limit > 0:
        for i in range(limit):
            if _list[i] > _list[i + 1]:
                # SWAP ---->
                copy = _list[i]
                _list[i] = _list[i + 1]
                _list[i + 1] = copy
                # ----->
        limit -= 1 #Decrement the range of the Cycle

    stop_time = time.time()
    print(f"{(stop_time-start_time):.7f}")


OwnBubbleSort(my_list) #Invoke BubbleSort function
print(my_list)  #Print on console my_list 
