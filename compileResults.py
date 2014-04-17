print "CompileResults_Juan"
print "This file will take an index file (format <sample_ID>\t<MS_long_name>)"
print "and browse the current folder with MS search results to generate "
print "a single output file with the concatenated results and corrected"
print "sample ID tags"

from sys import argv
import os

print "Usage: CompileResults_Juan.py <index_filename> <output_filename>"

#Read index file
ind=open(argv[1], 'r')
output=open(argv[2], 'w')

index=[]

for line in ind:
	s= line.split('\t')[0], line.rstrip('\n').split('\t')[1]
	index.append(s)
ind.close()

merged_ok=0
errors=0

#Traverses index
for line in index:
	c=0
	exp=line[1]+'_ITMSms2cid-results' #opens folder withreport file
	res_path=os.path.join(exp, 'report.txt')
	#print "Merging", res_path
	
	try: #If file not found or any other error found, still carry on
		exp_f=open(res_path, 'r')
		for e in exp_f:
			if merged_ok==0 and c==2:
				output.write(e)
			c+=1
			if c>3:
				l=e.split('\t')
				l[0]=line[0]
				output.write('\t'.join(l))
		merged_ok+=1
		exp_f.close()
	except:
		print "Error (probably file not found?)"
		errors+=1
		continue

output.close()

print merged_ok, " files were merged successfully"
print errors, " files could not be merged properly"