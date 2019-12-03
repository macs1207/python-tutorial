import tkinter
root = tkinter.Tk()

#視窗名稱
root.title('109-NKUST Information Technology Club')

#視窗大小
root.geometry('480x360')

# text:要顯示的文字
# bg:背景顏色
# font:自型設定
# width, height:寬, 高
lable = tkinter.Label(root, text='12/17有活動', bg='white',
                 font=('Arial', 12), width=30, height=2)

lable.place(relx=0.5, rely=0.5, anchor='center')
root.mainloop()
