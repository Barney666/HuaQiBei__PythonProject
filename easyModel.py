import csv
import xlrd
import os
import sys

List_a = []
List_by = []
List1 = []
List2 = []
List3 = []
a = 0
risk_grade = [a for i in range(50)]
risk_type = [a for i in range(50)]

# string_code = sys.argv[1]
# same_company = sys.argv[2]
# zcfzb = sys.argv[3]
# lrb = sys.argv[4]
# zysjb = sys.argv[5]
# xjllb = sys.argv[6]
string_code = "600100"

same_company = "15.xlsx"
zcfzb = "1"
lrb = "2"
zysjb = "3"
xjllb = "4"
score_of_Macro_environment = 7
score_Meso_environment = 9
score_of_Supervisory_authority = 10

csv1a = zcfzb + "\\" + string_code + ".csv"
csv2a = lrb + "\\" + string_code + ".csv"
csv3a = zysjb + "\\" + string_code + ".csv"
csv4a = xjllb + "\\" + string_code + ".csv"
if os.path.exists(csv1a) == False or os.path.exists(csv2a) == False or os.path.exists(
        csv3a) == False or os.path.exists(csv4a) == False:
     print("wrong")

def contain(code):
    code2 = len(str(code))
    re = False
    cj = 6 - code2
    while cj > 0:
        code = "0" + str(code)
        cj = cj - 1

    csv1_code = zcfzb + "\\" + str(code) + ".csv"
    csv2_code = lrb + "\\" + str(code) + ".csv"
    csv3_code = zysjb + "\\" + str(code) + ".csv"
    csv4_code = xjllb + "\\" + str(code) + ".csv"
    if os.path.exists(csv1_code) == True and os.path.exists(csv2_code) == True and os.path.exists(csv3_code)==True and os.path.exists(csv4_code) == True:
       re = True
    return re

def tz(data):
    ct = 0
    for i in range(len(data)):
        if data[i] == 0:
            ct = ct + 1

    for i in range(ct):
        data.remove(0)
    return data


