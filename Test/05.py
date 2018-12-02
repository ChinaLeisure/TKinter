import tkinter

baseFrame =  tkinter.Tk()
btn1 = tkinter.Button(baseFrame, text = 'A')
btn1.pack (side = tkinter.LEFT,expand = tkinter.YES, fill = tkinter.Y)

btn2 = tkinter.Button(baseFrame, text = 'B')
btn2.pack(side = tkinter.TOP,expand = tkinter.YES ,fill = tkinter.NONE,anchor = tkinter.NE)



baseFrame.mainloop()