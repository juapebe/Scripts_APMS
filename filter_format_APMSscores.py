#A script to take the SAINT information for the BAGs from the output file obtained in the APMS pipeline implemented by Erik
#and generating a file that we could use for further processing, such as clustering
from sys import argv
import csv

print "****\nRemember to manually remove the baits you don't want first\n****"
print "Usage: python filter_format_APMSscores.py <input_scoresfile> <output_file>"

#Reads data form .txt output file
t=[]
header=[]
with open(argv[1], 'rU') as filein:
	header=filein.readline().strip('\n').split('\t')
	for row in filein:
		t.append(row.strip('\n').split('\t'))

exindex=header.index("BAIT")
upindex=header.index("gene_name")

for element in enumerate(header):
	print element

#Chooses which criteria will be used in calculations. To simplify output.
criteriaindex=raw_input("Which column would you like to be used for the report? \nJust input column number from the list above:\n>>")
criteriaindex=int(criteriaindex)

#Generates a unique list of UniprotIDs
finalset=set()
upIDs=[]
exIDs=[]
superdict={} #a dictionary of dictionaries, one per bait

for e in t:
	finalset.add((e[exindex], e[upindex], e[criteriaindex]))
	bait=e[exindex]
	prey=e[upindex]
	value=e[criteriaindex]
	if bait not in exIDs:
		exIDs.append(bait)
		superdict[bait]={}
	if prey not in upIDs:
		upIDs.append(prey)
	superdict[bait][prey]=value

print "Total number of bait-prey pairs: %i"%len(t)
print "Number of preys with no assigned UniprotID (usually GFP, VIF, and some obsolete IDs found): %i"%(len(t)-len(finalset))
print "Total number of different Uniprot IDs pairs: %i"%len(upIDs)
print "Total number of unique baits (including negative control):%i"%len(exIDs)

print len(superdict)
for d in superdict:
	for prey in upIDs:
		if prey not in superdict[d].keys():
			superdict[d][prey]='0'


#Remove negative control column. Comment out if you want to keep it.
exIDs2=[]
remterm=raw_input("If you would like to select specific baits, write the string the name should contain (e.g. 'BAG3')\n>>")
exIDs.remove('negative')
print exIDs
print len(exIDs)
for ex in exIDs:
	print ex
	if remterm in ex:
		exIDs2.append(ex)


finalT=[]
finalT.append(['']+upIDs)

for bait in exIDs2:
	finalT.append([bait])
	for prey in upIDs:
		finalT[-1].append(superdict[bait][prey])

finalT=zip(*finalT)

criteria_threshold=raw_input("Would you like to set a threshold value?\nOnly preys with at least one bait over that score will be reported\n If no threshold, just press enter\n>>")
criteria_threshold=float(criteria_threshold)

#Pick only those for which at least one of the samples has P>threshold
delList=[]
for item in finalT[1:]:
	t=0
	for v in item[1:]:
		if v!='NA':
			if float(v)>criteria_threshold:
				t=1
	if t==0:
		finalT.remove(item)

#Write output table
output=open(argv[2], 'w')
for entry in finalT:
	output.write('\t'.join(entry)+'\n')