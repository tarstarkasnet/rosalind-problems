"""

Problem 7 - Introduction to Mendelian Inheritanceclick to expand

Problem

Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon 
with a random variable, which is simply a variable that can take a number of different distinct 
outcomes depending on the result of an underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X
represent the random variable corresponding to the color of a drawn ball, then the probability of
 each of the two outcomes is given by Pr(X=red)=3/5 and Pr(X=blue)=2/5

.

Random variables can be combined to yield new random variables. Returning to the ball example, let Y
model the color of a second ball drawn from the bag (without replacing the first ball). The 
probability of Y being red depends on whether the first ball was red or blue. To represent all 
outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents 
all possible individual probabilities for X and Y

, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by 
the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an 
event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A
be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different 
outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 3/10+1/10=2/5

(see Figure 2 above).

Given: Three positive integers k, m, and n, representing a population 
containing k+m+n organisms: k individuals are homozygous 
dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual 
possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two 
organisms can mate.
Sample Dataset

2 2 2

Sample Output

0.78333

"""

def mendel1():
	
	k = int(input("Enter k (homozygous dominant): "))
	m = int(input("Enter m (heterozygous dominant): "))
	n = int(input("Enter n (homozygous recessive): "))
	

	if k == 0 or k == 1:
		set11 = 0 #defaults to 0 if this is 0 or 1
	else:
		set11 = (k * (k-1)/2) / ((k + m + n) * (k + m + n -1) / 2)
		
	if m == 0 or m == 1:
		set22 = 0 #defaults to 0 if this is 0 or 1
	else:
		set22 = (m * (m - 1) / 2) / ((k + m + n) * (k + m + n -1) / 2)
		
	if n == 0 or n == 1:
		set33 = 0 #defaults to 0 if this is 0 or 1
	else:
		set33 = (n * (n - 1) /2) / ((k + m + n) * (k + m + n -1) / 2)
	
	set12 = (k * m) / ((k + m + n) * (k + m + n -1) / 2)
	set13 = (k * n) / ((k + m + n) * (k + m + n -1) / 2)
	set23 = (m * n) / ((k + m + n) * (k + m + n -1) / 2)
	
	# in case you need to error check:
	# print("set11", set11)
	# print("set12", set12)
	# print("set13", set13)
	# print("set22", set22)
	# print("set23", set23)
	# print("set33", set33)
	
	# sets 11, 12, 13, 22, and 23 have dominant alleles
	# 11, 12, and 13 are 100% chance, 22 is 75% chance, 23 is 50% chance
	# reasons why for this is good ol' Mendel boxes
	total = set11 + set12 + set13 + (set22 * 0.75) + (set23 * 0.5)
	print("total", total)
	

	
mendel1()


"""

Enter k (homozygous dominant): 21
Enter m (heterozygous dominant): 26
Enter n (homozygous recessive): 29
set11 0.07368421052631578
set12 0.19157894736842104
set13 0.21368421052631578
set22 0.11403508771929824
set23 0.26456140350877194
set33 0.1424561403508772
total 0.6967543859649122

"""