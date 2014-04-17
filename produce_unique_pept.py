print "*"*8
print "This program traverses the list of peptides from output"
print "and displays the list of UNIQUE peptides-experiments"
print "identified for those entries containing the provided term"
print "in the protein name field."
print "E.g. I want to filter down to the peptides that belong to 'BAG3'"

print "\n sample usage: \n python produce_unique_pept.py <input_peptfile> <output_peptfile>"
print "*"*8

import sys

#Traverses input list
inp=open(sys.argv[1], 'r')
out=open(sys.argv[2], 'w')

unique=[]
d={}

st=raw_input("Please write the string of text that you want present in the entries selected (e.g. 'BAG3', or 'HOMO SAPIENS')\n (leave it blank for 'all')\n>>>")

c=0
for line in inp:
	if c==0:
		out.write(line.strip('\n')+'\tSpecific Pept Counts\n')
	c+=1
	if st in line:
		l=line.strip(' \n').split('\t')
		#k=(l[0], l[-11]) #Modifications will not be counted as different peptides
		k=(l[0], l[-11], l[-10]) #Use this line if you want unique lines for modifications, too
		if k not in d:
			d[k]=l
			d[k].append('1')
		else:
			d[k][-1]=str(int(d[k][-1])+1)

for e in d:
	out.write('\t'.join(d[e]))
	out.write('\n')
 
 #inp.close()
 #out.close()