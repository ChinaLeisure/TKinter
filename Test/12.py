import tkinter
baseFrame = tkinter.Tk()

cvs = tkinter.Canvas(baseFrame, width=330, height=200)
cvs.pack()

#一条线需要两个点指明起始
#参数数字的单位是PX
cvs.create_line(23,23,190,234)
cvs.create_text(156,67, text = 'I love python')

baseFrame.mainloop()
