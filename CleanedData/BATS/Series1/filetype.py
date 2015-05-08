import csv
for i in [10,11]:
	num=str(i)
	filename= 'b100'+num
	f = open(filename+'_ctdout.csv','rb')
	fo = open(filename+'.txt','wb')
	content=f.read()
	fo.write(content)


# for i in range(13, 100):
# 	num=str(i)
# 	filename= 'b100'+num
# 	f = open(filename+'_ctdout.csv','rb')
# 	fo = open(filename+'.txt','wb')
# 	content=f.read()
# 	fo.write(content)
# for i in range(100, 145):
# 	num=str(i)
# 	filename= 'b10'+num
# 	f = open(filename+'_ctdout.csv','rb')
# 	fo = open(filename+'.txt','wb')
# 	content=f.read()
# 	fo.write(content)
# for i in range(146, 160):
# 	num=str(i)
# 	filename= 'b10'+num
# 	f = open(filename+'_ctdout.csv','rb')
# 	fo = open(filename+'.txt','wb')
# 	content=f.read()
# 	fo.write(content)
# for i in range(161, 305):
# 	num=str(i)
# 	filename= 'b10'+num
	# f = open(filename+'_ctdout.csv','rb')
	# fo = open(filename+'.txt','wb')
	# content=f.read()
	# fo.write(content)

	# use 'with' if the program isn't going to immediately terminate
	# so you don't leave files open
	# the 'b' is necessary on Windows
	# it prevents \x1a, Ctrl-z, from ending the stream prematurely
	# and also stops Python converting to / from different line terminators
	# On other platforms, it has no effect
	
	# out_csv = csv.writer(open(csv_file, 'wb'))

	# out_csv.writerows(in_txt)