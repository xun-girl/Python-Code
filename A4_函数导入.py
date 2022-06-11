#test1.py
#关于接受多个实参
def get_parameter(*topping):#将所有的内容收录在一个元组中
    for top in topping:
        print(f"hello {top}")
#-------------------------
import test1#导入文件模块
test1.get_parameter("zhang","wang","li","zhao")