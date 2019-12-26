from pip._vendor.distlib.compat import raw_input

code = raw_input("请输入序号:")#性能更优
print(code)

code2=input("请输入序号")#实际过程中都可以使用
print(code2)