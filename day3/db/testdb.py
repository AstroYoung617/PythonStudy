

import  pymysql

def connectDb():
    con = pymysql.connect("localhost","root","123456","test")
    return con
connectDb()
#检查连接是否成功

# con = connectDb()
# if con!= None:
#    print("成功")
# else:
#    print("失败")

#创建表

def createTable():
    try:
        con = connectDb()
        cursor = con.cursor()
        cursor.execute("drop table if exists user")
        cursor.execute("create table user "
                        "(id int(4) not null primary key auto_increment,"
                         "username varchar(12),password varchar(8))")
    except:
        print("建表失败")
        raise
    finally:
        con.commit()

# createTable()

#添加
def savaData():
    try:
        con = connectDb()
        cursor = con.cursor()
        cursor.execute("insert into user (username,password) values ('%s','%s')"%("jack","123456"))
        con.commit()
    except:
        raise
    finally:
        con.close()
#
# savaData()

#删除数据

def deleteData():
    try:
        con = connectDb()
        cursor = con.cursor()
        cursor.execute("delete from user where id='%d'"%(1))
        con.commit()
    except:
        raise
    finally:
        con.close()
# deleteData()


#修改数据

def UpdateData():
    try:
        con = connectDb()
        cursor = con.cursor()
        cursor.execute("update user set username = '%s',"
                       "password = '%s' where id = '%d'" % ('张三','1111111',2))
        con.commit()
    except:
        raise
    finally:
        con.close()

UpdateData()

#查询数据

def selectData():
    try:
        con = connectDb()
        cursor = con.cursor()
        cursor.execute("select * from user")
        resultSet = cursor.fetchall()#结果集
        #遍历结果结果集
        for item in resultSet:
            print(item)
    except:
        raise
    finally:
        con.close()
selectData()