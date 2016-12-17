import os
areas = 'seoul,national,daegu'
file_path = '/Users/cindy.wang/Downloads/'


def count(reader):
    c = 0
    for line in reader:
        c += 1
    return c


def main():
    #for area in areas.split(','):
        #command="sort %sresult-21-days-%s.csv >> %s%s" % (file_path, area, file_path, area)
        #os.system(command)

    readers = dict()
    for area in areas.split(','):
        readers[area] = open("%s%s" % (file_path, area), 'r')

    print(count(readers['seoul']))
    print(count(readers['national']))
    print(count(readers['daegu']))

if __name__ == '__main__':main()