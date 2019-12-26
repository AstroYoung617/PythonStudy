#自定义异常类函数


class MyException(Exception):
    def __init__(self,str):
        self.str = str #初始化变量str

    def process(self):
        if len(self.str)>=5:
            print("长度大于等于5")
        else:
            print("长度不足")

if __name__ == "__main__":#主函数

    try:
        string = input("请输入字符串：")
        raise MyException(string)
    except MyException as e:
        e.process()