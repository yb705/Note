number1=[]
for number in range(1,10):
	number1.append(number)#生成列表的法一
print(number1)
number2=list(range(1,10))#生成列表的法二
print(number2)
number3=[number**2 for number in range(1,10)]#生成列表的法三，列表解析
print(number3)
