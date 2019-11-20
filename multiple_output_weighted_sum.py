"""
In this example, a single input data will be applied to multiple weights to predict multiple outcomes.
Input is the win percentage of the team
The weights will be of hurt team members, winning probability and sad team members
"""

weights = [0.3, 0.2, 0.9]
weight_criteria = ["Hurt Team Members", "Win Probability", "Sad Team Members"]

def elem_mul(input, weights):
	output = [0, 0, 0]
	assert(len(output) == len(weights))

	for i in range(len(weights)):
		output[i] = input * weights[i]

	return output

def predict(input, weights):
	pred = elem_mul(input, weights)

	return pred

input = [0.65, 0.8, 0.8, 0.9]

for i in range(len(input)):
	prediction = predict(input[i], weights)
	print "Team %d results : " % (i+ 1,)
	print "----------------------------"

	for j in range(len(prediction)):
		print "The prediction for %s is %r" % (weight_criteria[j], prediction[j],)

	print "\n"

