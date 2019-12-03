from tkinter import *


class Caculator:
    def __init__(self, root):
        self.root = root
        self.result = 0
        inputEntry = Entry(root)
        inputEntry.pack(padx=10, pady=10, fill=X)
        caculateButton = Button(root, text="Caculate", width=10,
                                height=1, font=["Arial", 22], command=lambda: self.caculate(inputEntry.get(), resultVar))
        caculateButton.pack(padx=10, pady=10, fill=X)
        resultVar = IntVar()
        resultLabel = Label(root, textvariable=resultVar,
                            font=["Arial", 22])
        resultLabel.pack(padx=10, pady=10, fill=X)

    def caculate(self, input, result):
        try:
            result.set(eval(input))
        except SyntaxError:
            result.set("Invalid Input.")


def main():
    root = Tk()
    root.title("計算機")
    Caculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
