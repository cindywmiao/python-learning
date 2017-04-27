import argparse

executor_parser = argparse.ArgumentParser(description='Forecast System Executor')
executor_parser.add_argument('-f', '--file', required=True)
executor_parser.add_argument('-a', '--area', required=True)
executor_parser.add_argument('-d', '--date', required=True)
executor_parser.add_argument('-m', '--mode', required=True)
executor_parser.add_argument('-i', '--input_path', required=True)
executor_parser.add_argument('-o', '--output_path', required=False)
executor_parser.add_argument('-c', '--config_file', required=True)
executor_parser.add_argument('-t', '--config_type', required=True)

driver_parser = argparse.ArgumentParser(description='Forecast System Driver')
driver_parser.add_argument('-w', '--workflow', required=True)
driver_parser.add_argument('-a', '--areas', required=True)
driver_parser.add_argument('-d', '--date', required=True)
driver_parser.add_argument('-i', '--input_path', required=False)
driver_parser.add_argument('-o', '--output_path', required=False)
driver_parser.add_argument('-c', '--config_file', required=True)
driver_parser.add_argument('-t', '--config_type', required=True)

maple_parser = argparse.ArgumentParser(description='Forecast System Maple')
maple_parser.add_argument('-a', '--areas', required=True)
maple_parser.add_argument('-d', '--date', required=True)

## step 2
forecast_input_gathering_driver_parser = argparse.ArgumentParser(description='Forecast System Input Gathering')
forecast_input_gathering_driver_parser.add_argument('-w', '--workflow_id', required=True)
forecast_input_gathering_driver_parser.add_argument('--workspace', required=True)
forecast_input_gathering_driver_parser.add_argument('--tempTable', required=True)
forecast_input_gathering_driver_parser.add_argument('--start_date', required=False)
forecast_input_gathering_driver_parser.add_argument('--end_date', required=False)
forecast_input_gathering_driver_parser.add_argument('--target_date', required=False)

## step 3
forecast_area_partition_driver_parser = argparse.ArgumentParser(description='Forecast System Area Partition')
forecast_area_partition_driver_parser.add_argument('-w', '--workflow_id', required=True)
forecast_area_partition_driver_parser.add_argument('--sourceroot', required=True)
forecast_area_partition_driver_parser.add_argument('--workspace', required=True)
forecast_area_partition_driver_parser.add_argument('--start_date', required=False)
forecast_area_partition_driver_parser.add_argument('--end_date', required=False)
forecast_area_partition_driver_parser.add_argument('--target_date', required=False)

## step4
forecast_driver_parser = argparse.ArgumentParser(description='Forecast System Forecast Driver')
forecast_driver_parser.add_argument('-w', '--workflow_id', required=True)
forecast_driver_parser.add_argument('-i', '--input_file', required=True)
forecast_driver_parser.add_argument('-o', '--output_file', required=True)
forecast_driver_parser.add_argument('--config_file', required=True)
forecast_driver_parser.add_argument('--config_type', required=True)
forecast_driver_parser.add_argument('-a', '--areas', required=True)
forecast_driver_parser.add_argument('--start_date', required=False)
forecast_driver_parser.add_argument('--end_date', required=False)
forecast_driver_parser.add_argument('--target_date', required=False)