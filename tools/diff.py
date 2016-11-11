import csv
import itertools
import string

filename1 = "/Users/cindy.wang/Downloads/new"
filename2 = "/Users/cindy.wang/Downloads/old"

test1 = "/Users/cindy.wang/Downloads/old/test.csv"
test2 = "/Users/cindy.wang/Downloads/new/test.csv"


with open(filename1, "rb") as f1:
    with open(filename2, "rb") as f2:
        reader1 = csv.reader(f1, delimiter="\t")
        reader2 = csv.reader(f2, delimiter="\t" )
        for line1, line2 in itertools.izip(reader1, reader2):
            if line1 != line2:
                strs1 = string.split(line1[0], ",")
                strs2 = string.split(line2[0], ",")
                for item1, item2 in itertools.izip(strs1, strs2):
                    if(item1 != item2 and abs(float(item1) - float(item2)) > 0.000011):
                        print(strs1[0])