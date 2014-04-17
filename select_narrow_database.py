#The script below takes the list of all the uniprot proteins and their concatenations/inversions (for negative control) and narrows it down to those
#that have the uniprot ID codes found in another file
#This script will take two files: proteins_all and proteins_selected
#The proteins selected file has to have the uniprot numbers on it. Preferably its a FASTA file.

from sys import argv
import csv

print "Usage: python select_narrow_database.py <input_bigdbfile> <input_selectedFASTA file> <output_database>"

#Reads data form .txt output file
ti=[] #initial table
tiu=[] #initial uniprots
header=[]
with open(argv[1], 'rU') as filein:
	for row in filein:
		ti.append(row.strip('\n').split('\t'))


for line in ti:
	line=line[0].strip('>-').split('|')
	for e in line:
		if len(e)==6:
			tiu.append(e)

for l in ti[0:10]:
	print l

for l in tiu[0:10]:
	print l

"""
#Write output table
output=open(argv[2], 'w')
for entry in finalT:
	output.write('\t'.join(entry)+'\n')
"""