namenumbers=[16,17,18,28,29,30,40,41,42,43,52,53,54,55,65,66,67,68,76,79,89,90,91,93]
namenumbers2=[100,101,102,115,124,125,137,138,149,150,160,161,173,174,184,185,186,196,197,198,208,215,217,219,220,221,232,233,243,244,245,255,256,267,279,280,290,291,292]
for i in namenumbers:
	num = str(i)
	filename='b200'+ num +'_ctd'
	f = open(filename+'.csv','rb')
	fo = open(filename+'out.csv','wb')
	# go through each line of the file
	for line in f:
	    bits = line.split(',')
	    # change second column
	    if bits == '-9.99':
	    	bits = '"input"'
	    # join it back together and write it out
	    fo.write( ','.join(bits) )

	f.close()
	fo.close()

for i in namenumbers2:
	num = str(i)
	filename='b20'+ num +'_ctd'
	f = open(filename+'.csv','rb')
	fo = open(filename+'out.csv','wb')
	# go through each line of the file
	for line in f:
	    bits = line.split(',')
	    # change second column
	    if bits == '-9.99':
	    	bits = '"input"'
	    # join it back together and write it out
	    fo.write( ','.join(bits) )

	f.close()
	fo.close()