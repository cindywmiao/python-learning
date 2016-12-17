import csv
from datetime import timedelta, datetime, date

readFileName = '/Users/cindy.wang/Downloads/test'
reader = open(readFileName, 'r')

start_date = '20161017'
end_date = '20161123'

count = 0
for line in reader:
    str = line.split(",")
    if (datetime.strptime(str[0], '%Y%m%d') - datetime.strptime(start_date, '%Y%m%d')).days is not count:
        print(line)
    count += 1

