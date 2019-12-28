

# 1.下载网页
# 2.解析网页
# 3.存储到excel文件
# 4.存储文本文件
import urllib.request

import bs4
import pymysql
import requests
from openpyxl import Workbook


def pageDown(URL):#下载网页
    headers={"user-agent":"Mozilla/5.0"}#爬虫伪装成谷歌浏览器发出请求
    # response = requests.get(URL,headers = hearders).text
    request=urllib.request.Request(URL,headers=headers) #模拟一次请求
    response=urllib.request.urlopen(request) #发出请求
    return response.read().decode("gbk")#编码网页字符串

def parsePage(page):#解析网页中的职位信息
    soup = bs4.BeautifulSoup(page,"html.parser")
    jobList = soup.select("#resultList .el")#解析网页中id=resultList 下面class = el 的节点
    print(len(jobList))
    jobs=[]
    for item in jobList[1:]:
        jobname=item.select(".t1")[0].get_text(strip=True)
        company=item.select(".t2")[0].get_text(strip=True)
        city=item.select(".t3")[0].get_text(strip=True)
        salary=item.select(".t4")[0].get_text(strip=True)
        ddd=item.select(".t5")[0].get_text(strip=True)
        row={
            "jobname":jobname,
            "company":company,
            "city":city,
            "salary":salary,
            "ddd":ddd
        }
        jobs.append(row)
    return jobs

def saveExcel(jobList):
    workbook = Workbook("测试")
    sheet=workbook.create_sheet("北京Java开发",0)
    sheet.append(["职位名","公司名","地点","薪水","发布时间"])
    for item in jobList:
        sheet.append([item['jobname'],item['company'],item['city'],item['salary'],item['ddd']])
    workbook.save("51job.xlsx")

def saveTxt(jobList):#存储文本文件
    with open("51job.txt",mode="w",encoding="UTF-8") as file:
        try:
            for item in jobList:
                file.write("%s,%s,%s,%s,%s\n"%(item['jobname'],item['company'],item['city'],item['salary'],item['ddd']))
        except:
            print("写入失败")
            raise

def saveTitle(jobList):  #存储数据库
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
            cursor.execute("drop table if exists job")

            cursor.execute("create table job "
                           "(num int(5) not null primary key auto_increment,jobname varchar(50) ,"
                           "company varchar(50),city varchar(50),salary varchar(50),ddd varchar(50))")
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
            for item in jobList:
                # cursor.execute("insert into job (jobname,company,city,salary,ddd) values ('%s','%s','%s','%s','%s')" % (item['jobname'],item['company'],item['city'],item['salary'],item['ddd']))
                cursor.execute("insert into job(jobname,company,city,salary,ddd) values('%s','%s','%s','%s','%s')" % (item['jobname'], item['company'], item['city'], item['salary'], item['ddd']))
                con.commit()
        except:
            raise
        finally:
            con.close()
    #
    savaData()

data=pageDown("https://search.51job.com/list/010000,000000,0000,00,9,99,java%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")
# print(data)
job = parsePage(data)
print(job)
# saveExcel(job)
saveTxt(job)
saveTitle(job)