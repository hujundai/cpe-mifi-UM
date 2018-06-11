#!/usr/bin/python
#-*- encoding=UTF-8 -*-  
#-*- encoding=UTF-8 -*-  
__author__ = 'jinhui.lu'  
import sys,os
from Tkinter import *  
root = Tk() 
root.title('WEB UI Tasks')    #定义窗体标题  
root.geometry('600x400')     #定义窗体的大小，是400X200像素  
  
def hello():  
    print('hello')  
  
def about():
    w = Label(root,text="opppppppppppppppppppppppppp")
    w.pack(side=TOP)
    os.system("auto.sh")
  
menubar = Menu(root)  
  
#创建下拉菜单File，然后将其加入到顶级的菜单栏中  
filemenu = Menu(menubar,tearoff=0)  
filemenu.add_command(label="Open", command=hello)  
filemenu.add_command(label="Save", command=hello)  
filemenu.add_separator()  
filemenu.add_command(label="Exit", command=root.quit)  
menubar.add_cascade(label="File", menu=filemenu)  
  
#创建另一个下拉菜单Edit  
editmenu = Menu(menubar, tearoff=0)  
editmenu.add_command(label="Cut", command=hello)  
editmenu.add_command(label="Copy", command=hello)  
editmenu.add_command(label="Paste", command=hello)  
menubar.add_cascade(label="Edit",menu=editmenu)  
#创建下拉菜单Help  
helpmenu = Menu(menubar, tearoff=0)  
helpmenu.add_command(label="About", command=about)  
menubar.add_cascade(label="Help", menu=helpmenu)  
  
#显示菜单  
root.config(menu=menubar)  
  
mainloop() 