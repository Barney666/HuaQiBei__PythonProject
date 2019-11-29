# from fancyimpute import KNN
import csv

import pandas as pd
import numpy as np
import math
import random
import xlrd
from sklearn.cluster import DBSCAN
import json


def compare(a, b):
    return (b - a) / a


# 读取
def sjqx(temp_list):
    temp_has = []
    s = pd.Series(temp_list)
    if s.isnull().sum() / (s.shape[0]) > 0.8:
        s.fillna(s.mean, inplace=True)
        temp_list = s.tolist()
    else:
        for i in range(len(temp_list)):
            # print(temp_list[i])
            if np.isnan(temp_list[i]) == False:
                temp_has.append(i)
                if temp_list[i] == 0:
                    temp_list[i] = temp_list[i] + 1
        # print(temp_has)
        for j in range(0, len(temp_has) - 1):
            if temp_has[j + 1] - temp_has[j] > 1:
                for k in range(temp_has[j] + 1, temp_has[j + 1]):
                    temp_list[k] = temp_list[temp_has[j]] + (temp_list[temp_has[j + 1]] - temp_list[temp_has[j]]) * (
                            k - temp_has[j]) / (temp_has[j + 1] - temp_has[j])
        # print(temp_list)
        for k in range(temp_has[0] - 1, -1, -1):
            temp_list[k] = temp_list[temp_has[0]] - (temp_has[0] - k) * (
                    temp_list[temp_has[0] + 1] - temp_list[temp_has[0]])
        for k in range(temp_has[len(temp_has) - 1], len(temp_list)):
            temp_list[k] = temp_list[temp_has[len(temp_has) - 1]] + (k - temp_has[len(temp_has) - 1]) * (
                    temp_list[temp_has[len(temp_has) - 1]] - temp_list[temp_has[len(temp_has) - 2]])

    return temp_list


def collect(num, result, lm):
    temp_list = []

    for date in ["2019-09-30", "2019-06-30", "2019-03-31", "2018-12-31", "2018-09-30", "2018-06-30",
                 "2017-12-31", "2016-12-31", "2015-12-31", "2014-12-31", "2013-12-31"]:
        if result['report'][lm][date][num] == '--':
            a = np.NAN
        else:
            a = float(result['report'][lm][date][num])
        temp_list.append(a)
    temp_list1 = sjqx(temp_list)
    return temp_list1


