readFileName = '../socnts.csv'
writeFileName = '../write.csv'

reader = open(readFileName, 'r')
writer = open(writeFileName, 'w')

for line in reader:
    writer.write("%s,20161101\n"%line[:-1])