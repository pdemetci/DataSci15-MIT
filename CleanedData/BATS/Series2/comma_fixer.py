import csv
for i in [16,17,18,28,29,30,40,41,42,43,52,53,54,55,65,66,67,68,76,79,89,90,91,93]:
	num=str(i)
	filename= 'b200'+num
	with open(filename+'.txt', 'r') as f:
	    with open(filename+'new.txt', 'w') as t:
	    	content=f.read()
	        for line in content:
	        	line=str(line)
	        	print type(line)
	        	for a in len(line):
		        	if line[a:a+1]==',,':
		        		line[a:a+1]=','
		        	if line[a:a+2]==',,,':
		        		line[a:a+2]=','
		        	if line[a:a+3]==',,,,':
		        		line[a:a+3]=','
		        	if line[a:a+4]==',,,,,':
		        		line[a:a+4]=','
		           	t.write(line)
# for i in[100,101,102,115,124,125,137,138,149,150,160,161,173,174,184,185,186,196,197,198,208,215,217,219,220,221,232,233,243,244,245,255,256,267,279,280,290,291,292]:
# 	num=str(i)
# 	filename= 'b20'+num
# 	with open(filename+'.txt', 'r') as f:
# 	    with open(filename+'new.txt', 'w') as t:
# 	        for line in f:
# 	        	for a in line:
# 	        		new_line = a.replace(",,",",")
# 	        		new_line = a.replace(",,,",",")
# 	        		new_line = a.replace(",,,,",",")
# 	        		new_line = a.replace(",,,,,",",")
# 	        		t.write(new_line)
# for i in range(13, 100):
# 	num=str(i)
# 	filename= 'b100'+num
# 	with open(filename+'.txt', 'r') as f:
# 	    with open(filename+'.csv', 'w') as t:
# 	        for line in f:
# 	            new_line = line.replace(",,",",")
# 	            new_line = line.replace(",,,",",")
# 	            new_line = line.replace(",,,,",",")
# 	            new_line = line.replace(",,,,,",",")
# 	            t.write(new_line)

# for i in range(100, 145):
# 	num=str(i)
# 	filename= 'b10'+num
# 	with open(filename+'.txt', 'r') as f:
# 	    with open(filename+'.csv', 'w') as t:
# 	        for line in f:
# 	            new_line = line.replace(",,",",")
# 	            new_line = line.replace(",,,",",")
# 	            new_line = line.replace(",,,,",",")
# 	            new_line = line.replace(",,,,,",",")
# 	            t.write(new_line)
# for i in range(146, 160):
# 	num=str(i)
# 	filename= 'b10'+num
# 	with open(filename+'.txt', 'r') as f:
# 	    with open(filename+'.csv', 'w') as t:
# 	        for line in f:
# 	            new_line = line.replace(",,",",")
# 	            new_line = line.replace(",,,",",")
# 	            new_line = line.replace(",,,,",",")
# 	            new_line = line.replace(",,,,,",",")
# 	            t.write(new_line)
# for i in range(161, 305):
# 	num=str(i)
# 	filename= 'b10'+num
# 	with open(filename+'.txt', 'r') as f:
# 	    with open(filename+'.csv', 'w') as t:
# 	        for line in f:
# 	            new_line = line.replace(",,",",")
# 	            new_line = line.replace(",,,",",")
# 	            new_line = line.replace(",,,,",",")
# 	            new_line = line.replace(",,,,,",",")
# 	            t.write(new_line)
