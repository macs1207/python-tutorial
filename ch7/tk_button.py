import tkinter

on_hit = False


def hit_me():
    global on_hit
    if on_hit:
        on_hit = False
        var.set('12/17有活動')
    else:
        on_hit = True
        var.set('12/26也有')


# 初始化
root = tkinter.Tk()
root.title('109-NKUST Information Technology Club')
root.geometry('480x360')

# 用來存 label 的文字
var = tkinter.StringVar()
var.set('12/17有活動')
# textvariable 參數用來指定 StringVar 物件
lable = tkinter.Label(root, textvariable=var, bg='white',
                      font=('Arial', 12), width=30, height=2)
lable.place(relx=0.5, rely=0.5, anchor='center')
b = tkinter.Button(root, text='點一下', width=15,
                   height=2, command=hit_me).pack()

root.mainloop()
