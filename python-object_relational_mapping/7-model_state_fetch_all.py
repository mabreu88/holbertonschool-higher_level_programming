#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the\
    states table of hbtn_0e_0_usa where name matches the argument. """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.
    format(
        argv[1], 
        argv[2], 
        argv[3])
