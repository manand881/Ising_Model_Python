import numpy as np
x = np.ones((8,8),dtype=int)
x[1::2,::4] = -1
x[::2,1::4] = -1
print(x)