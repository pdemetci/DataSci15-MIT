for i in [1,2,3,4,5,7]:
	num=str(i)
	filename= 'b1000'+num
	with open(filename+'.txt', 'r') as f:
	    with open(filename+'.csv', 'w') as t:
	        for line in f:
	            new_line = line.replace(",,",",")
	            new_line = line.replace(",,,",",")
	            new_line = line.replace(",,,,",",")
	            new_line = line.replace(",,,,,",",")
	            t.write(new_line)

for i in [10,11]:
	num=str(i)
	filename= 'b100'+num
	with open(filename+'.txt', 'r') as f:
	    with open(filename+'.csv', 'w') as t:
	        for line in f:
	            new_line = line.replace(",,",",")
	            new_line = line.replace(",,,",",")
	            new_line = line.replace(",,,,",",")
	            new_line = line.replace(",,,,,",",")
	            t.write(new_line)

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
