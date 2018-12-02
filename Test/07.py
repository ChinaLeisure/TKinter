import tkinter
def baseLabel(event):
    global baseFrame
    print("哈哈哈 抓到我了")
    lb = tkinter.Label(baseFrame, text="狗币 点我")
baseFrame  = tkinter.Tk()

lb = tkinter.Label(baseFrame,text="模拟按钮")
#label 绑定相应的消息和处理函数
#自动获取左键点击，并启动相应的处理函数baseLable
lb.bind("<Button-1>", baseLabel)
lb.pack()
baseFrame.mainloop()