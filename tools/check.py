import csv
from datetime import timedelta, datetime, date

readFileName = '/Users/cindy.wang/Downloads/part-00000'
reader = open(readFileName, 'r')
for line in reader:
    str = line.split(",")
    start_date=str[4]
    end_date=str[5]
    start_date_object = datetime.strptime(start_date, "%Y%m%d")
    end_date_object = datetime.strptime(end_date, "%Y%m%d")
    gap = int((end_date_object - start_date_object).days)
    if len(str) - gap - 7 is not 0:
        print("sku : %s, start_date : %s, end_date : %s, len : %s %s" % (str[0], start_date, end_date, len(str), len(str) - gap - 7))
    #print(len(str))

