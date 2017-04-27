
import csv
from datetime import datetime

def main():
    print('main')
    file = '/Users/cindy.wang/Downloads/Children_Forecast_2017_Toys_Apr14.csv'
    writer = open('/Users/cindy.wang/Downloads/forecast_0415_0421.csv', 'w')

    start_date = datetime.strptime('4/15/17', '%m/%d/%y')
    end_date = datetime.strptime('4/21/17', '%m/%d/%y')

    holiday_promotion_dict = {}
    with open(file, 'rb') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            sku = row['skuseq']
            date = datetime.strptime(row['date'], '%m/%d/%Y') if row['date'] != '' else datetime.today()
            if date >= start_date and date <= end_date:
                if sku not in holiday_promotion_dict:
                    holiday_promotion_dict[sku] = 0
                holiday_promotion_dict[sku] += float(row['forecast'])

    for key, value in holiday_promotion_dict.iteritems() :
        writer.write(key + ',' + str(value/7) + '\n')

if __name__ == '__main__': main()