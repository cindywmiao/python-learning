import csv
from datetime import timedelta, datetime

workspace = '/Users/cindy.wang/Downloads/Archive/'
def main():
    print('main')

    target_date = '2017-04-03'
    file_name =  workspace + 'child.sku.' + target_date + '.forecast.csv'
    result = {}
    with open(file_name, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['skuseq'] not in result:
                result[row['skuseq']] = {}
            result[row['skuseq']][row['date']] = row['forecast']

    output_file = workspace + 'child.sku.output.' + target_date + '.forecast.csv'
    writer = open(output_file, 'w')

    for key, value in result.items():
        start_date = datetime.strptime(target_date, '%Y-%m-%d')
        writer.write(key)
        for i in range(0, 21):
            current_date = start_date + timedelta(days=i)
            writer.write(',' + "%.2f" % float(value[current_date.strftime('%Y-%m-%d')]))
        writer.write('\n')







if __name__ == '__main__': main()