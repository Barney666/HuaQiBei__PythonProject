import sys
import pandas as pd

def findName():
    # stock="600100"
    # file=pd.read_csv("Name_Code2.csv")
    stock=sys.argv[1]
    file=pd.read_csv(sys.argv[2])
    count=0
    for code in file['Code']:
        if(int(stock)==code):  #code是int类型
            break
        count+=1
    name=file['Name'][count]
    print(name)
    # print(1)



if __name__=="__main__":
    findName()