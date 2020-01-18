from timeit import time
from random import randrange

#Create a Random List of integers
my_list = [randrange(1000) for _ in range(1000)]

# ------ BubbleSort Algorithm ------

def OwnBubbleSort(list):
    start_time = time.time() 

    n = len(list) - 1
    while n > 0:
        for i in range(n):
            if list[i] > list[i + 1]:
                # SWAP ---->
                copy = list[i]
                list[i] = list[i + 1]
                list[i + 1] = copy
                # ----->
        n -= 1 #Decrement the range of the Cycle

    stop_time = time.time()
    print(f"{(stop_time-start_time):.7f}")


OwnBubbleSort(my_list) #Invoke BubbleSort function
print(my_list)  #Print on console my_list 
