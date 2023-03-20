import numpy as np

# print(np.__version__)
# np.show_config()

# Z = np.zeros(10)
# print(Z)

# Z = np.zeros((10,10))
# print("%d bytes" % (Z.size * Z.itemsize))

nz = np.nonzero([1,2,0,0,4,0])
print(nz)