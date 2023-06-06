"""
Copyright (c) 2020 ITCT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# 删除文件夹下面的所有文件(只删除文件,不删除文件夹)
import os
import shutil
import stat
import threading
import time
import socket
import tkinter as tk
from tkinter import ttk, END
from time import sleep
from tkinter import messagebox
from tkinter.filedialog import askdirectory



# Temp-临时文件
path_data1 = "C:\\Windows\\Temp"
# Prefetch-访问记录
path_data2 = "C:\\Windows\\Prefetch"
# Download-系统更新时下载的补丁和一些安装包等
path_data3 = "C:\\Windows\\SoftwareDistribution\\Download"
# LogFiles-系统日志及操作记录
path_data4 = "C:\\Windows\\System32\\LogFiles"
path_data_diy = ""


# python删除文件的方法 os.remove(path)path指的是文件的绝对路径,如：
# os.remove(r"E:\code\practice\data\1.py")#删除文件
# os.rmdir(r"E:\code\practice\data\2")#删除文件夹（只能删除空文件夹）
# shutil.rmtree(r"E:\code\practice\data\2")#删除文件夹
# path_data = "E:\code\practice\data"#


def thread_it(func, *args):
    """将函数打包进线程"""
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ITCT-windows tool V1.10") 
        self.root.configure(bg='#2c3038')
        self.root.option_add('*Font', '微软雅黑')
        # self.root.geometry("1500x200+1800+150")
        # 程序运行时在屏幕中间打开
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
         # 设置窗口大小
        ww = int(sw * 0.8)  # 将宽度设置为屏幕宽度的80%
        wh = int(sh * 0.6)  # 将高度设置为屏幕高度的60%
        x = (sw - ww) // 2
        y = (sh - wh) // 2
        self.root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        self.root.resizable(False, False)
        self.root.update()
        self.root.wm_attributes('-topmost', 1)
        self.interface()

    def interface(self):
        self.CheckVar1 = tk.IntVar()
        self.CheckVar2 = tk.IntVar()
        self.CheckVar3 = tk.IntVar()
        self.CheckVar4 = tk.IntVar()
        self.C1 = tk.Checkbutton(self.root, text="Temp-临时文件", variable=self.CheckVar1, onvalue=1, offvalue=0,
                                 fg='#d9f5ff', bg='#2c3038', selectcolor='#2c3344', activebackground='#2c3038',
                                 activeforeground='#60b6fc')
        self.C2 = tk.Checkbutton(self.root, text="Prefetch-访问记录", variable=self.CheckVar2, onvalue=1, offvalue=0,
                                 fg='#d9f5ff', bg='#2c3038', selectcolor='#2c3344', activebackground='#2c3038',
                                 activeforeground='#60b6fc')
        self.C3 = tk.Checkbutton(self.root, text="Download-系统更新补丁", variable=self.CheckVar3, onvalue=1, offvalue=0,
                                 fg='#d9f5ff', bg='#2c3038', selectcolor='#2c3344', activebackground='#2c3038',
                                 activeforeground='#60b6fc')
        self.C4 = tk.Checkbutton(self.root, text="LogFiles-系统日志", variable=self.CheckVar4, onvalue=1, offvalue=0,
                                 fg='#d9f5ff', bg='#2c3038', selectcolor='#2c3344', activebackground='#2c3038',
                                 activeforeground='#60b6fc')
        self.C1.select()
        self.C2.select()
        self.C3.select()
        self.C4.select()
        self.C1.grid(row=0, column=0, ipadx=10, ipady=10, padx=3, pady=10)
        self.C2.grid(row=0, column=1, ipadx=10, ipady=10, padx=3, pady=10)
        self.C3.grid(row=0, column=2, ipadx=10, ipady=10, padx=3, pady=10)
        self.C4.grid(row=0, column=3, ipadx=10, ipady=10, padx=3, pady=10)
        self.Button0 = tk.Button(self.root, text="清理基本C盘垃圾", command=lambda: thread_it(self.event_清理基本C盘垃圾), width=10,
                                 bg='#4a8e53', fg='#d9f5ff', activebackground='#4d535f', activeforeground='#fdfdfd')
        self.Button0.grid(row=0, column=4, ipadx=20, ipady=10, padx=5, pady=10)
        self.w1 = tk.Entry(self.root, textvariable='请输入目标路径', bg='#25272c', fg='#b2b2b2')
        self.w1.grid(row=1, column=0, columnspan=4, ipadx=290, ipady=8, padx=5, pady=10)
        self.Button1 = tk.Button(self.root, text="选择目标文件夹", command=lambda: thread_it(self.event_选择目标文件夹), width=10,
                                 bg='#4780ac', fg='#d9f5ff', activebackground='#4d535f', activeforeground='#fdfdfd')
        self.Button1.grid(row=1, column=4, ipadx=20, ipady=10, padx=5, pady=10)
        self.Button2 = tk.Button(self.root, text="清理目标文件夹", command=lambda: thread_it(self.event_清理目标文件夹), width=10,
                                 bg='#4a8e53', fg='#d9f5ff', activebackground='#4d535f', activeforeground='#fdfdfd')
        self.Button2.grid(row=1, column=5, ipadx=20, ipady=10, padx=5, pady=10)
        self.Button3 = tk.Button(self.root, text="清空输出信息", command=lambda: thread_it(self.event_清空输出信息), width=10,
                                 bg='#2c3038', fg='#d9f5ff', activebackground='#4d535f', activeforeground='#fdfdfd')
        self.Button3.grid(row=0, column=5, ipadx=20, ipady=10, padx=5, pady=10)
        self.text = tk.Text(self.root, bg='#25272c', fg='#777c8a')
        self.text.grid(row=2, column=0, columnspan=6, ipadx=195, padx=10, pady=10)
        # 新建滚动条
        self.scroll = tk.Scrollbar()
        # 两个控件关联
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)

    def event_清理基本C盘垃圾(self):
        try:
            if self.CheckVar1.get() == 1:
                self.routineCleanup1()
            if self.CheckVar2.get() == 1:
                self.routineCleanup2()
            if self.CheckVar3.get() == 1:
                self.routineCleanup3()
            if self.CheckVar4.get() == 1:
                self.routineCleanup4()
        except Exception as e:
            print(e)

    def event_选择目标文件夹(self):
        path_ = askdirectory()  # 使用askdirectory()方法返回文件夹的路径
        if path_ == "":
            self.w1.get()  # 当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
        else:
            path_ = path_.replace("/", "\\")  # 实际在代码中执行的路径为“\“ 所以替换一下
            print(path_)
            self.w1.delete(0, END)
            self.w1.insert(0, path_)

    def event_清理目标文件夹(self):
        try:
            data_path = self.w1.get()
            if data_path is not None:
                time1 = time.time()
                current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time1))
                self.text.insert(tk.INSERT, "正在清理目标文件" + data_path + current_time + '\n')
                self.text.see(END)
                self.del_file(data_path)
                time2 = time.time()
                self.text.insert(tk.INSERT, "清理用时" + str(round((time2 - time1), 2)) + 's' + '\n')
                self.text.see(END)
        except Exception as e:
            self.text.insert(tk.INSERT, "   " + str(e) + '\n')
            self.text.see(END)
            print(e)

    def event_清空输出信息(self):
        try:
            self.text.delete('1.0', END)
        except Exception as e:
            print(e)
            pass

    def del_file(self, path_data):
        if len(os.listdir(path_data)) == 0:
            self.text.insert(tk.INSERT, "  无垃圾可清理" + '\n')
            self.text.see(END)
            print("  无垃圾可清理")
            return
        n = 0
        for i in os.listdir(path_data):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
            # file_data = path_data + "\\" + i  # 当前文件夹的下面的所有东西的绝对路径
            path = os.path.join(path_data, i)
            if os.path.isdir(path):
                try:
                    # 使用shutil模块
                    shutil.rmtree(path)
                except Exception as error:
                    os.system('rd /s /q %s' % path)
                self.text.insert(tk.INSERT, '  已清除文件夹 ' + path + '\n')
                self.text.see(END)
                print('  已清除文件夹 ' + path)
            elif os.path.isfile(path):
                try:
                    # 使用os模块删除
                    os.remove(path)
                except Exception as error:
                    # 使用windows命令行强制删除
                    # os.system('del' + path + '/S')
                    os.system("del /f /q %s" % path)
                self.text.insert(tk.INSERT, '  已清除文件 ' + path + '\n')
                self.text.see(END)
                print('  已清除文件 ' + path)
            n += 1
        if n > 0:
            self.text.insert(tk.INSERT, '此路径共清除文件数： ' + str(n) + '\n')
            self.text.see(END)

    def routineCleanup1(self):
        try:
            time1 = time.time()
            current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time1))
            self.text.insert(tk.INSERT, "正在清理Temp-临时文件的垃圾……" + current_time + '\n')
            self.text.see(END)
            print("正在清理Temp-临时文件的垃圾……" + current_time)
            # 利用以下语言获得文件夹的写入权限
            os.chmod(path_data1, stat.S_IRWXU)
            self.del_file(path_data1)
            time2 = time.time()
            self.text.insert(tk.INSERT, "  清理用时" + str(round((time2 - time1), 2)) + 's' + '\n')
            self.text.see(END)
        except Exception as e:
            self.text.insert(tk.INSERT, "   " + str(e) + '\n')
            self.text.see(END)
            print("   " + str(e))

    def routineCleanup2(self):
        try:
            time1 = time.time()
            current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time1))
            self.text.insert(tk.INSERT, "正在清理Prefetch-访问记录的垃圾……" + current_time + '\n')
            self.text.see(END)
            print("正在清理Prefetch-访问记录的垃圾……" + current_time)
            os.chmod(path_data2, stat.S_IRWXU)
            self.del_file(path_data2)
            time2 = time.time()
            self.text.insert(tk.INSERT, "  清理用时" + str(round((time2 - time1), 2)) + 's' + '\n')
            self.text.see(END)
        except Exception as e:
            self.text.insert(tk.INSERT, "   " + str(e) + '\n')
            self.text.see(END)
            print("   " + str(e))

    def routineCleanup3(self):
        try:
            time1 = time.time()
            current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time1))
            self.text.insert(tk.INSERT, "正在清理Download-系统补丁的垃圾……" + current_time + '\n')
            self.text.see(END)
            print("正在清理Download-系统补丁的垃圾……" + current_time)
            # 利用以下语言获得文件夹的写入权限
            os.chmod(path_data3, stat.S_IRWXU)
            self.del_file(path_data3)
            time2 = time.time()
            self.text.insert(tk.INSERT, "  清理用时" + str(round((time2 - time1), 2)) + 's' + '\n')
            self.text.see(END)
        except Exception as e:
            self.text.insert(tk.INSERT, "   " + str(e) + '\n')
            self.text.see(END)
            print("   " + str(e))

    def routineCleanup4(self):
        try:
            time1 = time.time()
            current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time1))
            self.text.insert(tk.INSERT, "正在清理LogFiles-系统日志的垃圾……" + current_time + '\n')
            self.text.see(END)
            print("正在清理LogFiles-系统日志的垃圾……" + current_time)
            # 利用以下语言获得文件夹的写入权限
            os.chmod(path_data4, stat.S_IRWXU)
            self.del_file(path_data4)
            time2 = time.time()
            self.text.insert(tk.INSERT, "  清理用时" + str(round((time2 - time1), 2)) + 's' + '\n')
            self.text.see(END)
        except Exception as e:
            self.text.insert(tk.INSERT, "   " + str(e) + '\n')
            self.text.see(END)
            print("   " + str(e))


if __name__ == "__main__":
    a = GUI()
    a.root.mainloop()

#打包 pyinstaller -F -w -i ico.ico ITCT.py
# cd 进入主目录 project/python/clean
