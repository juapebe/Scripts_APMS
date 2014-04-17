#Generate a small bar chart that shows the peptide counts along APMS experiments
#The input is a file that contains a single peptide count value for every experiment
#Initially used for BAG3 peptide counts through experiments
#Can also be used for unique peptides
#Input: 

from sys import argv
import pylab as pl
#import numpy as np

data=[]
exp=[]
counts=[]
BAG3=[] #Whether it is a BAG3 bait or not. For later coloring
blank=[4,7,10,13,16,19,22,24, 25, 28, 31, 34, 37, 40, 43, 46, 49, 50, 53, 56, 59, 62, 65, 68, 71, 74, 75, 78, 81, 84, 87, 90, 93, 96, 99, 100, 103, 106, 109, 112, 115, 118, 121, 124, 125, 128]
#the number of sample after which blanks were run

with open(argv[1], 'rU') as filein:
	filein.readline()
	for row in filein:
		data.append(row)

for r in data:
	r=r.strip('\n').split('\t')
	exp.append(r[-2])
	counts.append(int(r[-1]))
	if 'BAG3' in exp[-1]:
		BAG3.append('r')
	else:
		BAG3.append('b')


fig=pl.figure(figsize=(13, 9))
ax=pl.subplot(111)
width=0.5
ax.bar(range(len(counts)), counts, width=width, linewidth=0, color=BAG3, align='center')
ax.set_xticks(range(len(exp)))
ax.set_xticklabels(exp, rotation=90, fontsize=5)
ax.set_xlim(-1,130)
ax.set_title('BAG3 spectral counts per experiment')
ax.set_xlabel('Experiment')
ax.set_ylabel('# Spec Counts')

#Draw blank lines (comment out if not wanted)
#for b in blank:
#	ax.axvline(x=b-width, color='g', linestyle='--')

pl.savefig("BAG3_counts.pdf")