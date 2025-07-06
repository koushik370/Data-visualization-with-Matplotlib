import numpy as np
a=np.arange(12)
a=np.reshape(a,(3,4))
print("before transpose of matrices")
print(a)
a=np.transpose(a)
print(a)