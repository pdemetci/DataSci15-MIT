for i in range(1,4):
	num = str(i)
	filename='b5000'+ num +'_ctd'
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

for i in range(5,10):
	num = str(i)
	filename='b5000'+ num +'_ctd'
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

for i in range(10,25):
	num = str(i)
	filename='b500'+ num +'_ctd'
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

for i in range(26,43):
	num = str(i)
	filename='b500'+ num +'_ctd'
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

for i in range(44,49):
	num = str(i)
	filename='b500'+ num +'_ctd'
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