def read(code):
    import pandas as pd
    import xlrd
    result = {}

    report = {}

    import os
    os.chdir(os.path.dirname(__file__))
    debt = "report\\1\\"  # 要加code.csv
    # debt = "D:\\360MoveData\\Users\\Fanghao\\Desktop\\4\\report期\\资产负债表\\"  # 要加code.csv
    debt_dic = {}
    profit = 'report\\2\\'
    # profit = 'D:\\360MoveData\\Users\\Fanghao\\Desktop\\4\\report\\利润表\\'
    profit_dic = {}
    main = 'report\\3\\'
    # main = 'D:\\360MoveData\\Users\\Fanghao\\Desktop\\4\\report\\主要财务指标\\'
    main_dic = {}
    flow = 'report\\4\\'
    # flow = 'D:\\360MoveData\\Users\\Fanghao\\Desktop\\4\\report\\现金流量表\\'
    flow_dict = {}

    basic = '公司名称与股票代码的对应关系.csv'
    basic_dic = {}
    peer = '15.xlsx'  # 注意这是xlsx的 不是csv
    peer_list = []
    conference = '开临时股东大会的次数.csv'
    conference_list = []

    # report
    count = 0
    pathList = [debt, profit, main, flow]
    for dict in [debt_dic, profit_dic, main_dic, flow_dict]:
        file = pd.read_csv(f"{pathList[count]}{code}.csv", encoding='gbk')
        for date in ["2019-09-30", "2019-06-30", "2019-03-31", "2018-12-31", "2018-09-30", "2018-06-30",
                     "2017-12-31", "2016-12-31", "2015-12-31", "2014-12-31", "2013-12-31"]:
            list = []
            for i in range(0, len(file[date])):
                list.append(file[date][i])
            dict[date] = list
        count += 1
    for fold in ["profit", "repay", "grow", "operation"]:
        path = main + fold + "/" + code + ".csv"
        file = pd.read_csv(path, encoding='gbk')
        for date in ["2019-09-30", "2019-06-30", "2019-03-31", "2018-12-31", "2018-09-30", "2018-06-30"]:
            list = main_dic.get(date)
            for i in range(0, len(file[date])):
                list.append(file[date][i])
    for fold in ["profit", "repay", "grow", "operation"]:  # 按顺序接下去
        path = f"annual\\3\\{fold}\\{code}.csv"  # TODO 不同pc要改
        file = pd.read_csv(path, encoding='gbk')
        for date in ["2017-12-31", "2016-12-31", "2015-12-31", "2014-12-31", "2013-12-31"]:
            list = main_dic.get(date)
            for i in range(0, len(file[date])):
                list.append(file[date][i])
    report["debt"] = debt_dic
    report["profit"] = profit_dic
    report["main"] = main_dic
    report["flow"] = flow_dict

    result["report"] = report

    # basic
    file = pd.read_csv(basic, index_col=0, converters={'Code': str}, encoding='utf-8')  #TODO 原先是gbk
    name = ""
    for i in range(1, len(file['Code'])):
        if str(file['Code'][i]) == code:
            name = file['Name'][i]
    basic_dic['Name'] = name
    basic_dic['Code'] = code
    result["basic"] = basic_dic

    # peer
    data = xlrd.open_workbook(peer)  # 打开文件
    worksheet = data.sheet_by_index(0)  # 通过sheet索引获得sheet对象
    for i in range(0, worksheet.nrows):  # worksheet.nrows---获取该表总行数
        temp = str(int(worksheet.cell_value(i, 3)))
        while len(temp) != 6:
            temp = "0" + temp
        if temp == code:
            if worksheet.cell_value(i, 2) == "":  # 中间
                for j in range(1, worksheet.nrows):  # 往上走
                    temp = str(int(worksheet.cell_value(i - j, 3)))
                    while len(temp) != 6:
                        temp = "0" + temp
                    peer_list.append(temp)
                    if i - j == 0:  # 第一行
                        break
                    if worksheet.cell_value(i - j, 2) != "" and worksheet.cell_value(i - j - 1, 2) == "":
                        break
                for j in range(1, worksheet.nrows):  # 往下走
                    temp = str(int(worksheet.cell_value(i + j, 3)))
                    while len(temp) != 6:
                        temp = "0" + temp
                    peer_list.append(temp)
                    if worksheet.cell_value(i + j + 1, 2) != "":
                        break
            if i == 0 or (worksheet.cell_value(i, 2) != "" and worksheet.cell_value(i - 1, 2) == ""):  # 最上面
                for j in range(1, worksheet.nrows):  # 往下走
                    temp = str(int(worksheet.cell_value(i + j, 3)))
                    while len(temp) != 6:
                        temp = "0" + temp
                    peer_list.append(temp)
                    if worksheet.cell_value(i + j + 1, 2) != "":
                        break
            if i == 3639 or (worksheet.cell_value(i, 2) == "" and worksheet.cell_value(i + 1, 2) != ""):  # 最下面
                for j in range(1, worksheet.nrows):  # 往上走
                    temp = str(int(worksheet.cell_value(i - j, 3)))
                    while len(temp) != 6:
                        temp = "0" + temp
                    peer_list.append(temp)
                    if i - j == 0:  # 第一行
                        break
                    if worksheet.cell_value(i - j, 2) != "" and worksheet.cell_value(i - j - 1, 2) == "":
                        break
            break
    result["peer"] = peer_list

    # conference
    file = pd.read_csv(conference, index_col=0, converters={'Code': str})
    temp18 = ""
    temp17 = ""
    for i in range(0, len(file['Code'])):
        if str(file['Code'][i]) == code:
            temp18 = file['2018'][i]
            temp17 = file['2017'][i]
    conference_list.append(temp18)
    conference_list.append(temp17)
    result["conference"] = conference_list

    # factor
    factor = {}
    mll = collect(30, result, 'main')
    factor['mll'] = mll
    yfzk = collect(6, result, 'debt')
    factor['yfzk'] = yfzk
    zzc = collect(13, result, 'main')
    jlr = collect(39, result, 'profit')
    factor['jlr'] = jlr
    ldfz = collect(83, result, 'debt')
    factor['ldfz'] = ldfz
    lxzc = collect(9, result, 'profit')
    # factor['lxzc'] = lxzc
    lxsr = collect(2, result, 'profit')
    # factor['lxsr'] = lxsr
    zfz = collect(15, result, 'main')
    factor['zfz'] = zfz
    ch = collect(19, result, 'debt')
    gdzc = collect(34, result, 'debt')
    # aqi = [x - y - z for x, y, z in zip(zzc, ch, gdzc)]
    # factor['aqi'] = aqi
    yysr = collect(0, result, 'profit')
    factor['yysr'] = yysr
    yycb = collect(7, result, 'profit')
    factor['yycb'] = yycb
    ljzj = collect(33, result, 'debt')
    gdzcyz = collect(32, result, 'debt')
    zjl = [x / y for x, y in zip(ljzj, gdzcyz)]
    # factor['zjl'] = zjl
    selling_cost = collect(20, result, 'profit')
    management_cost = collect(21, result, 'profit')
    research_cost = collect(12, result, 'profit')
    goodwill = collect(45, result, 'debt')
    factor['goodwill'] = goodwill
    inmains = [i for i in range(0, 55)]
    for inmain in inmains:
        factor["main" + str(inmain)] = collect(inmain, result, 'main')
    result['factor'] = factor

    # judge
    judge = {}
    mll = collect(30, result, 'main')
    judge['mll'] = mll
    hbzj = collect(0, result, 'debt')
    judge['hbzj'] = hbzj
    yfzk = collect(6, result, 'debt')
    judge['yfzk'] = yfzk
    zzc = collect(13, result, 'main')
    judge['zzc'] = zzc
    jlr = collect(39, result, 'profit')
    judge['jlr'] = jlr
    ldfz = collect(83, result, 'debt')
    judge['ldfz'] = ldfz
    lxzc = collect(9, result, 'profit')
    lxsr = collect(2, result, 'profit')
    zfz = collect(15, result, 'main')
    judge['zfz'] = zfz
    ch = collect(19, result, 'debt')
    gdzc = collect(34, result, 'debt')
    # aqi = [x - y - z for x, y, z in zip(zzc, ch, gdzc)]
    # factor['aqi'] = aqi
    yysr = collect(0, result, 'profit')
    judge['yysr'] = yysr
    yycb = collect(7, result, 'profit')
    judge['yycb'] = yycb
    ljzj = collect(33, result, 'debt')
    gdzcyz = collect(32, result, 'debt')
    zjl = [x / y for x, y in zip(ljzj, gdzcyz)]
    # factor['zjl'] = zjl
    selling_cost = collect(20, result, 'profit')
    management_cost = collect(21, result, 'profit')
    research_cost = collect(12, result, 'profit')
    goodwill = collect(45, result, 'debt')
    judge['goodwill'] = goodwill
    qtysk = collect(13, result, 'debt')
    judge['qtysk'] = qtysk
    inmains = [i for i in range(0, 55)]
    for inmain in inmains:
        judge["main" + str(inmain)] = collect(inmain, result, 'main')
    result['judge'] = judge

    return result