def median(data1):
    data = tz(data1)
    data.sort()
    if data == []:
        data = [0]

    if len(data) == 1:
        med = data[0]
    elif len(data) % 2 == 0:
        med = data[len(data) // 2] + data[len(data) // 2 - 1]
    else:
        med = data[len(data) // 2]
    return med


csv1 = zcfzb + "\\" + string_code + ".csv"
csv2 = lrb + "\\" + string_code + ".csv"
csv3 = zysjb + "\\" + string_code + ".csv"
csv4 = xjllb + "\\" + string_code + ".csv"

string = string_code
list_hy = []
data = xlrd.open_workbook(same_company)
table = data.sheets()[0]
nrows = table.nrows
name_before = ''
count = -1
list_t = []
list_hname = []





for i in range(nrows):
    row = table.row_values(i)
    if row[2] != '':
        if row[2] != name_before:
            name_before = row[2]
            list_hname.append(0)
            list_hname[count] = row[2]
            list_hy.append(0)
            count = count + 1
            if count != 0:
                list_hy[count] = list_t
            list_t = []
            cou = 0

    if contain(int(row[3])) == True:
        list_t.append(0)
        list_t[cou] = int(row[3])
        cou = cou + 1
list_hy.append(0)
count = count + 1
list_hy[count] = list_t


for i in range(len(list_hy)):
    if i != 0:
        for j in range(len(list_hy[i])):
            if list_hy[i][j] == int(string):
                catch = i



for k in range(len(list_hy[catch])):

    count_k = 0

    strnow = list_hy[catch][k]
    strl = 1
    strnow2 = len(str(strnow))

    cj = 6 - strnow2
    while cj > 0:
        strnow = "0" + str(strnow)

        cj = cj - 1

    csv1o = zcfzb + "\\" + str(strnow) + ".csv"
    csv2o = lrb + "\\" + str(strnow) + ".csv"
    csv3o = zysjb + "\\" + str(strnow) + ".csv"
    csv4o = xjllb + "\\" + str(strnow) + ".csv"
    with open(csv1o, 'r', encoding='gbk') as csvfile:

        reader = csv.reader(csvfile)
        for i, rows in enumerate(reader):
            List_by.append(0)
            row = rows
            name_of_this = row[0]

            if name_of_this == "固定资产(万元)":
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]

                if row[1] != '--':
                    Fixed_assets = int(row[1])
                else:
                    Fixed_assets = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Fixed_assets
                count_k = count_k + 1

            if name_of_this == "应收账款(万元)":
                if k == 0:
                    List_by.append(0)

                    List_by[count_k] = [range(len(list_hy[catch]))]

                if row[1] != '--':
                    Accounts_receivable = int(row[1])
                else:
                    Accounts_receivable = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Accounts_receivable
                count_k = count_k + 1

            if name_of_this == "其他应收款(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Other_receivable = int(row[1])
                else:
                    Other_receivable = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Other_receivable
                count_k = count_k + 1

            if name_of_this == "预付账款(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Advances_to_suppliers = int(row[1])
                else:
                    Advances_to_suppliers = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Advances_to_suppliers
                count_k = count_k + 1

            if name_of_this == "资产总计(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Total_assets = int(row[1])
                else:
                    Total_assets = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Total_assets
                count_k = count_k + 1

            if name_of_this == "流动资产合计(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Current_assets = int(row[1])
                else:
                    Current_assets = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Current_assets
                count_k = count_k + 1

            if name_of_this == "流动负债合计(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    current_liabilities = int(row[1])
                else:
                    current_liabilities = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = current_liabilities
                count_k = count_k + 1

            if name_of_this == "固定资产原值(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Primary_Value_of_Fixed_Assets = int(row[1])
                else:
                    Primary_Value_of_Fixed_Assets = 0

                List_by[count_k].append(0)
                List_by[count_k][k] = Primary_Value_of_Fixed_Assets
                count_k = count_k + 1

            if name_of_this == "累计折旧(万元)":
                # print(i)

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Depreciation_expenses = int(row[1])
                else:
                    Depreciation_expenses = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Depreciation_expenses
                count_k = count_k + 1

            if name_of_this == "在建工程(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Construction_in_progress = int(row[1])
                else:
                    Construction_in_progress = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Construction_in_progress
                count_k = count_k + 1

            if name_of_this == "存货(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Stock = int(row[1])
                else:
                    Stock = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Stock
                count_k = count_k + 1

            if name_of_this == "货币资金(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]

                if row[1] != '--':
                    Monetary_funds = int(row[1])
                else:
                    Monetary_funds = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Monetary_funds
                count_k = count_k + 1

            # number_of_whh_cb = input("Please input 财报问询函数目")
            # number_of_whh_cz = input("Please input 重组问询函数目")
            # number_of_whh_other = input("Please input 其他问询函数目")
            # number_of_jsh = input("Please input 警示函数目")
            # number_of_ladc = input("Please input 违规与立案数目")
            # Money_for_fixed_assets_and_others = input("Please input 投资固定资产无形资产及其他的金额")

            # Long_term_liabilities_one_year = input("Please input 一年内到期的非流动负债(万元)")
            if name_of_this == "一年内到期的非流动负债(万元)":
                # print(i)

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Long_term_liabilities_one_year = int(row[1])
                else:
                    Long_term_liabilities_one_year = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Long_term_liabilities_one_year
                count_k = count_k + 1

            # Dutiable_fees = input("Please input 应交税费")
            if name_of_this == "应交税费(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Dutiable_fees = int(row[1])
                else:
                    Dutiable_fees = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Dutiable_fees
                count_k = count_k + 1

            # Engineering_materials = input("Please input 工程物资")
            if name_of_this == "工程物资(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Engineering_materials = int(row[1])
                else:
                    Engineering_materials = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Engineering_materials
                count_k = count_k + 1

            # Accounts_payable = input("Please input 应付账款")
            if name_of_this == "应付账款(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Accounts_payable = int(row[1])
                else:
                    Accounts_payable = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Accounts_payable
                count_k = count_k + 1

            # Notes_payable = input("Please input 应付票据")
            if name_of_this == "应付票据(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Accounts_payable2 = int(row[1])
                else:
                    Accounts_payable2 = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Accounts_payable2
                count_k = count_k + 1

            # Total_liabilities = input("Please input 总负债")负债合计(万元)
            if name_of_this == "负债合计(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Total_liabilities = int(row[1])
                else:
                    Total_liabilities = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Total_liabilities
                count_k = count_k + 1

            # Goodwill = input("Please input 商誉")
            if name_of_this == "商誉(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Goodwill = int(row[1])
                else:
                    Goodwill = 0

                List_by[count_k].append(0)
                List_by[count_k][k] = Goodwill
                count_k = count_k + 1

            # Short_term_borrowing = input("Please input 短期借款")
            if name_of_this == "短期借款(万元)":
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Short_term_borrowing = int(row[1])
                else:
                    Short_term_borrowing = 0

                List_by[count_k].append(0)
                List_by[count_k][k] = Short_term_borrowing
                count_k = count_k + 1

            # long_term_borrowing = input("Please input 长期借款")
            if name_of_this == "长期借款(万元)":
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    long_term_borrowing = int(row[1])
                else:
                    long_term_borrowing = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = long_term_borrowing
                count_k = count_k + 1

            # Other_Liquidity_Liabilities = input("Please input 其他流动性负债")
            if name_of_this == "其他流动负债(万元)":
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Other_Liquidity_Liabilities = int(row[1])
                else:
                    Other_Liquidity_Liabilities = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Other_Liquidity_Liabilities
                count_k = count_k + 1

            # Bonds_payable = input("Please input 应付债券")
            if name_of_this == "应付债券(万元)":
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Bonds_payable = int(row[1])
                else:
                    Bonds_payable = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Bonds_payable
                count_k = count_k + 1

            # Asset_structure = input("Please input 企业资产结构")

            if name_of_this == "实收资本(或股本)(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Asset_structure = int(row[1])
                else:
                    Asset_structure = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Asset_structure
                count_k = count_k + 1

            if name_of_this == "资本公积(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Capital_reserve = int(row[1])
                else:
                    Capital_reserve = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Capital_reserve
                count_k = count_k + 1

            if name_of_this == "盈余公积(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Surplus_reserve = int(row[1])
                else:
                    Surplus_reserve = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Surplus_reserve
                count_k = count_k + 1

            if name_of_this == "未分配利润(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Undistributed_profits = int(row[1])
                else:
                    Undistributed_profits = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Undistributed_profits
                count_k = count_k + 1

            if name_of_this == "预收账款(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Advances_from_customers = int(row[1])
                else:
                    Advances_from_customers = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Advances_from_customers
                count_k = count_k + 1

    with open(csv2o, 'r', encoding='gbk') as csvfile2:
        reader2 = csv.reader(csvfile2)
        for i, rows in enumerate(reader2):
            row = rows
            name_of_this = row[0]

            if name_of_this == "营业收入(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Main_Business_Income = int(row[1])
                else:
                    Main_Business_Income = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Main_Business_Income
                count_k = count_k + 1

            if name_of_this == "营业成本(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Main_Business_Cost = int(row[1])
                else:
                    Main_Business_Cost = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Main_Business_Cost
                count_k = count_k + 1

            if name_of_this == "其他业务收入(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = []
                if row[1] != '--':
                    Other_Business_Income = int(row[1])
                else:
                    Other_Business_Income = 0

                List_by[count_k].append(0)

                List_by[count_k][k] = Other_Business_Income
                count_k = count_k + 1

            if name_of_this == "营业外收入(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Out_of_business_income = int(row[1])
                else:
                    Out_of_business_income = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Out_of_business_income
                count_k = count_k + 1

            if name_of_this == "营业外支出(万元)":
                # print(i)
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Out_of_business_expenses = int(row[1])
                else:
                    Out_of_business_expenses = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Out_of_business_expenses
                count_k = count_k + 1

            if name_of_this == "研发费用(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = [range(len(list_hy[catch]))]
                if row[1] != '--':
                    Research_costs = int(row[1])
                else:
                    Research_costs = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Research_costs
                count_k = count_k + 1

            if name_of_this == "销售费用(万元)":

                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = []
                if row[1] != '--':
                    Selling_costs = int(row[1])
                else:
                    Selling_costs = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Selling_costs
                count_k = count_k + 1

            if name_of_this == "管理费用(万元)":
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = []
                if row[1] != '--':
                    Management_costs = int(row[1])
                else:
                    Management_costs = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Management_costs
                count_k = count_k + 1
    print(csv3o)
    with open(csv3o, 'r', encoding='gbk') as csvfile3:
        reader3 = csv.reader(csvfile3)
        for i, rows in enumerate(reader3):
            row = rows
            if row:
                name_of_this = row[0]

            if name_of_this == "净利润(万元)":
                if k == 0:
                    List_by.append(0)

                    List_by[count_k] = []
                if row[1] != '--':
                    Net_profit = int(row[1])
                else:
                    Net_profit = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Net_profit
                count_k = count_k + 1

            if name_of_this == "总资产(万元)":
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = []
                if row[1] != '--':
                    Asset_liability_ratio = int(row[1])
                else:
                    Asset_liability_ratio = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Asset_liability_ratio
                count_k = count_k + 1

    with open(csv4o, 'r', encoding='gbk') as csvfile4:
        reader4 = csv.reader(csvfile4)
        for i, rows in enumerate(reader4):
            row = rows
            if row:
                name_of_this = row[0]

            # Assets_impairment_loss = input("Please input 资产减值损失")
            if name_of_this == " 资产减值准备(万元)":
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = []
                if row[1] != '--':
                    Assets_impairment_loss = int(row[1])
                else:
                    Assets_impairment_loss = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Assets_impairment_loss
                count_k = count_k + 1

            if name_of_this == " 经营活动产生的现金流量净额(万元)":
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = []
                if row[1] != '--':
                    Net_amount_from_operating_activities = int(row[1])
                else:
                    Net_amount_from_operating_activities = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Net_amount_from_operating_activities
                count_k = count_k + 1

            # Net_amount_from_Investment_Behavior = input("Please input 投资活动净额")
            if name_of_this == " 投资活动产生的现金流量净额(万元)":
                # print(i)
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = []
                if row[1] != '--':
                    Net_amount_from_Investment_Behavior = int(row[1])
                else:
                    Net_amount_from_Investment_Behavior = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Net_amount_from_Investment_Behavior
                count_k = count_k + 1

            # Cash_equivalents_ending_bal = input("Please input 现金等价物的期末余额：")
            if name_of_this == " 现金等价物的期末余额(万元)":
                # print(i)
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = []
                if row[1] != '--':
                    Cash_equivalents_ending_bal = int(row[1])
                else:
                    Cash_equivalents_ending_bal = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Cash_equivalents_ending_bal
                count_k = count_k + 1

            # Cash_ending_bal = input("Please input 现金的期末余额：")
            if name_of_this == " 现金的期末余额(万元)":
                # print(i)
                if k == 0:
                    List_by.append(0)
                    List_by[count_k] = []
                if row[1] != '--':
                    Cash_ending_bal = int(row[1])
                else:
                    Cash_ending_bal = 0
                List_by[count_k].append(0)
                List_by[count_k][k] = Cash_ending_bal
                count_k = count_k + 1

if List_by != []:
    a = len(List_by)
    c = 0
    while c < a:
        if List_by[c] == 0:
            List_by.remove(List_by[c])
            a = a - 1
            c = c - 1
        c = c + 1

for a in range(len(List_by)):

    List_a.append(0)
    at = 0
    if List_by[a] != 0:
        at = median(List_by[a])
    List_a[a] = at

count = 0
acount = 0
with open(csv1, 'r', encoding='gbk') as csvfile:
    reader = csv.reader(csvfile)
    for i, rows in enumerate(reader):

        row = rows
        name_of_this = row[0]
        Bank_and_cash = 0
        Bank_and_cash_sq = 0
        ("货币资金(万元)", name_of_this, Bank_and_cash, Bank_and_cash_sq)
        if name_of_this == "固定资产(万元)":
            if row[1] == '--':
                row[1] = 10
            Fixed_assets = int(row[1])
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Fixed_assets_sq = int(row[1 + count])
            Fixed_assets_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "应收账款(万元)":
            if row[1] == '--':
                row[1] = 10
            Accounts_receivable = int(row[1])
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Accounts_receivable_sq = int(row[1 + count])
            Accounts_receivable_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "其他应收款(万元)":
            if row[1] == '--':
                row[1] = 10
            Other_receivable = int(row[1])

            if Other_receivable == '--':
                Other_receivable = 10
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Other_receivable_sq = int(row[1 + count])
            Other_receivable_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "预付账款(万元)":
            if row[1] == '--':
                row[1] = 10
            Advances_to_suppliers = int(row[1])
            if Advances_to_suppliers == '--':
                Advances_to_suppliers = 10

            count = 1

            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Advances_to_suppliers_sq = int(row[1 + count])
            count = count + 1
            Other_receivable_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "资产总计(万元)":
            if row[1] == '--':
                row[1] = 10
            Total_assets = int(row[1])
            if Total_assets == '--':
                Total_assets = 10
            # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Total_assets_sq = int(row[1 + count])

            Total_assets_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "流动资产合计(万元)":
            if row[1] == '--':
                row[1] = 10
            Current_assets = int(row[1])
            if Current_assets == '--':
                Current_assets = 10
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Current_assets_sq = int(row[1 + count])
            Total_assets_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "流动负债合计(万元)":
            if row[1] == '--':
                row[1] = 10
            current_liabilities = int(row[1])
            if current_liabilities == '--':
                current_liabilities = 10
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            current_liabilities_sq = int(row[1 + count])
            current_liabilities_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "固定资产原值(万元)":
            if row[1] == '--':
                row[1] = 10
            Primary_Value_of_Fixed_Assets = int(row[1])
            if Primary_Value_of_Fixed_Assets == '--':
                Primary_Value_of_Fixed_Assets = 10
                # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Primary_Value_of_Fixed_Assets_sq = int(row[1 + count])

            Primary_Value_of_Fixed_Assets_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "累计折旧(万元)":
            if row[1] == '--':
                row[1] = 10
            Depreciation_expenses = int(row[1])
            if Depreciation_expenses == '--':
                Depreciation_expenses = 10
                # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Depreciation_expenses_sq = int(row[1 + count])
            Depreciation_expenses_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "在建工程(万元)":
            if row[1] == '--':
                row[1] = 10
            Construction_in_progress = int(row[1])
            if Construction_in_progress == '--':
                Construction_in_progress = 0
                # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Construction_in_progress_sq = int(row[1 + count])
            Construction_in_progress_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "存货(万元)":
            if row[1] == '--':
                row[1] = 10
            Stock = int(row[1])
            if Stock == '--':
                Stock = 10
            # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Stock_sq = int(row[1 + count])
            Stock_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "货币资金(万元)":
            if row[1] == '--':
                row[1] = 10
            Monetary_funds = int(row[1])
            if Monetary_funds == '--':
                Monetary_funds = 10
            # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Monetary_funds_sq = int(row[1 + count])
            Monetary_funds_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "一年内到期的非流动负债(万元)":
            if row[1] == '--':
                row[1] = 10

            Long_term_liabilities_one_year = int(row[1])
            if Long_term_liabilities_one_year == '--':
                Long_term_liabilities_one_year = 0
                # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Long_term_liabilities_one_year_sq = int(row[1 + count])
            Long_term_liabilities_one_year_hy = List_a[acount]
            acount = acount + 1

        # Dutiable_fees = input("Please input 应交税费")
        if name_of_this == "应交税费(万元)":
            if row[1] == '--':
                row[1] = 10
            Dutiable_fees = int(row[1])
            if Dutiable_fees == '--':
                Dutiable_fees = 10
                # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Dutiable_fees_sq = int(row[1 + count])
            Fixed_assets_hy = List_a[acount]
            acount = acount + 1

        # Engineering_materials = input("Please input 工程物资")
        if name_of_this == "工程物资(万元)":
            if row[1] == '--':
                row[1] = 10

            if row[1] == '--':
                Engineering_materials = 0
                # print("本期无该数据")
            else:
                Engineering_materials = int(row[1])
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Engineering_materials_sq = int(row[1 + count])
            Engineering_materials_hy = List_a[acount]
            acount = acount + 1

        # Accounts_payable = input("Please input 应付账款")
        if name_of_this == "应付账款(万元)":
            if row[1] == '--':
                row[1] = 10
            Accounts_payable = int(row[1])
            if Accounts_payable == '--':
                Accounts_payable = 10
                # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Accounts_payable_sq = int(row[1 + count])
            Accounts_payable_hy = List_a[acount]
            acount = acount + 1

        # Notes_payable = input("Please input 应付票据")
        if name_of_this == "应付票据(万元)":
            if row[1] == '--':
                row[1] = 10
            if row[1] == '--':
                Accounts_payable2 = 10
                # print("本期无该数据")
                count = 1
            else:
                Accounts_payable2 = int(row[1])
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Accounts_payable2_sq = int(row[1 + count])
            Accounts_payable2_hy = List_a[acount]
            acount = acount + 1

        # Total_liabilities = input("Please input 总负债")负债合计(万元)
        if name_of_this == "负债合计(万元)":
            if row[1] == '--':
                row[1] = 10
            Total_liabilities = int(row[1])
            if Total_liabilities == '--':
                Total_liabilities = 10
                # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Total_liabilities_sq = int(row[1 + count])
            Total_liabilities_hy = List_a[acount]
            acount = acount + 1

        # Criteria_for_withdrawal_of_inventory_depreciation = input("Please input 近三年存货跌价提取标准是否改变")
        # Completion_Degree_of_Construction_under_Construction = input("Please input 近三年在建工程完成度")
        # Period_of_depreciation = input("Please input 固定资产折旧年限")

        # Goodwill = input("Please input 商誉")
        if name_of_this == "商誉(万元)":
            if row[1] == '--':
                row[1] = 10
            Goodwill = int(row[1])
            if Goodwill == '--':
                Goodwill = 10
                # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Goodwill_sq = int(row[1 + count])
            Goodwill_hy = List_a[acount]
            acount = acount + 1

        # The_Valuation_Method_of_Investment_Real_Estate = input("Please input 投资性房地产计价方式")

        # Short_term_borrowing = input("Please input 短期借款")
        if name_of_this == "短期借款(万元)":
            if row[1] == '--':
                row[1] = 10
            Short_term_borrowing = int(row[1])
            if Short_term_borrowing == '--':
                Short_term_borrowing = 10
            # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Short_term_borrowing_sq = int(row[1 + count])
            Short_term_borrowing_hy = List_a[acount]
            acount = acount + 1

        # long_term_borrowing = input("Please input 长期借款")
        if name_of_this == "长期借款(万元)":

            if row[1] == '--':
                row[1] = 10
            long_term_borrowing = int(row[1])
            if long_term_borrowing == '--':
                long_term_borrowing = 10
                # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 0
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            long_term_borrowing_sq = int(row[1 + count])
            long_term_borrowing_hy = List_a[acount]
            acount = acount + 1

        # Other_Liquidity_Liabilities = input("Please input 其他流动性负债")
        if name_of_this == "其他流动资产(万元)":
            if row[1] == '--':
                row[1] = 10
            Other_Liquidity_Liabilities = int(row[1])
            if Other_Liquidity_Liabilities == '--':
                Other_Liquidity_Liabilities = 10
            #  print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Other_Liquidity_Liabilities_sq = int(row[1 + count])
            Other_Liquidity_Liabilities_hy = List_a[acount]
            acount = acount + 1

        # Bonds_payable = input("Please input 应付债券")
        if name_of_this == "应付债券(万元)":

            if row[1] == '--':
                row[1] = 10
            Bonds_payable = int(row[1])
            if Bonds_payable == '--':
                Bonds_payable = 0
            # print("本期无该数据")
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Bonds_payable_sq = int(row[1 + count])
            Bonds_payable_hy = List_a[acount]
            acount = acount + 1

        # Asset_structure = input("Please input 企业资产结构")

        if name_of_this == "实收资本(或股本)(万元)":
            if row[1] == '--':
                row[1] = 10
            Paid_in_capital = int(row[1])
            if Paid_in_capital == '--':
                Paid_in_capital = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Paid_in_capital_sq = int(row[1 + count])
            Paid_in_capital_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "资本公积(万元)":
            if row[1] == '--':
                row[1] = 10
            Capital_reserve = int(row[1])
            if Capital_reserve == '--':
                Capital_reserve = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Capital_reserve_sq = int(row[1 + count])
            Capital_reserve_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "盈余公积(万元)":
            if row[1] == '--':
                row[1] = 10
            Surplus_reserve = int(row[1])
            if Surplus_reserve == '--':
                Surplus_reserve = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Surplus_reserve_sq = int(row[1 + count])
            Surplus_reserve_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "未分配利润(万元)":
            if row[1] == '--':
                row[1] = 10
            Undistributed_profits = int(row[1])
            if Undistributed_profits == '--':
                Undistributed_profits = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Undistributed_profits_sq = int(row[1 + count])
            Undistributed_profits_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "预收账款(万元)":
            if row[1] == '--':
                row[1] = 10
            Advances_from_customers = int(row[1])
            if Advances_from_customers == '--':
                Advances_from_customers = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Advances_from_customers_sq = int(row[1 + count])

            Advances_from_customers_hy = List_a[acount]
            acount = acount + 1

with open(csv2, 'r', encoding='gbk') as csvfile2:
    reader2 = csv.reader(csvfile2)
    for i, rows in enumerate(reader2):
        row = rows
        name_of_this = row[0]

        if name_of_this == "营业收入(万元)":
            if row[1] == '--':
                row[1] = 10
            Main_Business_Income = int(row[1])
            if Main_Business_Income == '--':
                Main_Business_Income = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Main_Business_Income_sq = int(row[1 + count])
            Main_Business_Income_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "营业成本(万元)":
            if row[1] == '--':
                row[1] = 10
            Main_Business_Cost = int(row[1])
            if Main_Business_Cost == '--':
                Main_Business_Cost = 10
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Main_Business_Cost_sq = int(row[1 + count])
            Main_Business_Cost_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "其他业务收入(万元)":

            if row[1] == '--':
                row[1] = 10
            Other_Business_Income = int(row[1])
            if Other_Business_Income == '--':
                Other_Business_Income = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Other_Business_Income_sq = int(row[1 + count])
            Other_Business_Income_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "营业外收入(万元)":
            if row[1] == '--':
                row[1] = 10
            Out_of_business_income = int(row[1])
            if Out_of_business_income == '--':
                Out_of_business_income = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Out_of_business_income_sq = int(row[1 + count])
            Out_of_business_income_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "营业外支出(万元)":
            if row[1] == '--':
                row[1] = 10
            Out_of_business_expenses = int(row[1])
            if Out_of_business_expenses == '--':
                Out_of_business_expenses = 10
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Out_of_business_expenses_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "研发费用(万元)":
            if row[1] == '--':
                row[1] = 10
            Research_costs = int(row[1])
            if Research_costs == '--':
                Research_costs = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if row[1+count] == 0:
                row[1+count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10

            Research_costs_sq = int(row[1 + count])

            Research_costs_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "销售费用(万元)":
            if row[1] == '--':
                row[1] = 10
            Selling_costs = int(row[1])
            if Selling_costs == '--':
                Selling_costs = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Selling_costs_sq = int(row[1 + count])
            Selling_costs_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "管理费用(万元)":
            if row[1] == '--':
                row[1] = 10
            Management_costs = int(row[1])
            if Management_costs == '--':
                Management_costs = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Management_costs_sq = int(row[1 + count])
            Management_costs_hy = List_a[acount]
            acount = acount + 1

with open(csv3, 'r', encoding='gbk') as csvfile3:
    reader3 = csv.reader(csvfile3)
    for i, rows in enumerate(reader3):
        row = rows
        if row:
            name_of_this = row[0]

        if name_of_this == "净利润(万元)":
            if row[1] == '--':
                row[1] = 10
            Net_profit = int(row[1])

            if Net_profit == '--':
                Net_profit = 10
            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            Net_profit_sq = int(row[1 + count])
            Net_profit_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == "股东权益不含少数股东权益(万元)":
            if row[1] == '--':
                row[1] = 10
            gdqy = int(row[1])

            if gdqy == '--':
                gdqy = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1 + count]) == 0:
                row[1+count] = 10
            gdqy_sq = int(row[1 + count])

        if name_of_this == "净利润(扣除非经常性损益后)(万元)":
            if row[1] == '--':
                row[1] = 10
            Net_profit2 = int(row[1])

            if Net_profit2 == '--':
                Net_profit2 = 10

            count = 1
            while row[1 + count] == '--':
                count = count + 1
            if row[1 + count] == '':
                row[1 + count] = 10
            if int(row[1+count]) == 0:
                row[1+count] = 10
            Net_profit2_sq = int(row[1 + count])

        if name_of_this == "总资产(万元)":
            if row[1] == '--':
                row[1] = 10
            Asset_liability_ratio = int(row[1])
        if name_of_this == "总负债(万元)":
            if row[1] == '--':
                row[1] = 10
            Total_liabilities = int(row[1])
            Asset_liability_ratio = int(Total_liabilities) / int(Total_assets)
            Asset_liability_ratio_hy = List_a[acount]
            acount = acount + 1

