import pandas as pd
import mysql.connector as cn
import os


def main():

    "Source 1: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html "
    " Test 1: 1 database"

    # Database info
    # Sources:
        # 1. AWS
        # 2. http://datascience-enthusiast.com/R/AWS_RDS_R_Python.html

    host = "proteinfamilydb.c36zan5mzgot.us-west-2.rds.amazonaws.com:3306"
    port = 3306
    dbname = "serineProtease"
    username = "miskovitz"
    password = "PineCoffee18"

    # Connect
    conn = cn.connect(host=host, username=username,port=port,password=password, db=dbname)



    pdbs = ["4hoh", "1a0j", "2hhz", "1as0","1a4s"]
    d = {"name": [0,1,0,0,1], "res":[0,1,0,0,1], "chainID":[1,2,4,3,2],
         "x":[23.4,68.4,-98.5,0.04, 102.1], "y": [43.4,61.4,98.5,90.04, .021], "z": [-3.4,1.4,-985.5,190.04, 50.021],
         "ocupancy":[-23.4,108.4,-9.5,0.04, 10.1], "tempFact": [2.4,23.4,-50.5,9.04, 22.1]}
    a = pd.DataFrame(d,pdbs)

    a.to_sql()

    path = 'C:/Users/Brianna/PyCharmProjects/optimizer/TestingDB/'

    if not os.path.exists(path):
        os.makedirs(path)
    file = path + 'test1.pkl'
    a.to_pickle(file)

if __name__ == '__main__':
    main()