# bp
def intoflo(list_lz):
    max = float(list_lz[0])
    min = float(list_lz[0])
    for lz in range(len(list_lz)):
        if float(list_lz[lz]) > max:
            max = float(list_lz[lz])
        if float(list_lz[lz]) < min:
            min = float(list_lz[lz])
    wb = [float(list_lz[0])]
    tbl = []
    for i in range(1, 6):
        tbl.append(float(list_lz[i]))
    aim = [tbl, wb]
    return aim, max, min


def random_number(a, b):
    return (b - a) * random.random() + a


def makematrix(m, n, fill=0.0):
    a = []
    for i in range(m):
        a.append([fill] * n)
    return a


def sigmoid(x):
    return math.tanh(x)


def derived_sigmoid(x):
    return 1.0 - x ** 2


class BPNN:
    def __init__(self, num_in, num_hidden, num_out):

        self.num_in = num_in + 1
        self.num_hidden = num_hidden + 1
        self.num_out = num_out

        self.active_in = [1.0] * self.num_in
        self.active_hidden = [1.0] * self.num_hidden
        self.active_out = [1.0] * self.num_out

        self.wight_in = makematrix(self.num_in, self.num_hidden)
        self.wight_out = makematrix(self.num_hidden, self.num_out)

        for i in range(self.num_in):
            for j in range(self.num_hidden):
                self.wight_in[i][j] = random_number(-0.2, 0.2)
        for i in range(self.num_hidden):
            for j in range(self.num_out):
                self.wight_out[i][j] = random_number(-0.2, 0.2)

        self.ci = makematrix(self.num_in, self.num_hidden)
        self.co = makematrix(self.num_hidden, self.num_out)

    def update(self, inputs):
        if len(inputs) != self.num_in - 1:
            raise ValueError('与输入层节点数不符')

        for i in range(self.num_in - 1):
            # self.active_in[i] = sigmoid(inputs[i])
            self.active_in[i] = inputs[i]

        for i in range(self.num_hidden - 1):
            sum = 0.0
            for j in range(self.num_in):
                sum = sum + self.active_in[i] * self.wight_in[j][i]
            self.active_hidden[i] = sigmoid(sum)

        for i in range(self.num_out):
            sum = 0.0
            for j in range(self.num_hidden):
                sum = sum + self.active_hidden[j] * self.wight_out[j][i]
            self.active_out[i] = sigmoid(sum)

        return self.active_out[:]

    def errorbackpropagate(self, targets, lr, m):
        if len(targets) != self.num_out:
            raise ValueError('与输出层节点数不符！')

        out_deltas = [0.0] * self.num_out
        for i in range(self.num_out):
            error = targets[i] - self.active_out[i]
            out_deltas[i] = derived_sigmoid(self.active_out[i]) * error

        hidden_deltas = [0.0] * self.num_hidden
        for i in range(self.num_hidden):
            error = 0.0
            for j in range(self.num_out):
                error = error + out_deltas[j] * self.wight_out[i][j]
            hidden_deltas[i] = derived_sigmoid(self.active_hidden[i]) * error

        for i in range(self.num_hidden):
            for j in range(self.num_out):
                change = out_deltas[j] * self.active_hidden[i]
                self.wight_out[i][j] = self.wight_out[i][j] + lr * change + m * self.co[i][j]
                self.co[i][j] = change

        for i in range(self.num_in):
            for i in range(self.num_hidden):
                change = hidden_deltas[j] * self.active_in[i]
                self.wight_in[i][j] = self.wight_in[i][j] + lr * change + m * self.ci[i][j]
                self.ci[i][j] = change

        error = 0.0
        for i in range(len(targets)):
            error = error + 0.5 * (targets[i] - self.active_out[i]) ** 2
        return error

    def test(self, patterns):
        for i in patterns:
            pass
            # print(i[0], '->', self.update(i[0]))
        return self.update(i[0])

    def weights(self):
        print("输入层权重")
        for i in range(self.num_in):
            print(self.wight_in[i])
        print("输出层权重")
        for i in range(self.num_hidden):
            print(self.wight_out[i])

    def train(self, pattern, itera=1000, lr=0.1, m=0.1):
        for i in range(itera):
            error = 0.0
            for j in pattern:
                inputs = j[0]
                targets = j[1]
                self.update(inputs)
                error = error + self.errorbackpropagate(targets, lr, m)
            # if i % 100 == 0:
            # print('误差 %-.5f' % error)


