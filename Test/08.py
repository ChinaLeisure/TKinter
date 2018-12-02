import tkinter
def reg():
    name = e1.get()
    pwd = e2.get()

    t1 = len(name)
    t2 = len(pwd)
    if name == '111' and name == '222':
        #需要理解下面代码
        lb3["text"] = "登录成功"
    else:
        lb3['text'] = "用户名或密码错误"
        #输入框删除掉用户输入的内容
        #注意delete的两个参数，表示从第几个删除到第几个
        e1.delete(0,t1)
        e2.delete(0,t2)

baseFrame = tkinter.Tk()
lb1 = tkinter.Label(baseFrame, text="用户名：")
lb1.grid(row=0, column=0, sticky=tkinter.W)

e1 = tkinter.Entry(baseFrame)
e1.grid(row=0, column=1, sticky=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="密码：")
lb2.grid(row=1, column=0, sticky=tkinter.W)

e2 = tkinter.Entry(baseFrame)
e2.grid(row=1, column=1, sticky=tkinter.E)
e2['show'] = '*'    #e2显示为*

btn = tkinter.Button(baseFrame, text = "登录",command=reg) #command 调用函数
btn.grid(row=2, column=1, sticky=tkinter.W)
lb3 = tkinter.Label(baseFrame)
lb3.grid(row=3, column=1, sticky=tkinter.W)

baseFrame.mainloop() 
