"""
Problem 1 - Counting DNA Nucleotides 

Given: A DNA string s

of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

.
Sample Dataset

AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output

20 12 17 21


"""

def baseCounter():
	print("Input the DNA string to have the bases counted: ")
	inputString = input()

	# split the input into individual bases
	inputSplit = list(inputString)

	#set up blank counters
	aCount = 0
	cCount = 0
	gCount = 0
	tCount = 0

	#work through each on to do the counting, at this point we don't care about it only doing capital letters
	for i in inputSplit:
		if i == "A":
			aCount = aCount + 1
		elif i == "C":
			cCount = cCount + 1
		elif i == "G":
			gCount = gCount + 1
		elif i == "T":
			tCount = tCount + 1
			

	#print the output
	print(str(aCount) + " " + str(cCount) + " " + str(gCount) + " " + str(tCount))

baseCounter()

"""

Input the DNA string to have the bases counted:
CCACGCTACCGCCAACAAGGCGCTGACCGTGCTAGTTCAAAAATATTTCTAGTATCAGCATTTAGTCACTAACCACACCGATTCGTGAAGCCTGGCAGCTGCAGCGGGGTGTAGCCTCTTATGTTATAGGTTGCCTAAGTTGGATGCTCTGACCACAACGCTGATGCCTGTGTGCAAGCAGTTCTTGAGTTTGTGCTATGACTGCTAGCAAATTCCATACAAATCTAAAAAATAAGCTGAGCTCGACCTCGCATCTTATACGCGTGCCTACGTACAGCATGAGCGCTTTTAGCACTACGCATTCCCATCTGAACGCCGTAAATATCCATGGCATTGGTGGGCCTAACGTATGGGGCCGCGTGCGGGCGAAACTATTGACAAGCGTCTCCGAGAGGATGTATCCGACGGTCCAGACGGCAAGTAGCCCGTTATCTTTGATAAGATGTGATTATCCCCAATGGGCGGATGGCACCCCCTGGTCTCTAGAGTTGTTTCAACAGTTTTCTTGTGCATCTACCATTACGGACGTAGATCCTTGTTACGTAACACCCGAAAGACCCGCTTCAGGCGTACTGAGCTCAATGGCGTTTGGTATCAGCCGCCACGGTACGGTCCGTATACACTTTGAAAAGCCCTATCTAGCGGAAGAACGCTGAGAAGACGCACATCAACGACGAGTACCAATCTACGCAGGCAGTTCCATAAGTCCGCTACGCAAGTTCACCCTGCACTTGGAGGAGGTTATGATGACTAGTCTCCGGATTGCTAATCAATAGCAGGACTGGGGCCCGGAGATGATACTATCGGCAAGTGTCGGATACCGGGTACTGTCCGGCTCTGTTCCATGTGTGCGGTTCCGAACTGGGGGTATTCATGGCCATGTTAACTGTTGTAATCTCAA
220 229 225 227

"""
		