#np.concatenate((array1,array2),axis=0)

import numpy as np

arr1=np.array([12,12,12])
arr2=np.array([31,31,31])

new_arr=np.concatenate((arr1,arr2))
print(new_arr)