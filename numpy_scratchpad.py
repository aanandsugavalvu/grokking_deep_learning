import numpy as np

a = np.array([0, 1, 2, 3])
b = np.array([4, 5, 6, 7])
c = np.array([[0, 1, 2, 3],
			[4, 5, 6, 7]])
# (rows, columns)
d = np.zeros((2, 4))
e = np.random.rand(2, 5)

print a * c