#This script will, for every experiment, take the BAG counts/pepitdes and add collapse them into a single annotation
#It is recommended to do this before inputting the data into the APMS analysis pipeline, so BAG3 will show as a single def 

from sys import argv

#Input data is just the Prospector output in the form of a list, a row per entry.
def merge_counts(data=[]):
	currentexp=''
	rem=[]
	for e in data:
		if 'BAG3' in e[-1]:
			if e[0]!=currentexp:
				e[3], e[-1],e[-2], e[-3]='O95817', 'BAG3_HUMAN BAG family molecular chaperone regulator 3', 'HOMO SAPIENS', '61595.2'
				currentexp=e[0]
			else:
				rem.append(e)

	for t in rem:
		data.remove(t)

	return data


if __name__=='__main__':
	print "********\nUsage: python merge_BAGcounts.py <data_file> <output_file>\n*******"
	#A list of the BAG3_containing lines in data
	dat=open(argv[1], 'r')
	data=[]
	for l in enumerate(dat):
		data.append(l[1].strip('\n').split('\t'))
	dat.close()

	data_processed=merge_counts(data)

	#print output to file
	out=open(argv[2], 'w')
	for line in data_processed:
		out.write('\t'.join(line)+'\n')
	out.close()