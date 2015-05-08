import csv
for i in [16,17,18,28,29,30,40,41,42,43,52,53,54,55,65,66,67,68,76,79,89,90,91,93]:
	num=str(i)
	filename= 'b200'+num
	f = open(filename+'_ctdout.csv','rb')
	fo = open(filename+'.txt','wb')
	content=f.read()
	fo.write(content)
for i in[100,101,102,115,124,125,137,138,149,150,160,161,173,174,184,185,186,196,197,198,208,215,217,219,220,221,232,233,243,244,245,255,256,267,279,280,290,291,292]:
	num=str(i)
	filename= 'b20'+num
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