def bpdemo(dic_for_train, foraim, max, min):
    n = BPNN(5, 5, 1)
    n.train(dic_for_train)
    p = n.test([foraim])[0]
    return p * (max - min) + min
    # n.weights()


# jl
def jl(code):
    companys = read(code)['peer']
    #companys.append(code)

    listsc = {}
    for company in companys:
        list_temp = []
        for data in ["2018-12-31",
                     "2017-12-31", "2016-12-31", "2015-12-31", "2014-12-31", "2013-12-31"]:
            list_temp.append(read(company)['report']['main'][data][3])
        listsc[company] = list_temp
    # print(listsc)
    return listsc


def getsjdate(dic, num, listname):
    for i in range(6):
        sum = 0
        for key in dic:
            sum = sum + float(dic[key][i])
        for key in dic:
            dic[key][i] = float(dic[key][i]) / sum

    plx = []
    ply = []

    for key in dic:
        plx.append(dic[key][0])
        zzl = (dic[key][0] - dic[key][1]) / dic[key][1]
        ply.append(zzl)
    # plt.scatter(plx, ply, color='red', marker='+')
    # plt.show()
    xx = list(zip(plx, ply))

    X = np.array(xx)

    db = DBSCAN(eps=0.12, min_samples=2).fit(X)
    labels = db.labels_
    px = {}
    dictforqz = {}
    max = 0
    for i in range(len(labels)):
        if labels[i] > max:
            max = labels[i]
    for j in range(max+1):
        list_temp = []
        sumzzl = 0
        sumplx = 0
        count = 0
        for i in range(len(labels)):
            if labels[i] == j:
                list_temp.append((labels[i], listname[i]))
                sumzzl = sumzzl + ply[i]
                sumplx = sumplx + plx[i]
                count = count + 1
        dictforqz[j] = (sumzzl + sumplx) / count
        px[j] = list_temp
    tempa = sorted(dictforqz.items())
    for i in range(len(labels)):
        if labels[i] == -1:
            if ply[i]+plx[i] < tempa[len(tempa)-1][1]:
                labels[i] = max + 1
    labels = labels.tolist()
    labels.append(0)

    return labels


