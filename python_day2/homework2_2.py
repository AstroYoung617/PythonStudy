


def fileRead2():#第二种方式，不需要close会自动清理掉
    try:#异常处理，可读性更强一些
        with open("test/"+input("输入文件名："),mode="r",encoding="utf-8") as file:
            data = file.read()
            li=data.split("\n")
            def turn(b):
                a = 0
                for a in range(b,li.__len__()):
                    if a<10:
                        print(li[a])
                        a += 1
                    if a==10:
                        b+=a
                if input("是否继续阅读？（y/n）") == "y":
                    turn(b)
            turn(0)


    except:#捕获异常
        print("文件找不到")
    finally:#最终执行代码块，不管是否出现异常都会进行执行
        print("最终执行")
fileRead2()