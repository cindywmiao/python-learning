import pyhs2

with pyhs2.connect(host='10.10.129.141',
               port=11000,
               authMechanism="PLAIN",
               user='mercury',
               password='mercury1234',
               database='mercury') as conn:
    with conn.cursor() as cur:
        #Show databases
        print cur.getDatabases()

        # #Execute query
        # cur.execute("select * from mercury.daily_forecast_input where dt='20170102' and unitedskuseq='2165017' and area='seoul'")
        #
        # #Return column info from query
        # print cur.getSchema()
        #
        # #Fetch table results
        # for i in cur.fetch():
        #     print i