import tkinter
base = tkinter.Tk()
base.wm_title("Lable Test")
lb = tkinter.Label(base,text = "Python Lable")
lb.pack()
#给相应组件指定布局
base.mainloop()