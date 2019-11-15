import os
import time
import tkinter
from multiprocessing import Process, Queue


working = False
queue = Queue()


def start_(q):
    pid = os.getpid()
    q.put(pid)
    while 1:
        print("- - - start - - -")
        time.sleep(1)


def stop_(q):
    global working
    # 判断队列是否为空
    if not q.empty():
        pid = q.get(True)
        cmd = "taskkill /pid %d /f" % pid
        os.system(cmd)
        working = False


def work():
    global working
    if not working:
        p1 = Process(target=start_, args=(queue,))
        p1.start()
        working = True


def main():
    win = tkinter.Tk()
    win.title("auto")

    # 设置程序运行时的位置
    win.geometry("150x30+1000+200")

    start = tkinter.Button(win, text="开 始", command=work)
    start.place(x=30, y=0)

    stop = tkinter.Button(win, text="暂 停", command=lambda: stop_(queue))
    stop.place(x=80, y=0)

    win.mainloop()


if __name__ == '__main__':
    main()
