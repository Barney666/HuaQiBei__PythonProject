# encoding: utf-8
import requests
import json
import csv
import re
import time
import urllib
from urllib.request import urlopen
import matplotlib.pyplot as plt

from w3lib.html import remove_tags
from aip import AipNlp
from wordcloud import WordCloud

APP_ID = '17709404'
API_KEY = '48MSTrIOptHOUDY1set0mook'
SECRET_KEY = 'voGbVRltY9l3QIiaZPnpM1WU2OdAAPnW'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

data_list = []
data_ms = []
data_fx = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Cookie': 'acw_tc=276082a615733656152228566e90acfc4ed72e6b7bc00d63b950d4a29c580e; device_id=593729a380b6dd2660e80d7ef09d468a; s=cm12n5ex19; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_a_token=cc8312389bbfba4e8b4a4c4786554c68f8cdff85; xq_a_token.sig=MVpeq8FzU-gWMCfEpKp6nedVRCc; xqat=cc8312389bbfba4e8b4a4c4786554c68f8cdff85; xqat.sig=C5CtRfPusk5lrN-J4A0f8d9SoIc; xq_r_token=c4dac0182125e9cab8c7a70d84b6e2fd7b6f439b; xq_r_token.sig=UIPoUHMFyZ9BvRdtsMllPlwSmto; xq_is_login=1; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u=7433374099; u.sig=yK6d4_Wh4NEH6jcADqFUQrEtG8I; bid=a8c02f0e6f438b7dd878fcc0e8f100d7_k2v8gm6u; __utmz=1.1573525522.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=1.24640007.1573525522.1573525522.1573961454.2; aliyungf_tc=AQAAAHcZpWatMQwAcFGi0yISechCu8gN; Hm_lvt_1db88642e346389874251b5a1eded6e3=1573718049,1573957020,1573959764,1573987925; snbim_minify=true; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1573988716'
}


def get_index(url):
    # 请求的url
    # url = 'https://xueqiu.com/statuses/search.json?sort=relevance&source=all&q=%E8%A7%86%E8%A7%89%E4%B8%AD%E5%9B%BD&count=10&page=' + str(
    # number)

    # print(url)
    # 返回来的数据是json格式
    resp = requests.get(url, headers=headers).json()
    if resp:
        return resp
    else:
        return None


def start_spider(resp):
    # 判断数据是否存在
    if resp:
        # 我们需要的数据存在一个列表之中，先取出这个列表

        lists = resp.get('list')
        # 判断列表是否存在，然后遍历
        if lists:
            for temp in lists:

                # 获取文章的题目
                title = temp.get('title')
                title = remove_tags(title)
                # 如果没有题目，就continue，因为通过我的观察，没有title的一般是广告之类的
                if not title:
                    continue
                # 获取摘要
                description = temp.get('description')
                # 数据清洗，使用正则表达式的sub方法
                description = remove_tags(description)
                # 获取用户的信息，用户的信息在data里边的user键中
                user_name = temp.get('user').get('screen_name')
                # 获取是什么类型的文章
                column = temp.get('column')
                # 获取发表的时间戳
                created_at = temp.get('timeBefore')
                try:
                    created_at = created_at.split(' ')[0].split('-')
                    created_at = int(created_at[0] + created_at[1])
                except:
                    created_at = 0
                # 获取阅读人数
                view_count = temp.get('view_count')
                # 获取连接
                target = temp.get('target')
                hot = [temp.get('retweet_count'), temp.get('reply_count'), temp.get('fav_count')]
                text = temp.get('text')
                #text = remove_tags(text)

                # 声明一个字典存储数据
                data_dict = {}
                data_dict['title'] = title
                data_dict['description'] = description
                data_dict['user_name'] = user_name
                data_dict['column'] = column
                data_dict['created_at'] = created_at
                data_dict['view_count'] = view_count
                data_dict['target'] = target
                data_dict['hot'] = hot
                data_dict['text'] = text
                # 判断字典数据是否以及存在了列表，相当于是去重，将字典存入列表中
                if data_dict not in data_list:
                    data_list.append(data_dict)
                    # print(data_dict)
            # 设置一个flag并返回来判断是否没有数据了
            return True

        else:
            return None


def readhtml(newurl):
    resp = str(requests.get(newurl, headers=headers).text)
    resp = re.sub('.*text":"', '', resp, flags=re.S)
    resp = re.sub('"pic".*$', '', resp, flags=re.S)
    resp = resp.split('<p>')
    resp1 = []
    # print(remove_tags(resp))
    for i in range(len(resp)):
        if i != 0 and i != len(resp) - 1:
            resp1.append(remove_tags(resp[i]))

    return resp1


def bjh(elem):
    return elem[0]


