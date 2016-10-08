import sys

def main(): # passing parameters from command line
    args = sys.argv
    input_file = args[1]
    mode = args[2]
    area = args[3]
    result_output_file = args[4]
    result_output_file_uplift = args[5]
    target_date = args[6]
    target_days = int(args[7])
    cores = int(args[8])
    chunk_size = int(args[9])
    print input_file
    print mode
    print area
    print result_output_file
    print result_output_file_uplift
    print target_date
    print target_days
    print cores
    print chunk_size
    #mc_predict_skus(input_file, mode, area, result_output_file, result_output_file_uplift, target_date, target_days, cores, chunk_size)


if __name__ == '__main__': main()