# svc

def svc(listsvc):
    from sklearn.externals import joblib
    cfl = joblib.load('svntry.pkl')

    return cfl.predict(listsvc)


# judge

def judge(result, list_hy, code, pc):
    jlist = []
    # if float(result['judge']['tzsy'][0]) / float(result['judge']['zyywsr'][0]) > 0.5:
    # jlist.append('收入结构有较大风险')

    if float(result['judge']['goodwill'][0] / result['judge']['zzc'][0]) > 1.5 * list_hy['goodwill'] / list_hy['zzc']:
        jlist.append('商誉过高')

    with open('F:\\Result_of_Whether.csv', 'r', encoding='gbk') as csvfile5:
        reader4 = csv.reader(csvfile5)
        for i, rows in enumerate(reader4):
            row = rows
            if row:
                name_of_this = row[1]
            if name_of_this == code:
                jud = row[3]
                if jud == "FALSE":
                    Opinion = "标准无保留意见"
                else:
                    Opinion = "非标准"
                break
    if Opinion != "标准无保留意见":
        jlist.append('会计师出具意见不是标准无保留意见')
    if float(result['judge']['yfzk'][0]) / float(result['judge']['hbzj'][0]) > 0.3:
        jlist.append('存贷双高')
    if float(result['judge']['qtysk'][0] / result['judge']['zzc'][0]) > 3 * list_hy['qtysk'] / list_hy['zzc']:
        jlist.append('异常的其他应收款')
    count = 0
    f = pd.read_table('1.txt', header=None, encoding='gbk')
    f = np.array(f)
    for p in pc:
        if p != 1:
            if p > 0.4:
                try:
                    jlist.append(str(f[0][count]) + '向上偏离预测值')
                except:
                    pass
            if p < -0.2:
                try:
                    jlist.append(str(f[0][count]) + '向下偏离预测值')
                except:
                    pass
        count = count + 1

    return jlist