with open(csv4, 'r', encoding='gbk') as csvfile4:
    reader4 = csv.reader(csvfile4)
    for i, rows in enumerate(reader4):
        row = rows
        if row:
            name_of_this = row[0]

        # Assets_impairment_loss = input("Please input 资产减值损失")
        if name_of_this == " 资产减值准备(万元)":
            if row[1] == '--':
                row[1] = 10
            Assets_impairment_loss = row[1]
            if Assets_impairment_loss == '--':
                Assets_impairment_loss = 10

            Assets_impairment_loss_hy = List_a[acount]
            acount = acount + 1

        # Net_amount_from_operating_activities = input("Please input 经营活动净额")
        if name_of_this == " 经营活动产生的现金流量净额(万元)":
            if row[1] == '--':
                row[1] = 10
            Net_amount_from_operating_activities = row[1]
            if Net_amount_from_operating_activities == '--':
                Net_amount_from_operating_activities = 10

            Net_amount_from_operating_activities_hy = List_a[acount]
            acount = acount + 1

        if name_of_this == " 投资活动产生的现金流量净额(万元)":
            if row[1] == '--':
                row[1] = 10
            Net_amount_from_Investment_Behavior = row[1]
            if Net_amount_from_Investment_Behavior == '--':
                Net_amount_from_Investment_Behavior = 10

            Net_amount_from_Investment_Behavior_hy = List_a[acount]
            acount = acount + 1

        # Cash_equivalents_ending_bal = input("Please input 现金等价物的期末余额：")
        if name_of_this == " 现金等价物的期末余额(万元)":
            if row[1] == '--':
                row[1] = 10
            Cash_equivalents_ending_bal = row[1]
            if Cash_equivalents_ending_bal == '--':
                Cash_equivalents_ending_bal = 10

            Cash_equivalents_ending_bal_hy = List_a[acount]
            acount = acount + 1

        # Cash_ending_bal = input("Please input 现金的期末余额：")
        if name_of_this == " 现金的期末余额(万元)":
            if row[1] == '--':
                row[1] = 10
            Cash_ending_bal = row[1]
            if Cash_ending_bal == '--':
                Cash_ending_bal = 10

            Cash_ending_bal_hy = List_a[acount]
            acount = acount + 1

jud = "TRUE"
with open('Result_of_Whether.csv', 'r', encoding='gbk') as csvfile5:
    reader4 = csv.reader(csvfile5)
    for i, rows in enumerate(reader4):
        row = rows
        if row:
            name_of_this = row[1]
        if name_of_this == "000004":
            jud = row[3]
        if jud == "FALSE":
            Opinion = "标准无保留意见"
        else:
            Opinion = "非标准"

RTR = 2 * Main_Business_Income / (Accounts_receivable + Accounts_receivable_sq)
DSRI = (int(Accounts_receivable) / int(Main_Business_Income)) / (
        int(Accounts_receivable_sq) / int(Main_Business_Income_sq))  # 应收账款指数 本期应收账款占营业收入比例/ 上期应收账款占营业收入比例
