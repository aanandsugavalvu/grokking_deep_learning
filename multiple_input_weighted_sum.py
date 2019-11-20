#import sys


def weighted_sum(data, weights):
    assert (len(data) == len(weights))

    output = 0

    for i in range (len(data)):
    	output += data[i] * weights[i]

    return output

def predict(data, weights):
	assert (len(data) == len(weights))

	predicion = weighted_sum(data, weights)

	return predicion


input_toes = [8.5, 10, 23]
input_win_pc = [65, 34, 78]
input_fans = [12, 8, 15]

weights = [0.1, 0.2, 0]

assert (len(input_toes) == len(input_win_pc) == len(input_fans))

for i in range(len(input_fans)):
	input_vector = []
	input_vector.extend([input_toes[i], input_win_pc[i], input_fans[i]])
	predicion = predict(input_vector, weights)
	print "The chances of team %s winning is %r" % (i +1, predicion,)