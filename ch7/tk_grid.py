from tkinter import *

class Main:
    def __init__(self, root):
        self.root = root

    def main(self):
        buttons = []

        # Button 0
        button = Button(self.root, text=0, width=30, height=5)
        buttons.append(button)

        # Button 1~9
        for i in range(1, 10):
            button = Button(self.root, text=str(i), width=10, height=5)
            buttons.append(button)
            
        for row in range(3):
            for column in range(3):
                index = row * 3 + column + 1
                buttons[index].grid(row=row, column=column)
        buttons[0].grid(row=3, column=0, columnspan=3)

def main():
    root = Tk()

    # 視窗標題
    title = "標題"

    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.title(title)
    Main(root).main()
    root.mainloop()

if __name__ == "__main__":
    main()