GMI = 1  # Gross_interest_rate_sq / Gross_interest_rate
# 上期毛利率/ 本期毛利率  上期毛利率/ 本期毛利率
AQI = (int(Total_assets) - int(Stock) - int(Fixed_assets)) / (
        Total_assets_sq - Stock_sq - Fixed_assets_sq)  # 资产质量指数  本期的非实物资产比例/ 上期的非实物资产比例
SGI = Main_Business_Income / Main_Business_Income_sq  # 收入指数 本期营业收入 / 上期营业收入
DEPI = (Depreciation_expenses / Primary_Value_of_Fixed_Assets) / (
        Depreciation_expenses_sq / Primary_Value_of_Fixed_Assets_sq)  # 折旧率指数  上期折旧率/ 本期折旧率，其中，折旧率 = 折旧费用/ 固定资产原值

SGAI = ((Selling_costs + Management_costs) / Main_Business_Income) / ((
                                                                              Selling_costs_sq + Management_costs_sq) / Main_Business_Income_sq)  # 销售管理费用指数  销售管理费用占营业收入的比例t/销售管理费用占营业收入的比例t-1  销售管理费用 = 销售费用+管理费用
LVGI = 1
# Asset_liability_ratio / Asset_liability_ratio_sq  # 财务杠杆指数 本期资产负债率 / 上期资产负债率

TATA = (((Current_assets - Current_assets_sq) - (Bank_and_cash - Bank_and_cash_sq)) - (
        (current_liabilities - current_liabilities_sq) - (
        Long_term_liabilities_one_year - Long_term_liabilities_one_year_sq) - current_liabilities_sq - (
                Long_term_liabilities_one_year - Long_term_liabilities_one_year_sq) - (
            Dutiable_fees))) / Total_assets
# 总应计项 应计项 / 总资产，
# 应计项 = (Δ 流动资产－ Δ 货币资金)   －  (Δ 流动负债 － Δ 一年内到期长期负债 － Δ 应交税费)－ 折旧费用

CH_REC = 2 * (Accounts_receivable - Accounts_receivable_sq) / (Total_assets + Total_assets_sq)  # 应收账款变动率 Δ应收账款 / 平均总资产
CH_INV = 2 * (Stock - Stock_sq) / (Total_assets + Total_assets_sq)  # 存货变动率 Δ存货 / 平均总资产
Soft_as = (
                  Total_assets - Fixed_assets - Construction_in_progress - Engineering_materials - Monetary_funds) / Total_assets  # 软资产比例  ( 总资产 － 固定资产 － 在建工程 － 工 程物资 －货币资金) /总资产
CH_CS = (Main_Business_Income - (
        Accounts_receivable - Accounts_receivable_sq)) / Main_Business_Income  # 现金销售率 ( 营业收入 － Δ 应收账款) /营业收入
CH_ROA = (2 * Net_profit / Total_assets_sq + Total_assets) - (
        2 * Net_profit_sq / Total_assets_sq + Total_assets)  # ＲOA增长率  ( 净利润/平均总资产) t － ( 净利润/ 平均总资产) t －1
ISSUE = 1
OTHREC = Other_receivable / Total_assets
LOSST = Net_profit2 / gdqy
LOSS = 0
if LOSST < 0:
    LOSS = 0
else:
    LOSS = 1
STKCYC = 0
if score_of_Macro_environment > 8:
    STKCYC = 1


def jugde_one(Opinion):
    risk_type.append(0)
    risk_grade.append(0)
    if Opinion != '标准无保留意见':
        risk_grade[0] = 10
        if Opinion == '带强调事项段的无保留意见':
            risk_type[0] = 1
        elif Opinion == '无法表示意见':
            risk_type[0] = 2
        elif Opinion == '保留意见':
            risk_type[0] = 3


def judge_two(Short_term_liabilities, Other_Liquidity_Liabilities, Bonds_payable, Monetary_funds):
    risk_grade.append(0)
    risk_type.append(0)
    if (Short_term_liabilities + Other_Liquidity_Liabilities + Bonds_payable) / Monetary_funds < 1:
        risk_grade[1] = 0
    elif (Short_term_liabilities + Other_Liquidity_Liabilities + Bonds_payable) / Monetary_funds < 1.2:
        risk_grade[1] = 2
    elif (Short_term_liabilities + Other_Liquidity_Liabilities + Bonds_payable) / Monetary_funds < 1.4:
        risk_grade[1] = 4
    elif (Short_term_liabilities + Other_Liquidity_Liabilities + Bonds_payable) / Monetary_funds < 1.6:
        risk_grade[1] = 6
    elif (Short_term_liabilities + Other_Liquidity_Liabilities + Bonds_payable) / Monetary_funds < 1.8:
        risk_grade[1] = 8
    else:
        risk_grade[1] = 10


def judge_three(Short_term_liabilities, Long_term_liabilities, Bonds_payable, Monetary_funds, Short_term_liabilities_hy,
                Long_term_liabilities_hy, Bonds_payable_hy, total_assets,
                Monetary_funds_hy):
    risk_grade.append(0)
    risk_type.append(0)
    if Monetary_funds / total_assets > 0.15:
        zs_company = (Short_term_liabilities + Long_term_liabilities + Bonds_payable) / Monetary_funds
        zs_hy = (Short_term_liabilities_hy + Long_term_liabilities_hy + Bonds_payable_hy) / Monetary_funds_hy
        if zs_company / zs_hy < 1:
            risk_grade[2] = 0
        elif zs_company / zs_hy < 1.2:
            risk_grade[2] = 2
        elif zs_company / zs_hy < 1.4:
            risk_grade[2] = 4
        elif zs_company / zs_hy < 1.6:
            risk_grade[2] = 6
        elif zs_company / zs_hy < 1.8:
            risk_grade[2] = 8
        else:
            risk_grade[2] = 10


def judge_four(Bank_and_cash, Cash_equivalents_ending_bal, Cash_ending_bal):  # 现金及现金等价物的余额需要现金流量表
    risk_grade.append(0)
    risk_type.append(0)
    sumcash = Cash_equivalents_ending_bal + Cash_ending_bal
    if Bank_and_cash == 0:
        Bank_and_cash = 0.45 * sumcash

    # if RTR - RTR_hy - sumcash / Bank_and_cash >:
    #    risk_grade[3] = 10
    if sumcash / Bank_and_cash < 0.25:
        risk_grade[3] = 8
    elif sumcash / Bank_and_cash < 0.45:
        risk_grade[3] = 6
    elif sumcash / Bank_and_cash < 0.65:
        risk_grade[3] = 4
    elif sumcash / Bank_and_cash < 0.85:
        risk_grade[3] = 2
    else:
        risk_grade[3] = 0


def judge_5(Monetary_funds, Industry_Monetary_funds):  # 加上前缀Industry_表示行业均值(....)
    risk_grade.append(0)
    risk_type.append(0)
    if Monetary_funds > 3.5 * Industry_Monetary_funds:
        risk_grade[4] = 10
        risk_type[4] = 1
    elif Monetary_funds > 3.0 * Industry_Monetary_funds:
        risk_grade[4] = 8
        risk_type[4] = 1
    elif Monetary_funds > 2.5 * Industry_Monetary_funds:
        risk_grade[4] = 6
        risk_type[4] = 1
    elif Monetary_funds > 2.0 * Industry_Monetary_funds:
        risk_grade[4] = 4
        risk_type[4] = 1
    elif Monetary_funds > 1.8 * Industry_Monetary_funds:
        risk_grade[4] = 2
        risk_type[4] = 1


def judge_six(Bank_and_Cash, Total_assets, industry_level):
    risk_grade.append(0)
    risk_type.append(0)
    if Bank_and_Cash / Total_assets - industry_level:
        risk_grade[5] = 10
    elif Bank_and_Cash / Total_assets - industry_level > 0.3:
        risk_grade[5] = 8
    elif Bank_and_Cash / Total_assets - industry_level > 0.2:
        risk_grade[5] = 6
    elif Bank_and_Cash / Total_assets - industry_level > 0.1:
        risk_grade[5] = 4
    else:
        risk_grade[5] = 0


def judge_seven(Account_receivable, Previous_accounts_receivable, Main_Business_Income,
                Previous_Main_Business_Income):
    risk_grade.append(0)
    risk_type.append(0)
    IAR = (Account_receivable - Previous_accounts_receivable) / Previous_accounts_receivable
    IPOR = (Main_Business_Income - Previous_Main_Business_Income) / Previous_Main_Business_Income

    if IAR - IPOR > 0.4:
        risk_grade[6] = 10
    elif IAR - IPOR > 0.3:
        risk_grade[6] = 8
    elif IAR - IPOR > 0.2:
        risk_grade[6] = 6
    elif IAR - IPOR > 0.1:
        risk_grade[6] = 4
    elif IAR - IPOR > 0:
        risk_grade[6] = 2
    else:
        risk_grade[6] = 0


def judge_eight(Account_receivable, Main_Business_Income, Other_Business_Income):
    risk_grade.append(0)
    risk_type.append(0)
    Current_revenue = Main_Business_Income + Other_Business_Income

    if Account_receivable / Current_revenue > 0.45:
        risk_grade[7] = 10
    elif Account_receivable / Current_revenue > 0.35:
        risk_grade[7] = 8
    elif Account_receivable / Current_revenue > 0.25:
        risk_grade[7] = 6
    elif Account_receivable / Current_revenue > 0.15:

        risk_grade[7] = 4
    elif Account_receivable / Current_revenue > 0:
        risk_grade[7] = 2

    else:
        risk_grade[7] = 0


def judge_nine(
        RTR):
    risk_grade.append(8)
    risk_type.append(8)
    x = 360 / RTR
    if x > 360:
        risk_grade[9] = 10
    elif x > 300:
        risk_grade[9] = 8
    elif x > 240:
        risk_grade[9] = 6
    elif x > 120:
        risk_grade[9] = 4
    else:
        risk_grade[9] = 0


def judge_ten(Other_receivable, Total_assets, Other_receivable_hy, Total_assets_hy):
    risk_grade.append(0)
    risk_type.append(0)
    rateone = Other_receivable / Total_assets
    rateone_hy = Other_receivable_hy / Total_assets_hy
    if rateone - rateone_hy > 0.3:
        risk_grade[9] = 10
    elif rateone - rateone_hy > 0.2:
        risk_grade[9] = 8
    elif rateone - rateone_hy > 0.1:
        risk_grade[9] = 6
    else:
        risk_grade[9] = 0


def judge_12(BDPR, industry_level_lisrt_of_bad_debt_ratio):
    risk_grade.append(0)
    risk_type.append(0)
    # if BDPR < industry_level:
    #   risk_grade[11] = 6
    # else:
    risk_grade[11] = 0


def judge_13(Advances_to_suppliers, Total_assets):
    x = Advances_to_suppliers / Total_assets

    risk_grade.append(0)
    risk_type.append(0)
    if x > 0.1:
        risk_grade[12] = 10
    elif x > 0.06:
        risk_grade[12] = 8
    elif x > 0.03:
        risk_grade[12] = 6
    else:
        risk_grade[12] = 0


