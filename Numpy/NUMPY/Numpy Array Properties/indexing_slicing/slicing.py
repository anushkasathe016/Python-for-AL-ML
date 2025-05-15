"""array[start:stop:step]
    arrray[start:end], start to end -1
    negative step,-1 reverse
"""
import numpy as np

arr=np.array([10,20,30,40,50,60,70,80])
print(arr[1:5]) #index 1 to 4
print(arr[:5])# index 0 to 5
print(arr[::2])#every second element
print(arr[::-1])