from tkinter import *

class Main:
    def __init__(self, root):
        self.root = root

    def main(self):
        # 新增元件及排版可以寫在這裡
        pass

def main():
    root = Tk()

    # 視窗寬度
    width = 256

    # 視窗高度
    height = 256

    # 視窗標題
    title = "標題"

    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry("{}x{}+{}+{}".format(width, height,
                                       (screenWidth - width) // 2, (screenHeight - height) // 2))
    root.title(title)
    Main(root).main()
    root.mainloop()

if __name__ == "__main__":
    main()
