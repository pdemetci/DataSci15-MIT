
num = str(99)
filename='b100'+ num +'_ctd'
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
