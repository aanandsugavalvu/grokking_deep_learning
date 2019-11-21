import numpy as np

def neural_network(input, weights):
	hidden_prediction = input.dot(weights[0])
	prediction = hidden_prediction.dot(weights[1])
	return prediction


"""
Notice the .T at the end of the array definition. This is the transpose of the matrix.
"""
            # toes win% fan_turnout
ih_wgt = np.array([ [0.1, 0.1, -0.3], # hidden[0]
			[0.1, 0.2, 0.0], # hidden[1]
			[0.0, 1.3, 0.1] ]).T # hidden[2]

            # hid[0] hid[1] hid[2]
hp_wgt = np.array([ [0.1, 0.1, -0.3], # hurt?
			[0.1, 0.2, 0.0], # win?
			[0.0, 1.3, 0.1] ]).T # sad?

weights = [ih_wgt, hp_wgt]

weight_criteria = ["Hurt Team Members", "Win Probability", "Sad Team Members"]

input_toes = [8.5, 9.5, 9.9, 9.0]
input_win_pc = [0.65, 0.8, 0.8, 0.9]
input_fans = [1.2, 1.3, 0.5, 1.0]

for i in range(len(input_toes)):

	# an input vector is formed based on available data
	input_vector = np.array([input_toes[i], input_win_pc[i], input_fans[i]])
	prediction = neural_network(input_vector, weights)
	print "Team %d results : " % (i+ 1,)
	print "----------------------------"

	for j in range(len(prediction)):
		print "The prediction for %s is %r" % (weight_criteria[j], prediction[j],)

	print "\n"