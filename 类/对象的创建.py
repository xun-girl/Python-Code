class BOY:
    def __init__(self,name,color,age):#定义对象具有的属性
        self.name = name
        self.color = color
        self.age = age
    def eat(self,food):
        print(f"{self.name} eat {food}")# self的前缀跟的都是属性

cat1 = BOY("zhang","red",18)#创建一个对象这里和java中的类似
#以上是实例化一个对象
cat1.eat("meat")#利用这个对象（类的实例）调用类中的方法