def judge_14(Advances_to_suppliers_list, Total_assets_list, Advances_from_customers_list):
    risk_grade.append(13)
    risk_type.append(13)
    Asratelist = []
    Acratelist = []
    count1 = 0
    count2 = 0
    flag1 = 0
    flag2 = 0
    srate = Advances_to_suppliers(5) / Total_assets(5)
    crate = Advances_from_customers(5) / Total_assets(5)
    for t, i in Advances_to_suppliers_list, Total_assets_list:
        Asratelist.append(t / i)
    for c, i in Advances_from_customers_list, Total_assets_list:
        Acratelist.append(t / i)

    Asratelist.pop(0)
    Asratelist.pop(1)
    Acratelist.pop(0)
    Acratelist.pop(1)
    if srate > 0.03 and crate > 0.03:
        for s, c in Asratelist, Acratelist:
            if abs(s - c) < 0.01:
                count1 = count1 + 1
            if count1 >= 3:
                flag1 = 1
                break

    Asratelist.clear()
    Asratelist.clear()

    for t, i in Advances_to_suppliers_list, Total_assets_list:
        Asratelist.append(t / i)
    for c, i in Advances_from_customers_list, Total_assets_list:
        Acratelist.append(t / i)
    if srate > 0.03 and crate > 0.03:
        for i in range(4):
            if (Asratelist(i + 1) - Asratelist(i)) / (Acratelist(i + 1) - Acratelist(i)) > 0:
                count2 = count2 + 1
            if count2 >= 4:
                flag2 = 1
                break
    if flag1 * flag2 == 1:
        risk_grade[13] = 10
    else:
        if flag1 == 1 or flag2 == 1:
            risk_grade[13] = 8
        else:
            risk_grade.append[13] = 0


def judge_15(Initial_inventory, Industry_Initial_inventory, Final_inventory, Industry_Final_inventory,
             Selling_costs, Industry_Selling_costs):  # 加上前缀Industry_表示行业均值
    risk_grade.append(0)
    risk_type.append(0)
    Inventory_turnover = 2 * Selling_costs / (Initial_inventory + Final_inventory)
    Industry_Inventory_turnover = 2 * Industry_Selling_costs / (Industry_Initial_inventory + Industry_Final_inventory)
    Industry_Monetary_funds = Monetary_funds / 2
    if Inventory_turnover > 3.5 * Industry_Inventory_turnover:
        risk_grade[14] = 10
        risk_type[14] = 1
    elif Monetary_funds > 3.0 * Industry_Monetary_funds:
        risk_grade[14] = 8
        risk_type[14] = 1
    elif Monetary_funds > 2.5 * Industry_Monetary_funds:
        risk_grade[14] = 6
        risk_type[14] = 1
    elif Monetary_funds > 2.0 * Industry_Monetary_funds:
        risk_grade[14] = 4
        risk_type[14] = 1
    elif Monetary_funds > 1.8 * Industry_Monetary_funds:
        risk_grade[14] = 2
        risk_type[14] = 1


def judge_16(Initial_inventory, Industry_Initial_inventory, Final_inventory,
             Industry_Final_inventory):
    risk_grade.append(0)
    risk_type.append(0)
    Rate = (Final_inventory - Initial_inventory) / Initial_inventory
    Industry_Rate = (Industry_Final_inventory - Industry_Initial_inventory) / Industry_Initial_inventory

    if Rate > 3.5 * Industry_Rate:
        risk_grade[15] = 10
        risk_type[15] = 1
    elif Rate > 3.0 * Industry_Rate:
        risk_grade[15] = 8
        risk_type[15] = 1
    elif Rate > 2.5 * Industry_Rate:
        risk_grade[15] = 6
        risk_type[15] = 1
    elif Rate > 2.0 * Industry_Rate:
        risk_grade[15] = 4
        risk_type[15] = 1
    elif Rate > 1.8 * Industry_Rate:
        risk_grade[15] = 2
        risk_type[15] = 1


def judge_17(Criteria_for_withdrawal_of_inventory_depreciation):
    risk_grade.append(0)
    risk_type.append(0)

    if Criteria_for_withdrawal_of_inventory_depreciation == True:
        risk_grade[16] = 5
        risk_type[16] = 1


def judge_18(Period_of_depreciation, Industry_Period_of_depreciation):
    risk_grade.append(0)
    risk_type.append(0)
    if Period_of_depreciation > 3.5 * Industry_Period_of_depreciation:
        risk_grade[17] = 10
        risk_type[17] = 1
    elif Period_of_depreciation > 3.0 * Industry_Period_of_depreciation:
        risk_grade[17] = 8
        risk_type[17] = 1
    elif Period_of_depreciation > 2.5 * Industry_Period_of_depreciation:
        risk_grade[17] = 6
        risk_type[17] = 1
    elif Period_of_depreciation > 2.0 * Industry_Period_of_depreciation:
        risk_grade[17] = 4
        risk_type[17] = 1
    elif Period_of_depreciation > 1.5 * Industry_Period_of_depreciation:
        risk_grade[17] = 2
        risk_type[17] = 1


def judge_19(Goodwill, Industry_goodwill, Total_assets, Industry_total_assets):
    risk_grade.append(0)
    risk_type.append(0)
    Rate = Goodwill / Total_assets
    if Industry_total_assets == 0:
        Industry_total_assets = 10
    Industry_Rate = Industry_goodwill / Industry_total_assets

    if Rate > 3.5 * Industry_Rate:
        risk_grade[18] = 10
        risk_type[18] = 1
    elif Rate > 3.0 * Industry_Rate:
        risk_grade[18] = 8
        risk_type[18] = 1
    elif Rate > 2.5 * Industry_Rate:
        risk_grade[18] = 6
        risk_type[18] = 1
    elif Rate > 2.0 * Industry_Rate:
        risk_grade[18] = 4
        risk_type[18] = 1
    elif Rate > 1.8 * Industry_Rate:
        risk_grade[18] = 2
        risk_type[18] = 1


def judge_20(a):
    risk_grade.append(0)
    risk_type.append(0)
    risk_grade[19] = 0
    risk_type[19] = 1


def judge_21(a):
    risk_grade.append(0)
    risk_type.append(0)
    risk_grade[20] = 0
    risk_type[20] = 1


def judge_22(intangible_assets, Industry_intangible_assets, Total_assets, Industry_total_assets):
    risk_grade.append(0)
    risk_type.append(0)
    Rate = intangible_assets / Total_assets
    if Industry_total_assets == 0:
        Industry_total_assets = 10
    Industry_Rate = Industry_intangible_assets / Industry_total_assets

    if Rate > 3.5 * Industry_Rate:
        risk_grade[21] = 10
        risk_type[21] = 1
    elif Rate > 3.0 * Industry_Rate:
        risk_grade[21] = 8
        risk_type[21] = 1
    elif Rate > 2.5 * Industry_Rate:
        risk_grade[21] = 6
        risk_type[21] = 1
    elif Rate > 2.0 * Industry_Rate:
        risk_grade[21] = 4
        risk_type[21] = 1
    elif Rate > 1.8 * Industry_Rate:
        risk_grade[21] = 2
        risk_type[21] = 1


def judge_23(Completion_Degree_of_Construction_under_Construction):
    risk_grade.append(0)
    risk_type.append(0)

    if (Completion_Degree_of_Construction_under_Construction[-1] > 0.9 and
            Completion_Degree_of_Construction_under_Construction[-2] > 0.9
            and Completion_Degree_of_Construction_under_Construction[-3] > 0.9):
        risk_grade[22] = 8
        risk_type[22] = 1


def judge_24(assets_impairment_loss, Industry_assets_impairment_loss, total_operating_costs,
             Industry_total_operating_costs):
    risk_grade.append(0)
    risk_type.append(0)
    Rate = assets_impairment_loss / total_operating_costs
    Industry_Rate = Industry_assets_impairment_loss / Industry_total_operating_costs

    if Rate > 3.5 * Industry_Rate:
        risk_grade[23] = 10
        risk_type[23] = 1
    elif Rate > 3.0 * Industry_Rate:
        risk_grade[23] = 8
        risk_type[23] = 1
    elif Rate > 2.5 * Industry_Rate:
        risk_grade[23] = 6
        risk_type[23] = 1
    elif Rate > 2.0 * Industry_Rate:
        risk_grade[23] = 4
        risk_type[23] = 1
    elif Rate > 1.5 * Industry_Rate:
        risk_grade[23] = 2
        risk_type[23] = 1


def judge_25():
    risk_grade.append(0)
    risk_type.append(0)
    risk_grade[24] = 0
    risk_type[24] = 1


def judge_26(The_Valuation_Method_of_Investment_Real_Estate):
    risk_grade.append(0)
    risk_type.append(0)
    if The_Valuation_Method_of_Investment_Real_Estate == "公允价值法":
        risk_grade[25] = 0
        risk_type[25] = 1


def judge_27(Short_term_borrowing, Industry_Short_term_borrowing, Other_Liquidity_Liabilities,
             Industry_Other_Liquidity_Liabilities,
             Bonds_payable, Industry_Bonds_payable, Total_liabilities,
             Industry_Total_liabilities):
    risk_grade.append(0)
    risk_type.append(0)
    Rate = (Short_term_borrowing + Other_Liquidity_Liabilities + Bonds_payable) / Total_liabilities
    Industry_Rate = (
                            Industry_Short_term_borrowing + Industry_Other_Liquidity_Liabilities + Industry_Bonds_payable) / (
                            Industry_Total_liabilities + 1000)

    if Rate > 3.5 * Industry_Rate:
        risk_grade[26] = 10
        risk_type[26] = 1
    elif Rate > 3.0 * Industry_Rate:
        risk_grade[26] = 8
        risk_type[26] = 1
    elif Rate > 2.5 * Industry_Rate:
        risk_grade[26] = 6
        risk_type[26] = 1
    elif Rate > 2.0 * Industry_Rate:
        risk_grade[26] = 4
        risk_type[26] = 1
    elif Rate > 1.8 * Industry_Rate:
        risk_grade[26] = 2
        risk_type[26] = 1


def judge_28(Asset_structure):
    risk_grade.append(0)
    risk_type.append(0)
    if Asset_structure == "重资产":
        risk_grade[27] = 2
        risk_type[27] = 1


def judge_29(Main_business, Other_business, Main_business_sq, Other_business_sq):
    risk_grade.append(0)
    risk_type.append(0)
    a = Other_business / (Main_business + Other_business)
    a_sq = Other_business_sq / (Main_business_sq + Other_business_sq)
    if a > 0.3 and a > a_sq * 1.3:
        risk_type[28] = 3
        if a > 0.5:
            risk_grade[28] = 6
        else:
            risk_grade[28] = 4
    elif a > 0.3:
        risk_type[28] = 2
        if a > 0.5:
            risk_grade[28] = 4
        else:
            risk_grade[28] = 2
    elif a > a_sq * 1.3:
        risk_type[28] = 1
        risk_grade[28] = 2