def grade(input, nin, nhidden, nout):
    wight_in = [
        [6.256676257735021, -0.038227064159439605, 0.14994969765739175, -0.15903207055025162, -0.12622820923177225,
         0.19103964857075645, -0.0873541016337994, 0.038765345533140344, -0.1511098401930523, -0.14308957673308564,
         -0.0552397919004842],
        [
            -25.499707428321166, 0.04389493042374601, 0.13961670361160777, -0.010876674284311216, 0.1950889576695532,
            -0.12916823723696125, 0.12877289417895627, 0.1556104848994973, -0.1424408599822896, -0.17908991155575993,
            0.029158575694790884],
        [
            -419.9200529790457, 0.06453655867117841, 0.1785277465639955, 0.09780921796081926, -0.1384703956065324,
            0.17872474416028233, 0.19045026680786753, -0.15558683463594317, -0.0853955849727952, -0.06443176503601541,
            -0.1967879949842411],
        [
            16.022768036428314, -0.09723042823685746, -0.07044940568553432, -0.17556786579617212, 0.04282047795875221,
            -0.07528793432841147, -0.13572341503818647, 0.045427395896152994, 0.08614639831752513, 0.13804635032338491,
            0.1742332525292774],
        [
            5.304638481261136, 0.19738122158725196, -0.10635091053464625, -0.1690000821694666, 0.0816467631496472,
            -0.02655647360065272, 0.10188887627763671, 0.19337304323952192, 0.019601098147881635, 0.07369774844418014,
            -0.017957128957802077],
        [
            -109.36617498464012, -0.0802387245111727, 0.15620463012514102, -0.05183582807455403, -0.037451999682463016,
            0.07030580582011015, -0.09350840891319884, 0.16894066286420295, -0.15649603780151677, -0.10229469972345254,
            0.07620872230254794],
        [
            -94.92974528865953, 0.18522152620136206, 0.11017091518949379, 0.12562600689362946, 0.17417307437991153,
            0.0979589306951858, 0.11918993125001881, 0.021401301170276138, 0.1988575036868349, -0.1453724033799297,
            0.14021698755948692],
        [
            9.4652388384664, -0.10059537628478377, 0.07211483234910393, -0.09651646581045181, 0.03556867915149353,
            0.005716362118431961, -0.18833552742350196, -0.18802996529782795, -0.004239485484972244,
            0.10366239904947067, -0.08499703098310536],
        [
            -346.6724338066451, -0.18951657275947487, 0.19653417808322798, 0.07045655290056002, 0.0873353238062925,
            0.07996472511904879, 0.002813970953472994, -0.03499553464451516, 0.12761788881113562, -0.02274505045993283,
            0.17845457896343264],
        [
            -0.2353163890223987, 0.05249856448709156, -0.18113640710171072, -0.11041538812078606, -0.030948483518805997,
            0.17106234536015275, -0.021518044879734022, -0.1858169767348227, -0.041618838460813073, 0.18373223884212025,
            -0.10101010021801571],
        [
            -1.171023729633018, 0.08582887524258676, -0.06414242535254658, 0.008887380667658457, 0.1303818351841503,
            -0.12511799795010195, 0.19565066444250456, -0.07591531636342985, 0.05240932478727689, 0.11048426525217753,
            0.06339124227102177],
        [
            0.17611587592124295, -0.042788910776095035, 0.024128323048407785, -0.07965335337329292,
            -0.06144020577787823, 0.1566243926091721, 0.019831148387947917, -0.17308424803001074, -0.11209152774355893,
            0.02832092366177333, 0.12214725148728223],
        [
            -0.1844083289356866, -0.03208410658597871, -0.08391375087294045, -0.16487541115279747, -0.1806713607130254,
            -0.031950949223412545, -0.055871789819183004, -0.06760948389410104, 0.1832058081096053,
            -0.08717723394143757, -0.05171223326198576],
        [
            -0.10916771514468677, 0.05432817948715363, 0.142749369822246, -0.16944154406914227, 0.11309889064444922,
            -0.04669440838971922, -0.0917880183815111, 0.03228478824914616, 0.16101664671719962, -0.074235766779046,
            0.03284790886570438],
        [
            -0.07384079189211556, -0.056938118765983425, 0.05248324043177033, -0.1786583794812463, -0.11129454756840135,
            0.022654149101951904, -0.13204256009369558, 0.06613156038428708, -0.0792724917870653, 0.03249115401605995,
            -0.0694726679566236],
        [
            0.025339947024822285, 0.07064689547704583, -0.16733707523816688, -0.053893655085233555, 0.14188066351307144,
            0.13644600248073907, -0.06742106963696481, -0.006041336559373889, -0.12877712125496554,
            -0.047636421365958664, 0.057217493093432825],
        [
            0.11071586501483677, 0.004325637824507067, 0.049035381623563135, -0.11468067949763001, 0.16011619089123313,
            -0.029035777753417508, 0.144527744673988, -0.12355781756158053, 0.19511123166629185, 0.13597191058376307,
            0.19363550784100048],
        [
            -0.04475337916910421, -0.16857758292852532, 0.19931086294898143, -0.07846143127843011, 0.14683082107623596,
            -0.15759078622386735, 0.026565051426099495, -0.08731051846500933, 0.14251665438382494,
            0.0006271081701368642, -0.023105154354562257],
        [
            -0.10384694670875363, -0.11157969440913598, 0.08437218378401656, 0.06755885358846203, 0.003875382719490117,
            -0.016756214334346792, 0.1870073295079418, 0.10589445333912245, -0.07933072318104469, 0.16122671934562594,
            -0.0047126722278515165],
        [
            0.007902801711863555, 0.15628573450049088, -0.018614406523693672, 0.05065718467668029,
            -0.0028576272299280503, -0.18995839434970488, -0.1257147093608424, 0.06225703402756527,
            0.0019650516022197695, -0.031335071371004636, 0.1703937009568396],
        [
            -0.06964662841645261, -0.17579115488586622, -0.04543664528578226, 0.07730714881380207, 0.18323718889546975,
            0.16711685807147314, -0.07880514834497748, 0.0902853256831817, -0.19186370234942826, -0.05527043723109051,
            0.18132622783377145]

    ]

    wight_out = [[0.05809243433940223],
                 [-0.18612653814414826],
                 [0.020220242148929958],
                 [-0.026718116399207317],
                 [-0.1180310602108514],
                 [0.34313025725793384],
                 [-5.651957625454781],
                 [0.07569048004005793],
                 [0.8171442021707452],
                 [-0.26988568095873],
                 [0.01689650820114045],
                 ]
    wight_in = np.array(wight_in)
    wight_out = np.array(wight_out)
    activein = [1.0] * nin
    activehidden = [1.0] * nhidden
    activeout = [1.0] * nout
    for i in range(nin - 1):
        activein[i] = input[i]
    for i in range(nhidden - 1):
        sum = 0.0
        for j in range(nin):
            sum = sum + activein[i] * wight_in[j][i]
        activehidden[i] = sigmoid(sum)  # active_hidden[]是处理完输入数据之后存储，作为输出层的输入数据
    for i in range(nout):
        sum = 0.0
        for j in range(nhidden):
            sum = sum + activehidden[j] * wight_out[j][i]
        activeout[i] = sigmoid(sum)  # 与上同理
    grade = (activeout[:][0] - 0.2) * 20 + 100
    if grade > 97:
        grade = 97
    if grade < 30:
        grade = 30
    return grade


