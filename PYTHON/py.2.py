import numpy as np

numpy_baseball = np.array([4,5,8,6,5,7,8,9,6,5])

numpy_baseball = np.where(numpy_baseball == 6, 50, numpy_baseball)

print(numpy_baseball)
