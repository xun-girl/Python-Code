car = [1,2,3,4,5,6,7,8,9,10]
#在列表的末尾补充一个元素
car.append(100)
print(car)
#在列表中的开头插入一个元素
car.insert(0,1000)
print(car)
#在列表中定向删除一个元素
del car[0]
print(car)
#弹出列表中特定的元素
num  = car.pop(1)
print(car)
print(num)
#删除列表中的特定值元素
car.remove(5)#remove只删除第一个特定的值
print(car)