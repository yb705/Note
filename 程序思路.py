prompt="\nTell me something,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."#变量prompt是两句话合在一起
message=""
while message!='quit':
  message=input(prompt)
  if message!='quit'：
    print(message)#一个程序可以先定义所需要的各种变量，之后直接使用定义代指变量进行主体编程
