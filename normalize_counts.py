#This script will take the results table from APMS experiments (that is used as input for the APMS analysis pipeline)
#And will normalize all spectral counts (or unique peptide counts) by the total number of counts in the experiments (counts/totalcounts*10000)
#The aim is to see if this improves the clustering of the samples to be able to tell apart 'bad' samples

from sys import argv

t=[]
with open(argv[1], 'r') as inputfil:
	for r in inputfil:
		t.append(r.strip(' \n').split('\t'))

d={} #dictionary
for l in t[1:]:
	if l[0] not in d.keys():
		d[l[0]]=0
	d[l[0]]+=int(l[4])

#Output table with normalized values
o=open(argv[2], 'w')
o.write(('\t').join(t[0])+'\n')

for e in t[1:]:
	e[4]=str(int(round(float(e[4])/d[e[0]]*10000)))
	o.write('\t'.join(e)+'\n')
o.close()

print d
print len(d.keys())