def judge_30(net_amount_from_operating_activities, net_amount_from_operating_activities_pq,
             net_amount_from_Investment_Behavior, Net_profit, Accounts_payable):
    risk_grade.append(0)
    risk_type.append(0)

    a = net_amount_from_operating_activities
    b = net_amount_from_Investment_Behavior
    c = a / Net_profit
    if a > 0 and a - Accounts_payable < 0:
        risk_type[29] = 6
        risk_grade[29] = 4
    if c < 1:
        risk_type[29] = 5
        risk_grade[29] = 4
    if a < 0 and b < 0:
        risk_type[29] = 1
        risk_grade[29] = 2
        if net_amount_from_operating_activities_pq < 0:
            risk_grade[29] = 4
    elif a > 0 and b < 0:
        risk_type[29] = 2
        risk_grade[29] = 0
    elif a > 0 and b > 0:
        risk_type[29] = 3
        risk_grade[29] = 0
    elif a < 0 and b > 0:
        risk_type[29] = 4
        if net_amount_from_operating_activities_pq < 0:
            risk_grade[29] = 4


def judge_31(Net_amount_from_operating_activities, Net_profit):
    risk_grade.append(0)
    risk_type.append(0)
    a = Net_amount_from_operating_activities / Net_profit
    if a < 0:
        risk_grade[30] = 6
    elif a < 0.5:
        risk_grade[30] = 4
    elif a < 1:
        risk_grade[30] = 2


def judge_32(Main_Business_Income, Main_Business_Cost, Main_Business_Income_hy, Main_Business_Cost_hy):
    risk_grade.append(0)
    risk_type.append(0)
    mil = (Main_Business_Income - Main_Business_Cost) / Main_Business_Cost
    if Main_Business_Cost_hy == 0:
        Main_Business_Cost_hy = 10
    mil_hy = (Main_Business_Income_hy - Main_Business_Cost_hy) / Main_Business_Cost_hy
    if mil < mil_hy:
        risk_grade[31] = 4
        risk_type[31] = 3
    elif mil > 1.5 * mil_hy:
        risk_grade[31] = 4
        risk_type[31] = 4
    if mil > 0.2:
        risk_grade[31] = 0
        if mil > 0.4:
            risk_type[31] = 1
        else:
            risk_type[31] = 2
    else:
        risk_grade[31] = 4


def judge_33(Main_Business_Income, Management_costs, Main_Business_Income_hy, Management_costs_hy,
             Main_Business_Income_sq, Management_costs_sq):
    risk_grade.append(0)
    risk_type.append(0)
    a = Management_costs / Main_Business_Income
    if Main_Business_Income_hy == 0:
        Main_Business_Income_hy = 10
    a_hy = Management_costs_hy / Main_Business_Income_hy
    a_sq = Management_costs_sq / Main_Business_Income_sq
    if a < a_hy * 1.2:
        risk_grade[33] = 2
        risk_type[33] = 1
    elif a < a_hy * 1.4:
        risk_grade[33] = 4
        risk_type[33] = 1
    elif a < a_hy * 1.6:
        risk_grade[33] = 6
        risk_type[33] = 1
    elif a < a_hy * 1.8:
        risk_grade[33] = 8
        risk_type[33] = 1
    else:
        risk_grade[33] = 10
        risk_type[33] = 1
    if (a - a_sq) / a_sq > 0.3:
        risk_type[33] = 2
        risk_grade[33] = 4


if Main_Business_Income_hy == 0:
    Main_Business_Income_hy = 1.2 * Main_Business_Income


def judge_35(Main_Business_Income, Selling_costs, Main_Business_Income_hy, Selling_costs_hy,
             Main_Business_Income_sq, Selling_costs_sq, ):
    risk_grade.append(0)
    risk_type.append(0)

    a = Selling_costs / Main_Business_Income
    a_hy = Selling_costs_hy / Main_Business_Income_hy
    a_sq = Selling_costs_sq / Main_Business_Income_sq
    if a < a_hy * 1.2:
        risk_grade[34] = 2
        risk_type[34] = 1
    elif a < a_hy * 1.4:
        risk_grade[34] = 4
        risk_type[34] = 1
    elif a < a_hy * 1.6:
        risk_grade[34] = 6
        risk_type[34] = 1
    elif a < a_hy * 1.8:
        risk_grade[34] = 8
        risk_type[34] = 1
    else:
        risk_grade[34] = 10
        risk_type[34] = 1
    if (a - a_sq) / a_sq > 0.3:
        risk_type[34] = 2
        risk_grade[34] = 4


def judge_36(Main_Business_Income, Research_costs, Main_Business_Income_hy, Research_costs_hy,
             Main_Business_Income_sq, Research_costs_sq, ):
    risk_grade.append(0)
    risk_type.append(0)
    a = Research_costs / Main_Business_Income
    a_hy = Research_costs_hy / Main_Business_Income_hy
    a_sq = Research_costs_sq / Main_Business_Income_sq

    if a < a_hy * 1.2:
        risk_grade[35] = 2
        risk_type[35] = 1
    elif a < a_hy * 1.4:
        risk_grade[35] = 4
        risk_type[35] = 1
    elif a < a_hy * 1.6:
        risk_grade[35] = 6
        risk_type[35] = 1
    elif a < a_hy * 1.8:
        risk_grade[35] = 8
        risk_type[35] = 1
    else:
        risk_grade[35] = 10
        risk_type[35] = 1
    if (a - a_sq) / a_sq > 0.3:
        risk_type[35] = 2
        risk_grade[35] = 4


def judge_37(Money_for_fixed_assets_and_others, Net_amount_from_operating_activities,
             Money_for_fixed_assets_and_others_sq, Net_amount_from_operating_activities_sq):
    risk_grade.append(0)
    risk_type.append(0)
    if Money_for_fixed_assets_and_others > Net_amount_from_operating_activities:
        risk_grade[36] = 2
        if Money_for_fixed_assets_and_others_sq > Net_amount_from_operating_activities_sq:
            risk_grade[36] = 4
    else:
        risk_grade[36] = 0


def judge_38(Main_Business_Cost, Stock_qc, Stock_qm, Main_Business_Cost_hy, Stock_qc_hy, Stock_qm_hy):
    risk_grade.append(0)
    risk_type.append(0)
    a = Main_Business_Cost * 2 / (Stock_qc + Stock_qm)
    a_hy = Main_Business_Cost_hy * 2 / (Stock_qc_hy + Stock_qm_hy)
    if a < a_hy:
        risk_grade[37] = 2
    elif a > 0.6 * a_hy:
        risk_grade[37] = 4
    elif a > 0.3 * a_hy:
        risk_grade[37] = 6


Net_amount_from_operating_activities = 10
Net_amount_from_operating_activities_pq = Net_amount_from_operating_activities

Money_for_fixed_assets_and_others = 10
Money_for_fixed_assets_and_others_sq = 10

Stock_qc = Stock_sq
Stock_qm = Stock
Stock_qc_hy = Stock_hy
Stock_qm_hy = Stock_sq
Net_amount_from_Investment_Behavior = 10
Net_amount_from_operating_activities_sq = Net_amount_from_operating_activities
intangible_assets = Total_assets - Fixed_assets
intangible_assets_hy = Total_assets_hy - Fixed_assets_hy
Short_term_liabilities = Short_term_borrowing + Accounts_payable + Accounts_payable2 + Long_term_liabilities_one_year
Short_term_liabilities_hy = Short_term_borrowing_hy + Accounts_payable_hy + Accounts_payable2_hy + Long_term_liabilities_one_year_hy

Long_term_liabilities_hy = long_term_borrowing_hy
Long_term_liabilities = long_term_borrowing
Other_Liquidity_Liabilities = Total_liabilities - Short_term_liabilities - Long_term_liabilities
total_assets = Total_assets
Industry_Monetary_funds = Monetary_funds_hy
Bank_and_Cash = Bank_and_cash
industry_level = 10
Discount_and_allowance = 10
term_number = 10
Other_Business_Income = 10
The_Valuation_Method_of_Investment_Real_Estate = "公允价值法"
jugde_one(Opinion)
judge_two(Short_term_liabilities, Other_Liquidity_Liabilities, Bonds_payable, Monetary_funds)
judge_three(Short_term_liabilities, Long_term_liabilities, Bonds_payable, Monetary_funds, Short_term_liabilities_hy,
            Long_term_liabilities_hy, Bonds_payable_hy, total_assets, Monetary_funds_hy)
judge_four(Bank_and_cash, term_number, term_number)
judge_5(Monetary_funds, Industry_Monetary_funds)
judge_six(Bank_and_Cash, Total_assets, industry_level)
judge_seven(Accounts_receivable, Accounts_receivable_sq, Main_Business_Income, Main_Business_Income_sq)
judge_eight(Accounts_receivable, Main_Business_Income, Other_Business_Income)
judge_ten(Other_receivable, Total_assets, 10, 10)
judge_12(term_number, term_number)

judge_13(10, Total_assets)
# judge_14(term_number, Total_assets_list, Advances_from_customers_list)

# judge_15(Initial_inventory, Industry_Initial_inventory, Final_inventory, Industry_Final_inventory,Selling_costs, Industry_Selling_costs)

# judge_16(Initial_inventory, Industry_Initial_inventory, Final_inventory,Industry_Final_inventory)

# judge_17(Criteria_for_withdrawal_of_inventory_depreciation)

# judge_18(Period_of_depreciation, Industry_Period_of_depreciation)

judge_19(Goodwill, Goodwill_hy, Total_assets, Total_assets_hy)
judge_22(intangible_assets, intangible_assets_hy, Total_assets, Total_assets_hy)
# judge_23(Completion_Degree_of_Construction_under_Construction)

assets_impairment_loss = (Total_assets - Total_assets_sq + 1000) * 0.3
Industry_assets_impairment_loss = (Total_assets - Total_assets_sq + 1000) * 0.3
total_operating_costs = Selling_costs + Management_costs + Research_costs + 1000
Industry_total_operating_costs = Selling_costs_hy + Management_costs_hy + Research_costs_hy + 1000
judge_24(assets_impairment_loss, Industry_assets_impairment_loss, total_operating_costs, Industry_total_operating_costs)
judge_26(The_Valuation_Method_of_Investment_Real_Estate)
judge_27(Short_term_borrowing, Short_term_borrowing_hy, Other_Liquidity_Liabilities, Other_Liquidity_Liabilities_hy,
         Bonds_payable, Bonds_payable_hy, Total_liabilities, Total_liabilities_hy)

if Fixed_assets / Total_assets > 0.5:
    Asset_structure = '重资产'

