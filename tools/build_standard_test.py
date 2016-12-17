import csv
import string

def build_standard_test(source, dist):
    c = 0
    with open(source) as file1:
        with open(dist, 'w') as file2:
            reader = csv.reader(file1, delimiter=",")
            writer = csv.writer(file2, delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for line in reader:
                flag = False
                for i in range(6, len(line)):
                    if line[i] != "0;0;0" :
                        print(line[i])
                        flag = True;
                        break

                if flag:
                    writer.writerow(line)
                    c += 1

                if c >= 20:
                    break
    return c


reader="/Users/cindy.wang/Workplace/demand-forecast/resources/part.csv"
writer="/Users/cindy.wang/Workplace/demand-forecast/resources/test.csv"
print(build_standard_test(reader, writer))
