

def fileRead2():#第二种方式，不需要close会自动清理掉
    try:#异常处理，可读性更强一些
        with open("test/test.txt",mode="r",encoding="utf-8") as file:
            data = file.read()
            li=data.split("\n")
            for item in li:
                item1=item.strip()
                if not item1.startswith("#"):
                    print(item1)
    except:#捕获异常
        print("文件找不到")
    finally:#最终执行代码块，不管是否出现异常都会进行执行
        print("最终执行")
fileRead2()