def clhot(list_hot, key, count_hot, hot):
    list_hot.append(key)
    hotkey = key['hot'][0] + key['hot'][1] + key['hot'][2]
    hot = hot + hotkey
    count_hot.append([hotkey, len(count_hot)])
    return list_hot, count_hot, hot


def titlefl(compname):
    keytitleaboutcw = []
    hotcw = 0
    count1 = []
    keytitleaboutcw_gs = []
    hotcw_gs = 0
    count2 = []
    keytitleaboutpl = []
    hotpl = 0
    count3 = []
    keytitleaboutpl_gs = []
    hotpl_gs = 0
    hot = []
    count4 = []
    listofjudge = [r"季度", r"利润", r"净利", r"同比", r"季报", "营收"]
    for key in data_list:
        title = key['title']
        flag = 0
        for mc in listofjudge:
            if re.search(mc, title) != None:
                flag = 1
        if flag == 0 and re.search(compname, key['user_name']) == None:
            keytitleaboutpl, count3, hotpl = clhot(keytitleaboutpl, key, count3, hotpl)
        elif flag == 0 and re.search(compname, key['user_name']) != None:
            keytitleaboutpl_gs, count4, hotpl_gs = clhot(keytitleaboutpl_gs, key, count4, hotpl_gs)
        elif flag == 1 and re.search(compname, key['user_name']) == None:
            keytitleaboutcw, count1, hotcw = clhot(keytitleaboutcw, key, count1, hotcw)
        else:
            keytitleaboutcw_gs, count2, hotcw_gs = clhot(keytitleaboutcw_gs, key, count2, hotcw_gs)
    count1.sort(key=bjh)
    count2.sort(key=bjh)
    count3.sort(key=bjh)
    count4.sort(key=bjh)

    return [keytitleaboutcw, keytitleaboutcw_gs, keytitleaboutpl, keytitleaboutpl_gs], [count1, count2, count3,
                                                                                        count4], [hotcw, hotcw_gs,
                                                                                                  hotpl, hotpl_gs]


'''
newurl = 'https://xueqiu.com' + str(key['target'])
txt = readhtml(newurl)
words = jieba.lcut(txt,cut_all = False)
counts = {}

for word in words:
    if len(word) == 1 or word =="视觉" or word == "中国":
        continue
    else:
        counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse = True)

for i in range(15):
    word ,count = items[i]
    print("{0:<5}{1:>5}".format(word,count))

# ac = client.lexer(txt)
ac = client.lexerCustom(txt)
for key in ac['items']:
    print(key['item'], key['pos'], key['ne'])

break
'''


def clindata(compname):
    newdatalist = []
    for key in data_list:
        title = key['title']
        if re.search(compname, title) != None:
            newdatalist.append(key)

    return newdatalist


'''
for i in range(40):
    a = get_index(i)
    time.sleep(0.1)
    b = start_spider(a)
'''


def getrange(start_time, end_time,url):
    flag = 0
    timeflag = 0
    page = 1
    lastlength = 0
    while flag == 0:
        urlx = url + str(page)
        a = get_index(urlx)
        b = start_spider(a)
        if len(data_list) - lastlength == 0:
            flag = 1

            break
        if start_time >= end_time:
            if data_list[-1]['created_at'] < start_time and timeflag == 0:
                timeflag = 1
            if data_list[-1]['created_at'] > start_time and timeflag == 1:
                timeflag = 2
            if data_list[-1]['created_at'] < end_time and timeflag == 2:
                flag = 1
                break
        else:
            if data_list[-1]['created_at'] < end_time and timeflag == 0:
                timeflag = 1
            if data_list[-1]['created_at'] > start_time and timeflag == 1:
                flag = 1
                break
        page = page + 1
        # print(page)
        lastlength = len(data_list)
    return page


# 时间统计
def jltry(listx):
    counts = {}
    for dic in listx:
        counts[dic['created_at']] = counts.get(dic['created_at'], 0) + 1
    # print(counts)
    return counts


def fxtext(txt):
    maintxt = []
    stops = ["分析师", "研究所", "证书编号", "电话", "邮箱"]
    flag = 0
    for paragraph in txt:
        #print(paragraph)
        try:
            a = client.newsSummary(paragraph, 50)['summary']
            if len(a) > 10:
                #print(a)
                if re.search("风险提示", a) != None:
                    data_fx.append(a)
                    flag = 2
                for stop in stops:
                    if re.search(stop, a) != None:
                        flag = 1
                        break
                if flag == 1:
                    break
                a = re.sub("[。].*$", "", a)
                # print(a)
                if flag != 1:
                    maintxt.append(a)
                if flag == 2:
                    flag = 1
            time.sleep(0.2)
        except:
            pass

    return maintxt


