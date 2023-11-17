import pandas as pd
from load_csv import load

def load(path: str) -> Dataset:
    '''takes a path as argument, writes the dimensions of the data set
and returns it.'''


if __name__ == "__main__":
    print(load("life_expectancy_years.csv"))