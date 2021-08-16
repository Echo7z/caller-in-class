# Author:Echo7z,Azathoth
# Time:2021/8/16/  10:52
# Version:2.0.1

from tkinter import *
from tkinter import filedialog, messagebox
import random
import os


def openfile():# 把文件保存在库.txt中
    file = filedialog.askopenfilename(filetypes=[('文本文档',".txt")])
    with open(file) as f:
        contents = f.read()
        with open('库.txt','w') as ku:
            ku.write(contents)

def takeone ():
    with open('库.txt') as a:
        contents = a.read()
        classmembers = contents.split(',')
    classes = random.sample(classmembers, 2)
    person1 = classes[0]
    var1.set(person1)
    var2.set("")
    var3.set("")

def taketwo ():
    with open('库.txt') as a:
        contents = a.read()
        classmembers = contents.split(',')
    classes = random.sample(classmembers, 2)
    person1 = classes[0]
    person2 = classes[1]
    var1.set(person1)
    var2.set(person2)
    var3.set("")

def takethree ():
    with open('库.txt') as a:
        contents = a.read()
        classmembers = contents.split(',')
    classes = random.sample(classmembers, 3)
    person1 = classes[0]
    person2 = classes[1]
    person3 = classes[2]
    var1.set(person1)
    var2.set(person2)
    var3.set(person3)

def backtofirst ():
    var1.set("")
    var2.set("")
    var3.set("")

def alldelete ():
    #全部初始化
    try:
        os.remove('库.txt')
    except FileNotFoundError:
        pass


def author ():
    messagebox.showinfo("作者", "Authors : Echo7z , Azathoth")

    pass

root = Tk()
root.geometry('340x180')
root.title("点名器")


classmembers = []


var0 = StringVar()
var0.set("请选择人数")
try:
    with open('库.txt') as ku:
        contents = ku.read()
except FileNotFoundError:
    var0.set("请导入人名列表")

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

menubar = Menu(root)

addmenu = Menu(menubar,tearoff=0)

addmenu.add_command(label="初始化程序",command=alldelete)
addmenu.add_command(label="退出",command=root.quit)
addmenu.add_separator()
addmenu.add_command(label="关于作者",command=author)
menubar.add_cascade(label='菜单', menu=addmenu)
menubar.add_command(label="导入新的人名列表",command=openfile)

root.config(menu=menubar)


textLable0 = Label(root,textvariable=var0,font=('Arial', 20)).grid(row=0,column=1)

textLable1 = Label(root,textvariable=var1,font=('Arial', 19)).grid(row=2,column=0)

textLable2 = Label(root,textvariable=var2,font=('Arial', 19)).grid(row=2,column=1)

textLable3 = Label(root,textvariable=var3,font=('Arial', 19)).grid(row=2,column=2)


theButton1 = Button(root,text="1人",command=takeone,font=('Arial', 17),height=1).grid(row=4,column=0)

theButton2 = Button(root,text="2人",command=taketwo,font=('Arial', 17),height=1).grid(row=4,column=1)

theButton3 = Button(root,text="3人",command=takethree,font=('Arial', 17),height=1).grid(row=4,column=2)

theButton4 = Button(root,text="清零",command=backtofirst,font=('Arial', 17),height=1).grid(row=6,column=1)


mainloop()