def cptj(txt):
    ac = client.lexerCustom(txt)
    counts = {}
    cp = []
    for key in ac['items']:
        if len(key['item']) != 1 and (key['pos'] in ['n', 'nt', 'v', 'nz', 'a', 'an', 'vn'] and key['ne'] != 'ORG'):
            word = key['item']
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)

    for i in range(3):
        word, count = items[i]
        cp.append("{0:<5}{1:>5}".format(word, count))


def fxtitle(title, compname):
    # print(title)
    yds = ["骗", "操作", "离奇", "暴雷", "爆雷", "造假", "处罚", "谜团", "戏码"]
    flag = 0
    for yd in yds:
        if re.search(yd, title) != None:
            flag = 1

    strin = compname + "[.]*[：|！]"
    if re.search(strin, title) != None and re.search('公告', title) == None:
        titleshort = re.sub(".*[：|！]", "", title)
        # print(0)
        if len(titleshort) > 4:
            data_ms.append(titleshort)
    return flag


def qgfx(txt):
    qg = client.sentimentClassify(txt)

    if qg['items'][0]['sentiment'] == 2:
        if qg['items'][0]['confidence'] > 0.7:
            degree = 6
        else:
            degree = 5
    elif qg['items'][0]['sentiment'] == 1:
        if qg['items'][0]['positive_prob'] - qg['items'][0]['negative_prob'] > 0.06:
            degree = 4
        elif -0.06 < qg['items'][0]['positive_prob'] - qg['items'][0]['negative_prob'] < 0.06:
            degree = 3
        else:
            degree = 2
    else:
        if qg['items'][0]['confidence'] > 0.7:
            degree = 0
        else:
            degree = 1
    return degree

def readk(resp):
    #print(resp)
    resp = resp.split('<p>')
    resp1 = []
    # print(remove_tags(resp))
    for i in range(len(resp)):
        if i != 0 and i != len(resp) - 1:
            resp1.append(remove_tags(resp[i]))

    return resp1

def wordcloud(txt):

    f = open(txt, "rb").read()
    f = f.lower()
    wordcloud = WordCloud(background_color="white").generate(f)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

if __name__ == '__main__':

    import sys
    compname = sys.argv[1]  # 公司名称
    url = f'https://xueqiu.com/statuses/search.json?sort=relevance&source=all&q={compname}&count=10&page='
    cd = getrange(start_time=930, end_time=930,url = url)  # 返回帖子数 2019.9。30 和2018.9.30之间

    import os
    os.chdir(os.path.dirname(__file__))

    shuchu = {}

    data_list = clindata(compname)  # 排除无关新闻
    #print(data_list)
    keyfl, hotcount, hot = titlefl(compname)  # 返回【财务评价，财务新闻，事件评价，事件新闻】，【热度对应1，。。。】【热度值】
    shuchu["allcount"] = jltry(data_list)
    shuchu["count1"] = jltry(keyfl[0])
    shuchu['count2'] = jltry(keyfl[1])
    shuchu['count3'] = jltry(keyfl[2])
    shuchu['count4'] = jltry(keyfl[3])


    fxyj = []
    for i in range(1,len(hotcount[0])):
        shuchu["cwpj"] = fxtext(readk(keyfl[0][hotcount[0][len(hotcount[0])-i][1]]['text']))  # 对热度最高的一篇做分析，【时间较长
        if shuchu["cwpj"] != []:
            break
    for i in range(1,len(hotcount[2])):
        shuchu["sjpj"] = fxtext(readk(keyfl[2][hotcount[2][len(hotcount[2]) - i][1]]['text']))
        if shuchu["sjpj"] != []:
            break

    jltry(data_list)
    #cptj(data_list[0]['text'])  # 给出词频
    qg = []
    for news in data_list:
        try:
            qg.append(qgfx(news['title']))
            fl = fxtitle(news['title'], compname)
            if fl == 1:
                fxyj.append(fxtext(readk(news['text'])))
            time.sleep(0.05)
        except:
            pass
    shuchu["qg"] = qg  #对每篇的情感风险 0为十分悲观，1为悲观，2为中性偏悲观，3为中性，4为中性偏乐观，5为乐观，6为十分乐观
    msforcloud = []
    for ma in data_ms:
        a = ma.split("，")
        for key in a:
            msforcloud.append(key)
    shuchu["fxyj"] = fxyj #对财务风险观点的分析提取
    shuchu["jkpj"] = msforcloud #对近期的大事财务的部分评价
    file = open('data.txt', 'w', encoding ='utf-8')
    for i in msforcloud:
        file.write(i+"  ")
    file.close()
    # wordcloud('data.txt')  #用以做文字云
    shuchu["redu"] = cd + hot[0] + hot[1] + hot[2] + hot[3] #热度

    print(json.dumps(shuchu, ensure_ascii=False))
