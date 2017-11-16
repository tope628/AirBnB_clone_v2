#!/usr/bin/python3
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

user = 'hbnb_dev'
passwd = 'hbnb_dev_pwd'
host = 'localhost'
db = 'hbnb_dev_db'


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                user, passwd, host, db))
    print("connection success!")