judge_28(Asset_structure)
Other_Business_Income_sq = Other_Business_Income
judge_29(Main_Business_Income, Other_Business_Income, Main_Business_Income_sq, Other_Business_Income_sq)
judge_30(Net_amount_from_operating_activities, Net_amount_from_operating_activities_pq,
         Net_amount_from_Investment_Behavior, Net_profit, Accounts_payable)
judge_31(Net_amount_from_operating_activities, Net_profit)
judge_32(Main_Business_Income, Main_Business_Cost, Main_Business_Income_hy, Main_Business_Cost_hy)
judge_33(Main_Business_Income, Management_costs, Main_Business_Income_hy, Management_costs_hy,
         Main_Business_Income_sq, Management_costs_sq)
judge_35(Main_Business_Income, Selling_costs, Main_Business_Income_hy, Selling_costs_hy, Main_Business_Income_sq,
         Selling_costs_sq, )
judge_36(Main_Business_Income, Research_costs, Main_Business_Income_hy, Research_costs_hy, Main_Business_Income_sq,
         Research_costs_sq)
judge_37(Money_for_fixed_assets_and_others, Net_amount_from_operating_activities,
         Money_for_fixed_assets_and_others_sq, Net_amount_from_operating_activities_sq)
judge_38(Main_Business_Cost, Stock_qc, Stock_qm, Main_Business_Cost_hy, Stock_qc_hy, Stock_qm_hy)
score_of_grade10 = 0
score_of_grade8 = 0
score_of_grade6 = 0
score_of_grade4 = 0
score_of_grade2 = 0
for i in range(len(risk_grade)):
    if risk_grade[i] == 10:
        score_of_grade10 = score_of_grade10 + 1
    if risk_grade[i] == 8:
        score_of_grade8 = score_of_grade8 + 1
    if risk_grade[i] == 6:
        score_of_grade6 = score_of_grade6 + 1
    if risk_grade[i] == 4:
        score_of_grade4 = score_of_grade4 + 1
    if risk_grade[i] == 2:
        score_of_grade2 = score_of_grade2 + 1


def grade():
    Enterprise_environment = 79.911 - 1.1827 * RTR + 4.4168 * DSRI + 0.5016 * AQI + 1.1509 * SGI - 0.6003 * DEPI - 0.0935 * SGAI - 11.7524 * LVGI - 46.1602 * CH_REC - 3.8614 * CH_INV - 0.0001 * Soft_as + 40.7000 * CH_CS - 19.9478 * CH_ROA - 2.5024 * STKCYC

    grade_1 = score_of_Macro_environment + score_Meso_environment + 0.8 * Enterprise_environment
    grade_2 = grade_1 - score_of_Supervisory_authority - 1.9 * score_of_grade10 - 1.2 * score_of_grade8 - 0.7 * score_of_grade6 - 0.2 * score_of_grade4 - 0.1 * score_of_grade2
    if grade_2 >95:
        grade_2 = 95
    if grade_2 < 45:
        grade_2 = 45
    return grade_2


grade = grade()

degree = 0
add = []
add = [a for i in range(60)]

count_now1 = -1
description = ""

