from scoop import futures
import time
import math
import numpy as np
import operator
import random


def func(value):
    result = math.sqrt(value)
    print(f"The value {value} and the elaboration is {result}")
    return result

if __name__ == "__main__":
    data = np.array([12,3,4,2,6,7,34,666666,3,324,23,2,1,9])
    # results = list(futures.map(func, data))
    # for result in results:
    #     print(f"This is the result: {result}")
        
    # results = sum(futures.map(func, data))
    # print(f"resution result is {results}")
    
    #result = futures.mapReduce(func, operator.add, data)
    #print(f"reduction result is {result}")
    
    result = np.mean(list(futures.map(int, futures.map(func, data))))
    print(f"mean result is {result}")
    