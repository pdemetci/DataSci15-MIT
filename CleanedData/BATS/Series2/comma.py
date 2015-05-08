import csv
for i in [16,17,18,28,29,30,40,41,42,43,52,53,54,55,65,66,67,68,76,79,89,90,91,93]:
	num=str(i)
	filename= 'b200'+num
	with open(filename+'.csv', 'r') as f:
	    with open(filename+'wwneww.txt', 'w') as t:
	    	content=f.read()
	    	for line in content:
				bits = line.split(',')
				if bits != '':
					t.write( ','.join(bits) )

	f.close()
	t.close()