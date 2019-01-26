"""

Problem 8 - The Genetic Code

Problem

The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s

corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s

.
Sample Dataset

AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output

MAMAPRTEINSTRING


"""




#regex
import re

#read file into strings
fileToRead = open("C:/pycode/rosalind/rosalind_aatransl_input.txt","r+")

def transl():
	
	# read entire file as one chunk, then split into list of 3bp long strings
	fileContent = fileToRead.read()
	triplicats = re.findall("...", fileContent)
	#print(triplicats) #ec
	
	aaCode = ""
	
	for i in triplicats:
		newCode = rnaTranslate(i)
		aaCode = aaCode + newCode
		
	print(aaCode)	
	
	
	
def rnaTranslate(code):
	#your handy-dandy RNA translation tool, edit "STOP" to whatever you need
	if (code == "UUU" or code == "UUC"):
		translate = "F"
	if (code == "UUA" or code == "UUG" 
			or code == "CUU" or code == "CUC" 
			or code == "CUA" or code == "CUG"):
		translate = "L"
	if (code == "UCU" or code == "UCC"
			or code == "UCA" or code == "UCG"):
		translate = "S"
	if (code == "UAU" or code == "UAC"):
		translate = "Y"
	if (code == "UGU" or code == "UGC"):
		translate = "C"
	if code == "UGG":
		translate = "W"
	if (code == "CCU" or code == "CCC"
			or code == "CCA" or code == "CCG"):
		translate = "P"
	if (code == "CAU" or code == "CAC"):
		translate = "H"
	if (code == "CAA" or code == "CAG"):
		translate = "Q"
	if (code == "CGU" or code == "CGC"
			or code == "CGA" or code == "CGG"
			or code == "AGA" or code == "AGG"):
		translate = "R"
	if (code == "AUU" or code == "AUC"
			or code == "AUA"):
		translate = "I"
	if code == "AUG":
		translate = "M"
	if (code == "ACU" or code == "ACC"
			or code == "ACA" or code == "ACG"):
		translate = "T"
	if (code == "AAU" or code == "AAC"):
		translate = "N"
	if (code == "AAA" or code == "AAG"):
		translate = "K"
	if (code == "AGU" or code == "AGC"):
		translate = "S"
	if (code == "GUU" or code == "GUC"
			or code == "GUA" or code == "GUG"):
		translate = "V"
	if (code == "GCU" or code == "GCC"
			or code == "GCA" or code == "GCG"):
		translate = "A"
	if (code == "GAU" or code == "GAC"):
		translate = "D"
	if (code == "GAA" or code == "GAG"):
		translate = "E"
	if (code == "GGU" or code == "GGC"
			or code == "GGA" or code == "GGG"):
		translate = "G"
	if (code == "UAA" or code == "UAG"
			or code == "UGA"):
		translate = "STOP"
	
	return translate
		

	
transl()