def bptry(code, key1):
    result = read(code)
    yclist = []
    zslist = []
    for key in [key1]:
        zsz = result['factor'][key][0]
        zslist.append(zsz)
        (foraim, max, min) = intoflo(result['factor'][key])
        dic_for_train_t = []
        dic_for_train = []
        # factororhy = []
        # count = len(result['peer'])
        # flag = 0
        for strx in result['peer']:
            per = read(strx)
            # if flag == 0:
            # factororhy = per['factor']
            # print(factororhy)
            # flag = 1
            # else:
            # for i in per['factor']:
            # for j in range(len(per['factor'][i])):
            # factororhy[i][j] = factororhy[i][j] + float(per['factor'][i][j])
            (faim, max2, min2) = intoflo(per['factor'][key])
            if max2 > max:
                max = max2
            if min2 < min:
                min = min2
            if np.isnan(faim[1][0]) == False:
                dic_for_train_t.append(faim)
        '''
        for key in factororhy:
            for j in range(factororhy[key]):
               factororhy[key][j] = factororhy[key][j] / count
        '''
        foraim = [[(float(x) - min) / (max - min) for x in foraim[0]], [(float(foraim[1][0]) - min) / (max - min)]]
        for aim in dic_for_train_t:
            aim = [[(float(x) - min) / (max - min) for x in aim[0]], [(float(aim[1][0]) - min) / (max - min)]]
            dic_for_train.append(aim)
        ycz = bpdemo(dic_for_train, foraim, max, min)
        yclist.append(ycz)
    print(yclist)
    print(zslist)


