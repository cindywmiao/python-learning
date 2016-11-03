import csv
import itertools
import string

def count(filename):
    c = 0
    with open(filename, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for line in reader:
            c += 1
    return c

def diff(filename1, filename2):
    count = 0
    with open(filename1, "rb") as f1:
        with open(filename2, "rb") as f2:
            reader1 = csv.reader(f1, delimiter="\t")
            reader2 = csv.reader(f2, delimiter="\t" )
            for line1, line2 in itertools.izip(reader1, reader2):
                if line1 != line2:
                    strs1 = string.split(line1[0], ",")
                    strs2 = string.split(line2[0], ",")
                    if strs1[0] == strs2[0]:
                        for item1, item2 in itertools.izip(strs1, strs2):
                            if(item1 != item2):
                                break
                        #print(strs1[0])
                        count += 1
    print "count : ----------------------------------"
    print count

daegu = "/Users/cindy.wang/Downloads/result-21-days-daegu.csv"
seoul = "/Users/cindy.wang/Downloads/result-21-days-seoul.csv"
national = "/Users/cindy.wang/Downloads/result-21-days-national.csv"

daegu_raw = "/Users/cindy.wang/Downloads/result-21-days-daegu-raw.csv"
seoul_raw = "/Users/cindy.wang/Downloads/result-21-days-seoul-raw.csv"
national_raw = "/Users/cindy.wang/Downloads/result-21-days-national-raw.csv"

#diff(daegu, national)
#diff(daegu_raw, national_raw)
diff(seoul_raw, national_raw)