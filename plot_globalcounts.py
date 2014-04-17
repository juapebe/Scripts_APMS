#This script will take the results table from APMS experiments (that is used as input for the APMS analysis pipeline)
#And will plot the spectral counts for every one of the experiments.
#The spectral counts will be displayed grouped per bait.
#The input is the '_wKeys' file that is first output of the APMS pipeline analysis (you can start running it and halt pretty soon and still get the table)
#It also produces a file with the counts per experiment (for further processing)
#and a file with the number of experiments per bait (_BADs are excluded as per label)

print "****\nUsage: python plot_globalcounts.py <name-of-_wKeys-file>\n****"

from sys import argv
import pylab as pl

#open file. load table.
t=[]
with open(argv[1], 'r') as inputfil:
	for r in inputfil:
		t.append(r.strip(' \n').split('\t'))

d={} #dictionary
for l in t[2:]:
	if len(l[1]) < 8:
		if l[1] not in d.keys():
			d[l[1]]=['',0]
			d[l[1]][0]=l[0]
		d[l[1]][1]+=int(l[5])


keys=d.keys()[:]
keys.sort()
exp=[]
counts=[]
for e in keys:
	exp.append(d[e][0]+'_'+e)
	counts.append(d[e][1])
print counts
print len(counts)

#Elaborate plot
fig=pl.figure(figsize=(16, 9))
ax=pl.subplot(111)
width=0.75
ax.bar(range(len(counts)), counts, width=width, linewidth=0, align='center')
ax.set_xticks(range(len(exp)))
ax.set_xticklabels(exp, rotation=90, fontsize=5)
ax.set_xlim(-1,160)
ax.set_title('Total spectral counts per experiment\n(script used for this: %s)'%argv[0])
ax.set_xlabel('Experiment')
ax.set_ylabel('# of Total Spec Counts')

#Draw set separating lines (comment out if not wanted)
sep=[24, 49, 74, 99, 124, 149]
for b in sep:
	ax.axvline(x=b-width*0.5, color='m', linestyle='-', linewidth=1)

pl.savefig("experiment_counts.pdf")


#Output table to put on excel (easier to process in groups by bait)
o=open("counts_per_exp.txt", 'w')

for e in d:
	o.write('\t'.join([e, d[e][0], str(d[e][1])])+'\n')
o.close()


#Output table with replicates per bait (at least, the ones not tagged)
o2=open("exp_per_bait.txt", 'w')
d2={}
for k in d:
	bait=d[k][0]
	print bait
	if bait not in d2:
		d2[bait]=0
	d2[bait]+=1
	print d2[bait]

for b in d2:
	o2.write('\t'.join([b, str(d2[b])])+'\n')
o2.close()

