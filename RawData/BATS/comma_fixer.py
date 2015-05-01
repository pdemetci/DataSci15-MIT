with open("b10004_ctd.csv", 'r') as f:
    with open("b10004_ctd3.csv", 'w') as t:
        for line in f:
            new_line = line.replace(",,",",")
            t.write(new_line)