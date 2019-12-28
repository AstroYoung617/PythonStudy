import re

import bs4
import lxml
import pymysql

import requests
from lxml import etree


def pageDown(URL):#下载网页
    hearders={"user-agent":"Google Chrome"}#爬虫伪装成谷歌浏览器发出请求
    response = requests.get(URL,headers = hearders).text
    return response

#正则表达式

def parsePage(page):#解析网页
    str = 'src="(.*\.jpg)"'
    regex = re.compile(str)#获取正则表达式对象
    imgList = re.findall(regex,page)#获取图片地址列表
    print(len(imgList))
    n=0
    for item in imgList:
        with open("image/%s.jpg"%(n),mode="wb") as file:
            img=requests.get(item).content
            file.write(img)
            n+=1

#LXML

def parsePage2(page):
    selector = etree.HTML(page) #根据网页生成选择器
    imgList=selector.xpath("//div/div[1]/a/img/@src")#LXML表达式
    print(len(imgList))
    n=0
    for item in imgList:
        with open("image/%s.jpg"%(n),mode="wb") as file:
            img=requests.get(item).content
            file.write(img)
            n+=1



def pageParse3(page):
    # soup = bs4.BeautifulSoup(page,"html.parser")
    # titleList=soup.find_all("a",class_="title")
    soup = bs4.BeautifulSoup(page,"lxml")
    titleList = soup.select("a.title")
    print(len(titleList))
    return titleList


def saveTxt(titleList):
    with open("title.txt",mode="w",encoding="utf-8") as file:
        n=1
        for item in titleList:
            file.write("%d.%s"%(n,item.string)+"\n")
            n+=1

def saveTitle(titleList):  #存储数据库
    #1.获取连接
    #2.获取游标
    #3.执行SQL
    #4.关闭连接
    def connectDb():
        con = pymysql.connect("localhost", "root", "123456", "test")
        return con
    connectDb()

    def createTable():
        try:
            con = connectDb()
            cursor = con.cursor()
            cursor.execute("drop table if exists title")

            cursor.execute("create table title "
                           "(id int(4) not null primary key auto_increment,"
                           "titles varchar(30))")
        except:
            print("建表失败")
            raise
        finally:
            con.commit()

    createTable()

    def savaData():
        try:
            con = connectDb()
            cursor = con.cursor()
            for item in titleList:
                cursor.execute("insert into title (titles) values ('%s')" % (item.string))
                con.commit()
        except:
            raise
        finally:
            con.close()
    #
    savaData()



#html=pageDown("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&word=%E6%9C%88%E6%BB%A1%E8%BD%A9%E5%B0%BC%E8%AF%97")
#print(html)
# parsePage(html)
# parsePage2(html)
page=pageDown("https://www.51job.com/")
# print(page)
# pageParse3(page)
saveTitle(pageParse3(page))