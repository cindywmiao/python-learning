
workspace = '/Users/cindy.wang/Downloads/'
def main():

    writer = open(workspace + 'uplift_input.csv', 'w')
    writer.write('Unit,Category,SKUSEQ,Starting Date,Ending Date,Uplift(%),Reason\n')

    holiday_promotion_file = workspace + 'forecast_0415_0421.csv'
    holiday_promotion_dict = {}
    with open(holiday_promotion_file, 'r') as reader:
        for line in reader:
            strs = line.split(',')
            holiday_promotion_dict[strs[0]] = float(strs[1])

    with open(workspace + 'result-21-days-national.csv', 'r') as reader2:
        for line in reader2:
            strs = line.split(',')
            sku = strs[0]
            if sku in holiday_promotion_dict:
                unit = strs[2]
                category = strs[3]
                forecast_d2 = float(strs[5])
                forecast_d3 = float(strs[6])
                forecast_d4 = float(strs[7])
                forecast_d5 = float(strs[8])
                forecast_d6 = float(strs[9])
                forecast_d7 = float(strs[10])
                forecast_d8 = float(strs[11])

                baseline = (forecast_d2 + forecast_d3 + forecast_d4 + forecast_d5 + forecast_d6 + forecast_d7 + forecast_d8)/7
                if baseline != 0 and holiday_promotion_dict[sku] != 0:
                    uplift = (holiday_promotion_dict[sku]-baseline) / baseline
                    writer.write(unit + ',' + category + ',' + sku + ',' + '20170415,' + '20170421,' + str(round(uplift*100)) + '%,Children Holiday\n')


if __name__ == '__main__': main()