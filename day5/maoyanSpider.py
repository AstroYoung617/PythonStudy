# 1.下载网页
# 2.解析网页
# 3.存储文本文件
# 4.存储数据库
import json
import time
import urllib.request

import pymysql


def pageDown(URL):
    header = {"user-agent":"Mozilla"}
    request = urllib.request.Request(URL,headers = header)
    response = urllib.request.urlopen(request)
    return response.read().decode("utf-8")

def pageParse(page):
    comments = json.loads(page)["cmts"]
    print(len(comments))
    return comments

def saveTxt(comments):
    with open("maoyan.csv",mode="a+",encoding="utf-8") as file:
        for item in comments:
            file.write("%s:%s:%s:%s:%s\n" % (item['content'],str(item['id']),item['nickName'],str(item['userId']),str(item['userLevel'])))

def saveTitle(comments):  #存储数据库
    #1.获取连接
    #2.获取游标
    #3.执行SQL
    #4.关闭连接
    def connectDb():
        con = pymysql.connect("localhost", "root", "123456", "test")
        return con
    connectDb()

    def savaData():
        try:
            con = connectDb()
            cursor = con.cursor()
            for item in comments:
                # cursor.execute("insert into job (jobname,company,city,salary,ddd) values ('%s','%s','%s','%s','%s')" % (item['jobname'],item['company'],item['city'],item['salary'],item['ddd']))
                cursor.execute("insert into movie(content,id,nickName,userId,userLevel) values('%s','%s','%s','%s','%s')"
                               % (item['content'], item['id'], str(item['nickName']), item['userId'], item['userLevel']))
                con.commit()
        except:
            raise
        finally:
            con.close()
    #
    savaData()


if __name__ =="__main__":
    for i in range(0,20):
        page=pageDown("http://m.maoyan.com/mmdb/replies/comment/1094068807.json?_v_=yes&offset="+str(i*10))
        time.sleep(1)
        comments = pageParse(page)
        saveTxt(comments)
        # saveTitle(comments)

        # print(page)



# page=pageDown("http://m.maoyan.com/mmdb/replies/comment/1094068807.json?_v_=yes&offset=10")
# print(page)