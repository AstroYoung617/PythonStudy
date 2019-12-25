

def fileRead():#第一种方式
    file=open("test/test.txt",mode="r",encoding="utf-8")
    data= file.read()
    print(data)
    file.close()#关闭文件，清理掉
#fileRead()

def fileRead2():#第二种方式，不需要close会自动清理掉
    try:#异常处理，可读性更强一些
        with open("test/test.txt",mode="r",encoding="utf-8") as file:
            data = file.read()
            print(data)
    except:#捕获异常
        print("文件找不到")
    finally:#最终执行代码块，不管是否出现异常都会进行执行
        print("最终执行")
fileRead2()

def writeFile():#如果文件不存在，则会自动生成该文件，并将内容写入
    with open("test/test.txt",mode="w",encoding="utf-8") as file:
        file.write("你好，西华")

#writeFile()

def appendFile():#追加在文件的后面
    with open("test/test.txt",mode="a",encoding="utf-8") as file:
        file.write("你好，成都")

#appendFile()

#file.read() #按字节读取
#file.readline() #按行读取
#file.readlines() #按行读取返回数组