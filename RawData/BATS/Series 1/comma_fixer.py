with open("b10001_ctd.txt", 'r') as f:
    with open("b10004_ctd1out.csv", 'w') as t:
        for line in f:
            new_line = line.replace(",,",",")
            new_line = line.replace(",,,",",")
            new_line = line.replace(",,,,",",")
            new_line = line.replace(",,,,,",",")
            t.write(new_line)