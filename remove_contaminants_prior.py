#This script will take as input the prospector output of a set of experiments, and remove all the entries that are present in the given contaminant list
#The contaminants file must be in FASTA format, e.g. the contaminants file obtained from the MaxQuant website.
from sys import argv

print "****\nUsage: python %s <contaminants_file> <prospector_report_data> <output_filename>\n****" %argv[0]


def produce_contlist():
#returns a set of contaminant IDs from a FASTA file such as the MaxQuant one
	contlist=set()
	with open(argv[1], 'r') as cont:
		for line in cont:
			if line[0]=='>' and ':' in line:
				uniprot=line.split(':')[1].split(' ')[0]
				for e in uniprot.split(';'):
					contlist.add(e.split('-')[0])
	return contlist

data=[]
cont=produce_contlist()
with open(argv[2], 'r') as sd, open(argv[3], 'w') as ofile:
		for lin in sd:
			if lin.split('\t')[3] not in cont:
				ofile.write(lin)
