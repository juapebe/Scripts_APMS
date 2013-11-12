#THe following script will take any number of given files (from argv)
#and merge them on a single, long report file. They all should have same heading.

from sys import argv

def merge(files):
	t=[]
	for n in range(1,len(files)):
		f=open(files[n])
		for l in f:
			i=l.strip('\n').split('\t')
			if len(i[0])==6: #adds a '0' to the sample index if it only has 2 digits
				i[0]=i[0].split('-')
				i[0]='-0'.join(i[0])
			if n==1:
				t.append(i)
			else:
				if i!=t[0]: #skips the header line
					t.append(i)
		f.close()
	#Prompts for output filename, and write
	output=raw_input("Please write output filename and press enter:\n>>")
	merged=open(output, 'w')
	for lin in t:
		merged.writelines('\t'.join(lin)+'\n')
	merged.close()

if len(argv)>1:
	merge(argv)