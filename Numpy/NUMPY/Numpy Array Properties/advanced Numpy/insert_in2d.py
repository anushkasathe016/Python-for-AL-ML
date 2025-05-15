import numpy as np
arr=np.array([[1,2],[3,4]])
print(arr)
#insert a new row at index 1
new_arr_2d=np.insert(arr,1,[5,6],axis=1)
print(new_arr_2d)

new_arr_2d=np.insert(arr,1,[5,6],axis=0)
print(new_arr_2d)

new_arr_2d=np.insert(arr,1,[5,6],axis=None)
print(new_arr_2d)