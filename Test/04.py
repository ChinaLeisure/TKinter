import tkinter
def showLabel():
    global  baseFrame
    #在函数中定义了一个Lable
    #label的父组件是baseFrame
    lb = tkinter.Label(baseFrame, text = "显示Label")
    lb.pack()
baseFrame = tkinter.Tk()
baseFrame.wm_title("我是傻逼高磊")
btn = tkinter.Button(baseFrame, text = "Show Label",command = showLabel)
btn.pack()

baseFrame.mainloop()