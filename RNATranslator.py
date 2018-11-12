# Take Input from user regerding input file name and output file name
import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

# Initial gene
initialGene = open(arguments[0]).readlines()
TATAIndicator = ''

# This function finds the complementing DNA strand and turns the DNA encoded 
# information into an RNA single strand sequence
def findRNASequence(geneSequence):
	# Initialise as an array, to make it easier to find and replace/assign
	complementOfGeneSequence = []
	reverseComplementOfGeneSequence = ''
	TATA_Boolean = ''
	# Find and store in a variable
	for i in range(0,len(geneSequence)):
		if geneSequence[i] == 'T' or geneSequence[i] == 't':
			complementOfGeneSequence += 'A'
		if geneSequence[i] == 'A' or geneSequence[i] == 'a':
			complementOfGeneSequence += 'U'
		if geneSequence[i] == 'G' or geneSequence[i] == 'g':
			complementOfGeneSequence += 'C'
		if geneSequence[i] == 'C' or geneSequence[i] == 'c':
			complementOfGeneSequence += 'G'

	# Turn back into string
	complementOfGeneSequence = ''.join(complementOfGeneSequence)

	# Reverse the sequence
	reverseComplementOfGeneSequence = complementOfGeneSequence[::-1]

	returnvarReverseComplandTATA = reverseComplementOfGeneSequence
	return returnvarReverseComplandTATA

f = open(str(arguments[1])+'.txt','w+')
for l in range(0, len(initialGene)):
	f.write(findRNASequence(initialGene[l]))
	print('Progressing. Reached line number : ' + str(l))
