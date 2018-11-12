# Take Input from user regerding input file name and output file name
import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

# Initial RNA
initialRNA = open(arguments[0]).readlines()

aminoAcid = {'AUG': 'M', 'GCG': 'A', 'UCA': 'S', 'GAA': 'E', 'GGG': 'G', 'GGU': 'G', 'AAA': 'K', 'GAG': 'E', 'AAU': 'N', 'CUA': 'L', 'CAU': 'H', 'UCG': 'S', 'UAG': 'STOP', 'GUG': 'V', 'UAU': 'Y', 'CCU': 'P', 'ACU': 'T', 'UCC': 's', 'CAG': 'Q', 'CCA': 'P', 'UAA': 'STOP', 'AGA': 'R', 'ACG': 'T', 'CAA': 'Q', 'UGU': 'C', 'GCU': 'A', 'UUC': 'F', 'AGU': 'S', 'AUA': 'I', 'UUA': 'L', 'CCG': 'P', 'AUC': 'I', 'UUU': 'F', 'CGU': 'R', 'UGA': 'STOP', 'GUA': 'V', 'UCU': 'S', 'CAC': 'H', 'GUU': 'V', 'GAU': 'D', 'CGA': 'R', 'GGA': 'G', 'GUC': 'V', 'GGC': 'G', 'UGC': 'C', 'CUG': 'L', 'CUC': 'L', 'CGC': 'R', 'CGG': 'R', 'AAC': 'N', 'GCC': 'A', 'AUU': 'I', 'AGG': 'R', 'GAC': 'D', 'ACC': 'T', 'AGC': 'S', 'UAC': 'Y', 'ACA': 'T', 'AAG': 'K', 'GCA': 'A', 'UUG': 'L', 'CCC': 'P', 'CUU': 'L', 'UGG': 'W'}

def translateToProtein(RNA):
    protein = []
    # Find the start codon in the RNA sequence.
    start = RNA.find('AUG')
    # Proceed forwards in the sequence until the end.
    while start+2 < len(RNA):
        # Read in the next codon.
        codon = RNA[start:start+3]
        # Break if the codon is a stop codon.
        if aminoAcid[codon]=='STOP': 
            print('Stop codon identified.');
            break

        # Add the translated codon to the end of the protein string.
        protein += (aminoAcid[codon])
        start+=3
    return ''.join(protein)

f = open(str(arguments[1])+'.txt','w+')
for l in range(0, len(initialRNA)):
    f.write(translateToProtein(initialRNA[l]))
    print('Progressing. Reached line number : ' + l)
