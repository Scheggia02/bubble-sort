from timeit import time
from random import randrange 

lista = [ randrange(1000) for _ in range(10)] 

#------ My BubbleSort Algorithm ------

def OwnBubbleSort(list):
    n = len(list) - 1  
    while n > 0:
        for i in range(n):
            if list [i] > list[i + 1]:
                #SWAP ---->
                copy = list[i]
                list[i] = list[i + 1]
                list[i + 1] = copy
                #----->
        n -= 1 


OwnBubbleSort(lista)

print(lista)




