import utils as util
import csv
from datetime import timedelta, datetime
import os

workspace = '/Users/cindy.wang/Downloads/Archive/'
hdfs_path = '/user/mercury/scm-output/scm_forecast_demand_forecast/'

def upload(target_date):
    with open(workspace + target_date + '_result.csv', 'r') as reader:
        for line in reader:
            strs = line.split(',')
            if len(strs) != 57:
                print(line)

    util.upload_file(workspace + target_date + '_result.csv', hdfs_path + 'children-holiday/' +
                     datetime.strptime(target_date, '%Y-%m-%d').strftime('%Y%m%d') + '/result-21-days-national.csv')

def main():
    start_date = datetime.strptime('20170416', '%Y%m%d')
    for i in range(0, 1):
        target_date = start_date + timedelta(days=i)
        upload(target_date.strftime('%Y-%m-%d'))

if __name__ == '__main__': main()