import tkinter

def hit_me():
    var = e.get()
    # 可以把 insert 換成 end 試試看
    t.insert('insert', var)

root = tkinter.Tk()
root.title('109-NKUST Information Technology Club')
root.geometry('480x360')
e = tkinter.Entry(root)
e.pack()
b = tkinter.Button(root, text='點一下insert', width=15, height=2, command=hit_me)
b.pack()
t = tkinter.Text(root, height=5)
t.pack()
root.mainloop()
