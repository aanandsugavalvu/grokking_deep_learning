import numpy as np

def predict(input, weights):
	assert(len(input) == len(weights))

	pred = input.dot(weights)
	return pred

weights = np.array([0.1, 0.2, 0])

input_toes = np.array([8.5, 10, 23])
input_win_pc = np.array([65, 34, 78])
input_fans = np.array([12, 8, 15])

for i in range(len(input_fans)):
	input_vector = np.array([input_toes[i], input_win_pc[i], input_fans[i]])
	predicion = predict(input_vector, weights)
	print "The chances of team %s winning is %r" % (i +1, predicion,)