degree = ""
list_out = []
for i in range(60):
    if i != 0:
        count_now1 = count_now1 + 1
        list_out.append(0)
    if i == 1:
        description = "会计师出具意见不是标准无保留意见"

        if risk_grade[0] == 10:
            degree = 10
        elif risk_grade[0] == 8:
            degree = 8
        elif risk_grade[0] == 6:
            degree = 6
        elif risk_grade[0] == 4:
            degree = 4
        elif risk_grade[0] == 2:
            degree = 2
        else:
            degree = 0
        list_out_1 = [degree, description, add[0]]
        list_out[count_now1] = list_out_1

    if i == 2:
        description = "货币资金与短期债务和经营需要不相符合——货币资金与短期债务和经营需要不相符合,"
        if risk_grade[1] == 10:
            degree = 10
        elif risk_grade[1] == 8:
            degree = 8
        elif risk_grade[1] == 6:
            degree = 6
        elif risk_grade[1] == 4:
            degree = 4
        elif risk_grade[1] == 2:
            degree = 2
        else:
            degree = 0
        list_out_2 = [degree, description, add[1]]
        list_out[count_now1] = list_out_2

    if i == 3:
        description = "货币资金与短期债务和经营需要不相符合——货币资金充裕，却有许多有息或高息负债"
        if risk_grade[2] == 10:
            degree = 10
        elif risk_grade[2] == 8:
            degree = 8
        elif risk_grade[2] == 6:
            degree = 6
        elif risk_grade[2] == 4:
            degree = 4
        elif risk_grade[2] == 2:
            degree = 2
        else:
            degree = 0
        list_out_3 = [degree, description, add[2]]

        list_out[count_now1] = list_out_3

    if i == 4:
        description = "货币资金与短期债务和经营需要不相符合——定期存款很多，其他货币资金很多，但是流动资金却很缺乏"
        if risk_grade[3] == 10:
            degree = 10
        elif risk_grade[3] == 8:
            degree = 8
        elif risk_grade[3] == 6:
            degree = 6
        elif risk_grade[3] == 4:
            degree = 4
        elif risk_grade[3] == 2:
            degree = 2
        else:
            degree = 0
        list_out_4 = [degree, description, add[3]]

        list_out[count_now1] = list_out_4

    if i == 5:
        description = "货币资金与短期债务和经营需要不相符合，其他货币资金金额巨大却没有合理解释"
        if risk_grade[4] == 10:
            degree = 10
        elif risk_grade[4] == 8:
            degree = 8
        elif risk_grade[4] == 6:
            degree = 6
        elif risk_grade[4] == 4:
            degree = 4
        elif risk_grade[4] == 2:
            degree = 2
        else:
            degree = 0
        list_out_5 = [degree, description, add[4]]

        list_out[count_now1] = list_out_5

    if i == 6:
        description = "货币资金与短期债务和经营需要不相符——账上货币资金留存过多合"
        if risk_grade[5] == 10:
            degree = 10
        elif risk_grade[5] == 8:
            degree = 8
        elif risk_grade[5] == 6:
            degree = 6
        elif risk_grade[5] == 4:
            degree = 4
        elif risk_grade[5] == 2:
            degree = 2
        else:
            degree = 0
        list_out_6 = [degree, description, add[5]]

        list_out[count_now1] = list_out_6

    if i == 7:
        description = "应收账款大幅度增长"
        if risk_grade[6] == 10:
            degree = 10
        elif risk_grade[6] == 8:
            degree = 8
        elif risk_grade[6] == 6:
            degree = 6
        elif risk_grade[6] == 4:
            degree = 4
        elif risk_grade[6] == 2:
            degree = 2
        else:
            degree = 0
        list_out_7 = [degree, description, add[6]]

        list_out[count_now1] = list_out_7

    if i == 8:
        description = "应收账款过多"
        if risk_grade[7] == 10:
            degree = 10
        elif risk_grade[7] == 8:
            degree = 8
        elif risk_grade[7] == 6:
            degree = 6
        elif risk_grade[7] == 4:
            degree = 4
        elif risk_grade[7] == 2:
            degree = 2
        else:
            degree = 0
        list_out_8 = [degree, description, add[7]]

        list_out[count_now1] = list_out_8

    if i == 9:
        description = "应收账款周转率"
        if risk_grade[8] == 10:
            degree = 10
        elif risk_grade[8] == 8:
            degree = 8
        elif risk_grade[8] == 6:
            degree = 6
        elif risk_grade[8] == 4:
            degree = 4
        elif risk_grade[8] == 2:
            degree = 2
        else:
            degree = 0
        list_out_9 = [degree, description, add[8]]

        list_out[count_now1] = list_out_9

    if i == 10:
        description = "其他应收款过多"
        if risk_grade[9] == 10:
            degree = 10
        elif risk_grade[9] == 8:
            degree = 8
        elif risk_grade[9] == 6:
            degree = 6
        elif risk_grade[9] == 4:
            degree = 4
        elif risk_grade[9] == 2:
            degree = 2
        else:
            degree = 0
        list_out_10 = [degree, description, add[9]]

        list_out[count_now1] = list_out_10

    if i == 11:
        description = "坏账计提标准过低"
        if risk_grade[10] == 10:
            degree = 10
        elif risk_grade[10] == 8:
            degree = 8
        elif risk_grade[10] == 6:
            degree = 6
        elif risk_grade[10] == 4:
            degree = 4
        elif risk_grade[10] == 2:
            degree = 2
        else:
            degree = 0
        list_out_11 = [degree, description, add[10]]

        list_out[count_now1] = list_out_11

    if i == 12:
        description = "企业多以预付账款模式支付"
        if risk_grade[11] == 10:
            degree = 10
        elif risk_grade[11] == 8:
            degree = 8
        elif risk_grade[11] == 6:
            degree = 6
        elif risk_grade[11] == 4:
            degree = 4
        elif risk_grade[11] == 2:
            degree = 2
        else:
            degree = 0
        list_out_12 = [degree, description, add[11]]

        list_out[count_now1] = list_out_12

    if i == 13:
        description = "预付款、预收款关联"
        if risk_grade[12] == 10:
            degree = 10
        elif risk_grade[12] == 8:
            degree = 8
        elif risk_grade[12] == 6:
            degree = 6
        elif risk_grade[12] == 4:
            degree = 4
        elif risk_grade[12] == 2:
            degree = 2
        else:
            degree = 0
        list_out_13 = [degree, description, add[12]]

        list_out[count_now1] = list_out_13

    if i == 14:
        description = "其他应收款过多"
        if risk_grade[13] == 10:
            degree = 10
        elif risk_grade[13] == 8:
            degree = 8
        elif risk_grade[13] == 6:
            degree = 6
        elif risk_grade[13] == 4:
            degree = 4
        elif risk_grade[13] == 2:
            degree = 2
        else:
            degree = 0
        list_out_14 = [degree, description, add[13]]

        list_out[count_now1] = list_out_14

    if i == 15:
        description = "存货计提跌价标准偏离行业"
        if risk_grade[14] == 10:
            degree = 10
        elif risk_grade[14] == 8:
            degree = 8
        elif risk_grade[14] == 6:
            degree = 6
        elif risk_grade[14] == 4:
            degree = 4
        elif risk_grade[14] == 2:
            degree = 2
        else:
            degree = 0
        list_out_15 = [degree, description, add[14]]

        list_out[count_now1] = list_out_15

    if i == 16:
        description = "虚构商品采购流出资金"
        if risk_grade[15] == 10:
            degree = 10
        elif risk_grade[15] == 8:
            degree = 8
        elif risk_grade[15] == 6:
            degree = 6
        elif risk_grade[15] == 4:
            degree = 4
        elif risk_grade[15] == 2:
            degree = 2
        else:
            degree = 0
        list_out_16 = [degree, description, add[15]]

        list_out[count_now1] = list_out_16

    if i == 17:
        description = "存货的计价方式变化"
        if risk_grade[16] == 10:
            degree = 10
        elif risk_grade[16] == 8:
            degree = 8
        elif risk_grade[16] == 6:
            degree = 6
        elif risk_grade[16] == 4:
            degree = 4
        elif risk_grade[16] == 2:
            degree = 2
        else:
            degree = 0
        list_out_17 = [degree, description, add[16]]

        list_out[count_now1] = list_out_17

    if i == 18:
        description = "固定资产折旧方法"
        if risk_grade[17] == 10:
            degree = 10
        elif risk_grade[17] == 8:
            degree = 8
        elif risk_grade[17] == 6:
            degree = 6
        elif risk_grade[17] == 4:
            degree = 4
        elif risk_grade[17] == 2:
            degree = 2
        else:
            degree = 0
        list_out_18 = [degree, description, add[17]]

        list_out[count_now1] = list_out_18

    if i == 19:
        description = "商誉过高"
        if risk_grade[18] == 10:
            degree = 10
        elif risk_grade[18] == 8:
            degree = 8
        elif risk_grade[18] == 6:
            degree = 6
        elif risk_grade[18] == 4:
            degree = 4
        elif risk_grade[18] == 2:
            degree = 2
        else:
            degree = 0
        list_out_19 = [degree, description, add[18]]

        list_out[count_now1] = list_out_19

    if i == 20:
        description = "虚增商誉"
        if risk_grade[19] == 10:
            degree = 10
        elif risk_grade[19] == 8:
            degree = 8
        elif risk_grade[19] == 6:
            degree = 6
        elif risk_grade[19] == 4:
            degree = 4
        elif risk_grade[19] == 2:
            degree = 2
        else:
            degree = 0
        list_out_20 = [degree, description, add[19]]

        list_out[count_now1] = list_out_20

    if i == 21:
        description = "区分无形资产与投资性房地产"
        if risk_grade[20] == 10:
            degree = 10
        elif risk_grade[20] == 8:
            degree = 8
        elif risk_grade[20] == 6:
            degree = 6
        elif risk_grade[20] == 4:
            degree = 4
        elif risk_grade[20] == 2:
            degree = 2
        else:
            degree = 0
        list_out_21 = [degree, description, add[20]]

        list_out[count_now1] = list_out_21

    if i == 22:
        description = "非高科技公司研发中的无形资产过多"
        if risk_grade[21] == 10:
            degree = 10
        elif risk_grade[21] == 8:
            degree = 8
        elif risk_grade[21] == 6:
            degree = 6
        elif risk_grade[21] == 4:
            degree = 4
        elif risk_grade[21] == 2:
            degree = 2
        else:
            degree = 0
        list_out_22 = [degree, description, add[21]]

        list_out[count_now1] = list_out_22

    if i == 23:
        description = "在建工程迟迟不转化为固定资产"
        if risk_grade[22] == 10:
            degree = 10
        elif risk_grade[22] == 8:
            degree = 8
        elif risk_grade[22] == 6:
            degree = 6
        elif risk_grade[22] == 4:
            degree = 4
        elif risk_grade[22] == 2:
            degree = 2
        else:
            degree = 0
        list_out_23 = [degree, description, add[22]]

        list_out[count_now1] = list_out_23

    if i == 24:
        description = "持有至到期投资大额减值"
        if risk_grade[23] == 10:
            degree = 10
        elif risk_grade[23] == 8:
            degree = 8
        elif risk_grade[23] == 6:
            degree = 6
        elif risk_grade[23] == 4:
            degree = 4
        elif risk_grade[23] == 2:
            degree = 2
        else:
            degree = 0
        list_out_24 = [degree, description, add[23]]

        list_out[count_now1] = list_out_24

    if i == 25:
        description = "持有至到期投资重分类"
        if risk_grade[24] == 10:
            degree = 10
        elif risk_grade[24] == 8:
            degree = 8
        elif risk_grade[24] == 6:
            degree = 6
        elif risk_grade[24] == 4:
            degree = 4
        elif risk_grade[24] == 2:
            degree = 2
        else:
            degree = 0
        list_out_25 = [degree, description, add[24]]

        list_out[count_now1] = list_out_25

    if i == 26:
        description = "投资性房地产"
        if risk_grade[25] == 10:
            degree = 10
        elif risk_grade[25] == 8:
            degree = 8
        elif risk_grade[25] == 6:
            degree = 6
        elif risk_grade[25] == 4:
            degree = 4
        elif risk_grade[25] == 2:
            degree = 2
        else:
            degree = 0
        list_out_26 = [degree, description, add[25]]

        list_out[count_now1] = list_out_26

    if i == 27:
        description = "有息负债率过高"
        if risk_grade[26] == 10:
            degree = 10
        elif risk_grade[26] == 8:
            degree = 8
        elif risk_grade[26] == 6:
            degree = 6
        elif risk_grade[26] == 4:
            degree = 4
        elif risk_grade[26] == 2:
            degree = 2
        else:
            degree = 0
        list_out_27 = [degree, description, add[26]]

        list_out[count_now1] = list_out_27

    if i == 28:
        description = "投资资产结构"
        if risk_grade[27] == 10:
            degree = 10
        elif risk_grade[27] == 8:
            degree = 8
        elif risk_grade[27] == 6:
            degree = 6
        elif risk_grade[27] == 4:
            degree = 4
        elif risk_grade[27] == 2:
            degree = 2
        else:
            degree = 0
        list_out_28 = [degree, description, add[27]]

        list_out[count_now1] = list_out_28

    if i == 29:
        description = "非主营业务收入占总收入比例过高"
        if risk_grade[28] == 10:
            degree = 10
        elif risk_grade[28] == 8:
            degree = 8
        elif risk_grade[28] == 6:
            degree = 6
        elif risk_grade[28] == 4:
            degree = 4
        elif risk_grade[28] == 2:
            degree = 2
        else:
            degree = 0
        list_out_29 = [degree, description, add[28]]
        list_out[count_now1] = list_out_29

    if i == 30:
        description = "持续的经营活动净现金流为负"
        if risk_grade[29] == 10:
            degree = 10
        elif risk_grade[29] == 8:
            degree = 8
        elif risk_grade[29] == 6:
            degree = 6
        elif risk_grade[29] == 4:
            degree = 4
        elif risk_grade[29] == 2:
            degree = 2
        else:
            degree = 0
        list_out_30 = [degree, description, add[29]]

        list_out[count_now1] = list_out_30

    if i == 31:
        description = "经营活动现金流净额远低于净利润"
        if risk_grade[30] == 10:
            degree = 10
        elif risk_grade[30] == 8:
            degree = 8
        elif risk_grade[30] == 6:
            degree = 6
        elif risk_grade[30] == 4:
            degree = 4
        elif risk_grade[30] == 2:
            degree = 2
        else:
            degree = 0
        list_out_31 = [degree, description, add[30]]

        list_out[count_now1] = list_out_31

    if i == 32:
        description = "企业毛利率较低"
        if risk_grade[31] == 10:
            degree = 10
        elif risk_grade[31] == 8:
            degree = 8
        elif risk_grade[31] == 6:
            degree = 6
        elif risk_grade[31] == 4:
            degree = 4
        elif risk_grade[31] == 2:
            degree = 2
        else:
            degree = 0
        list_out_32 = [degree, description, add[31]]

        list_out[count_now1] = list_out_32

    if i == 33:
        description = "管理费用显著高于同行业平均水平或高于上期水平"
        if risk_grade[32] == 10:
            degree = 10
        elif risk_grade[32] == 8:
            degree = 8
        elif risk_grade[32] == 6:
            degree = 6
        elif risk_grade[32] == 4:
            degree = 4
        elif risk_grade[32] == 2:
            degree = 2
        else:
            degree = 0
        list_out_33 = [degree, description, add[32]]

        list_out[count_now1] = list_out_33

    if i == 34:
        description = "研发费用显著高于同行业平均水平或高于上期水平"
        if risk_grade[33] == 10:
            degree = 10
        elif risk_grade[33] == 8:
            degree = 8
        elif risk_grade[33] == 6:
            degree = 6
        elif risk_grade[33] == 4:
            degree = 4
        elif risk_grade[33] == 2:
            degree = 2
        else:
            degree = 0
        list_out_34 = [degree, description, add[33]]

        list_out[count_now1] = list_out_34

    if i == 35:
        description = "销售费用显著高于同行业平均水平或高于上期水平"
        if risk_grade[34] == 10:
            degree = 10
        elif risk_grade[34] == 8:
            degree = 8
        elif risk_grade[34] == 6:
            degree = 6
        elif risk_grade[34] == 4:
            degree = 4
        elif risk_grade[34] == 2:
            degree = 2
        else:
            degree = 0
        list_out_35 = [degree, description, add[34]]

        list_out[count_now1] = list_out_35

    if i == 36:
        description = "购买固定资产，无形资产的支出，持续高于经营活动现金流量净额"
        if risk_grade[35] == 10:
            degree = 10
        elif risk_grade[35] == 8:
            degree = 8
        elif risk_grade[35] == 6:
            degree = 6
        elif risk_grade[35] == 4:
            degree = 4
        elif risk_grade[35] == 2:
            degree = 2
        else:
            degree = 0
        list_out_36 = [degree, description, add[35]]
        list_out[count_now1] = list_out_36

    if i == 37:
        description = "存货周转率低于行业平均水准"
        if risk_grade[36] == 10:
            degree = 10
        elif risk_grade[36] == 8:
            degree = 8
        elif risk_grade[36] == 6:
            degree = 6
        elif risk_grade[36] == 4:
            degree = 4
        elif risk_grade[36] == 2:
            degree = 2
        else:
            degree = 0
        list_out_37 = [degree, description, add[36]]
        list_out[count_now1] = list_out_37

    if i == 38:
        description = "欺诈性提升毛利率"
        if risk_grade[37] == 10:
            degree = 10
        elif risk_grade[37] == 8:
            degree = 8
        elif risk_grade[37] == 6:
            degree = 6
        elif risk_grade[37] == 4:
            degree = 4
        elif risk_grade[37] == 2:
            degree = 2
        else:
            degree = 0
        list_out_38 = [degree, description, add[37]]
        list_out[count_now1] = list_out_38

    if i == 40:
        description = "大量现金是由于出售固定资产和其他长期资产获得的利润"
        if risk_grade[39] == 10:
            degree = 10
        elif risk_grade[39] == 8:
            degree = 8
        elif risk_grade[39] == 6:
            degree = 6
        elif risk_grade[39] == 4:
            degree = 4
        elif risk_grade[39] == 2:
            degree = 2
        else:
            degree = 0
        list_out_40 = [degree, description, add[39]]
        list_out[count_now1] = list_out_40



List1 = [grade]
print(grade)
print(RTR, DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA, CH_REC, CH_INV, Soft_as, CH_CS, CH_ROA, ISSUE, OTHREC, STKCYC,
      LOSS)

print(list_out)
