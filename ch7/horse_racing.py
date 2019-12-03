from tkinter import *
import random

# class init


def gui_init():
    root.title("Horse Racing")
    screeenWidth = root.winfo_screenwidth()
    screeenHeight = root.winfo_screenheight()
    w = 400
    h = 300
    root.geometry("{}x{}+{}+{}".format(w, h, (screeenWidth - w) //
                                       2, (screeenHeight - h) // 2))


def goalGenerate():
    goalLbl = []
    for i in range(8):
        goalLbl.append(Label(root, text="|", font=("Consolas", 16)))
        goalLbl[i].place(x=385, y=0 + i * 30)


def horseGenerate():
    horseLbl = []
    for i in range(8):
        horseLbl.append(
            Label(root, text="~/-\^", font=("Consolas", 16), relief="raised"))
        horseLbl[i].place(x=0, y=0 + i * 30)
    return horseLbl


def horseMove(horse):
    location = [0] * 8

    def move():
        idx = random.randrange(8)
        location[idx] += 10
        for i in range(8):
            horse[i].place(x=location[i], y=0 + i * 30)
        if(location[idx] < 330):
            root.after(10, move)
        else:
            endMsg = Label(root, text="Horse " + str(idx + 1) +
                           " wins!", font=("Consolas", 16))
            endMsg.place(y=260)
    move()


root = Tk()
gui_init()
goalGenerate()
horseLbl = horseGenerate()
horseMove(horseLbl)
root.mainloop()
