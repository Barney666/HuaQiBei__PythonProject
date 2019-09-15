import sys
import pandas as pd

def findCode():
    # stock="同方股份"
    # file=pd.read_csv("Name_Code2.csv")
    stock=sys.argv[1]
    file=pd.read_csv(sys.argv[2])
    count=0
    for name in file['Name']:
        if(stock==name):  #code是int类型
            break
        count+=1
    code=file['Code'][count]
    print(code)
    # print(1)



if __name__=="__main__":
    findCode()