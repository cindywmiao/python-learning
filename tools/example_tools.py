import os

readFileName = '/Users/cindy.wang/Downloads/result-21-days-seoul.csv'
path = '/Users/cindy.wang/Downloads'
def getList():
    mylist = list()
    if (os.path.exists(readFileName)):
        reader = open(readFileName, 'r')
        for line in reader:
            str = line.split(",")
            mode = str[-5]
            if mode not in mylist:
                mylist.append(mode)
    return mylist

def getSku(mode):
    writeFileName = '%s/%s.csv' % (path, mode)
    if(os.path.exists(readFileName)):
        reader = open(readFileName, 'r')
        writer = open(writeFileName, 'w')
        for line in reader:
            str = line.split(",")
            if mode == str[-5]:
                writer.write(line)


def main():
    mylist = getList()
    for mode in mylist:
        getSku(mode)

if __name__ == '__main__':
    main()