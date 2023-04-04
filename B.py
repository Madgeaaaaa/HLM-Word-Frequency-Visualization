import jieba
import re
import zhconv
import collections
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

def Getlist():#传进要查询的副词列表
    a=[]
    while True:
        x=input("请输入想查询频率的字或词:")
        if x!="exit":
            a.append(x)
        else:
            return a

def show(counts,words):
    for i in words:
        print(i+str(counts[i]))

def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese

def Gettext():
    with open('dreamofredmaison.txt', encoding='utf-8') as f:
        text = f.read()
    #进行数据清洗，将繁体字转化为简体字，去除所有的非中文字符。
    text=find_chinese(text)
    text=zhconv.convert(text,'zh-hans')
    return text

def Break(text):
    fir=text.find("第八十一回")
    text1=text[:fir]
    text2=text[fir:]
    return text1,text2

def Getcount(text):
    result=jieba.lcut(text)#lcut返回列表
    counts=collections.Counter(result)
    return counts

def Getwordcloud(counts):
    ## 设置词云样式
    wc = WordCloud(
        background_color='white',  # 设置背景颜色
        font_path='msyh.ttc',
        width=200,
        height=100
    )
    wc.generate_from_frequencies(counts)  # 通过频率生成词云
    plt.imshow(wc)  # 显示词云图
    plt.axis('off')  # 是否显示x轴、y轴下标
    plt.show()

def GetHistogram(text,words):
    counts=Getcount(text)
    #words=Getlist()
    counts1=[counts[i] for i in words]
    fig = plt.figure()
    plt.bar(words,counts1, 0.4, color="steelblue")
    for a, b in zip(words, counts1):  # 柱子上的数字显示
        plt.text(a, b, '%d' % b, ha='center', va='bottom', fontsize=7);
    plt.ylabel("频率")
    plt.xlabel("词语")
    plt.show()

def question1():
    # 第一题
    words = Getlist()
    text = Gettext()
    counts = Getcount(text)
    show(counts, words)
    counts1 = Getcount(text1)
    counts2 = Getcount(text2)
def question2(text):
    text1, text2 = Break(text)
    xu = Getxuci()
    shi = Getshici()
    counts1 = Getcount(text1)
    counts2 = Getcount(text2)
    f1 = open(r'F:\Python\Python计算综合实验3\xu80.txt', 'w', encoding='utf-8')
    for word in xu:
        f1.write(word + str(counts1[word]) + '\n')
    f1.close()
    f2 = open(r'F:\Python\Python计算综合实验3\xu40.txt', 'w', encoding='utf-8')
    for word in xu:
        f2.write(word + str(counts2[word]) + '\n')
    f2.close()
    f3 = open(r'F:\Python\Python计算综合实验3\shi80.txt', 'w', encoding='utf-8')
    for word in shi:
        f3.write(word + str(counts1[word]) + '\n')
    f3.close()
    f3 = open(r'F:\Python\Python计算综合实验3\shi40.txt', 'w', encoding='utf-8')
    for word in shi:
        f3.write(word + str(counts2[word]) + '\n')
    f3.close()
def Getxuci():
    xu=["而","何","乎","乃","其","且","若","所","为","焉","也","以","因","与","于","则","者","之","了","的"]
    return xu
def Getshici():
    shi=["爱","安","伯","被","本","鄙","兵","病","察","长","朝","池","曾","乘","诚","笑","望","患","顾","怜","望","宜"]
    return shi

def question3(text):
    text1, text2 = Break(text)
    xu = Getxuci()
    shi = Getshici()
    counts1 = Getcount(text1)
    counts2 = Getcount(text2)
    GetHistogram(text1,xu)
    GetHistogram(text1,shi)
    GetHistogram(text2, xu)
    GetHistogram(text2, shi)
    wordscounts=dict([(key,counts1[key]) for key in xu])
    Getwordcloud(wordscounts)
    wordscounts = dict([(key, counts1[key]) for key in shi])
    Getwordcloud(wordscounts)
    wordscounts = dict([(key, counts2[key]) for key in xu])
    Getwordcloud(wordscounts)
    wordscounts = dict([(key, counts2[key]) for key in shi])
    Getwordcloud(wordscounts)

if __name__=='__main__':
    # text=Gettext()
    # question2(text)
    # text=Gettext()
    # counts=Getcount(text)
    # Getwordcloud(counts)
    text = Gettext()
    question3(text)




