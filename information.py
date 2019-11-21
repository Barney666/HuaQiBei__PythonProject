import sys
import pandas as pd

def information():
    # code="600100"
    # num="3"


    file=pd.read_csv(sys.argv[1],encoding='gbk',header=None)

    print(file.values.tolist())

if __name__ == '__main__':
    information()