def eat():
    print("吃吃吃")

def drink():
    print("喝喝喝")

def intro():
    print("大家好我是ITCCC")

def good_morning():
    print("早安R")


input_action = input("要做什麼呢:")

actions = {
    "吃": eat,
    "喝": drink,
    "自我介紹": intro,
    "說早安": good_morning,
}

if input_action in actions:
    actions[input_action]()
else:
    print("這個我不會喔QQ")