def gethy(listname):
    bj = {}
    length = len(listname)
    flag = 0
    for company in listname:
        try:
            res = read(company)
            if flag == 0:
                for key in res['judge']:
                    bj[key] = 0
                flag = len(res['judge'])
            for key in res['judge']:
                try:
                    bj[key] = bj[key] + res['judge'][key][0]
                except:
                    pass

        except:
            length = length - 1

    for key in bj:
        bj[key] = bj[key] / length

    return bj


def gethyn(code):
    peer = 'F:\\15.xlsx'
    data = xlrd.open_workbook(peer)
    table = data.sheets()[0]
    nrows = table.nrows
    re = 0
    for i in range(nrows):
        row = table.row_values(i)
        if i == 0:
            last_name = str(row[1])
        if str(row[1]) == last_name or row[1] == '':
            pass
        else:
            last_name = str(row[1])
            re = re + 1
        temp = str(int(row[3]))
        while len(temp) < 6:
            temp = "0" + temp
        if temp == code:
            break
    return re


def readjuz(res, code):
    path = 'fh1\\'
    count = 0
    ycz = []
    zsz = []
    name = []
    for key in res['factor']:

        try:
            path1 = path + str(gethyn(code)) + str(key) + 'inw.txt'
            path2 = path + str(gethyn(code)) + str(key) + 'outw.txt'
            path3 = path + str(gethyn(code)) + str(key) + 'maxmin.txt'
            data1 = pd.read_table(path1, header=None)
            datafg1 = eval(str(data1[0][0]))
            data2 = pd.read_table(path2, header=None)
            datafg2 = eval(str(data2[0][0]))
            data3 = pd.read_table(path3, header=None)
            max = float(str(data3[0][0]).split('  ')[0])
            min = float(str(data3[0][0]).split('  ')[1])
            wight_in = np.array(datafg1)
            wight_out = np.array(datafg2)
            nin = 6
            nhidden = 5
            nout = 1
            (foraim, max1, min1) = intoflo(result['factor'][key])
            activein = [1.0] * nin
            activehidden = [1.0] * nhidden
            activeout = [1.0] * nout
            for i in range(nin - 1):
                activein[i] = foraim[0][i]
            for i in range(nhidden - 1):
                sum = 0.0
                for j in range(nin):
                    sum = sum + activein[i] * wight_in[j][i]
                activehidden[i] = sigmoid(sum)  # active_hidden[]是处理完输入数据之后存储，作为输出层的输入数据
            for i in range(nout):
                sum = 0.0
                for j in range(nhidden):
                    sum = sum + activehidden[j] * wight_out[j][i]
                activeout[i] = sigmoid(sum)  # 与上同理
            ycz.append(activeout[:][0] * (max1 - min1) + min1)
            zsz.append(foraim[1][0])
            name.append(key)
            count = 1
        except:
            ycz.append(-1)
            zsz.append(-1)
            name.append(key)

    return ycz, zsz, name


if __name__ == '__main__':
    import sys
    code = sys.argv[1]
    # code = "000001"

    result = read(code)
    listname = result['peer']
    listname.append(code)

    flag = 0
    if len(listname) == 1:
        flag = 1

    ycz, zsz, name = readjuz(result, code)
    pc = [compare(a, b) for a, b in zip(zsz, ycz)]

    listz = gethy(listname)
    # tempjudge = judge(result, listz, code, pc)

    listgra = []

    for key in result['factor']:
        try:
            listgra.append((result['factor'][key][0] - result['factor'][key][1]) / result['factor'][key][1])
        except:
            listgra.append(0)

    grad = grade(listgra, 20, 10, 1)
    if flag == 1:
        grad = -1

    shuchu = {"yuce": ycz, "zhenshi": zsz, "piancha": pc, "fenshu": grad}
    # shuchu = {"yuce": ycz, "zhenshi": zsz, "piancha": pc, "daima": pc,
    #           "fenlei": getsjdate(jl(code), 1, listname), "fenshu": grad}
    # shuchu = {"yuce": ycz, "zhenshi": zsz, "piancha": pc, "daima": pc,
    #           "fenlei": getsjdate(jl(code), 1, listname), "fenshu": grad, 'wenzi': tempjudge}
    print(json.dumps(shuchu, ensure_ascii=False))
