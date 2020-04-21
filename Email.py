#!/usr/bin/python3.7

import smtplib  # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText  # email 用于构建邮件内容
from email.mime.multipart import MIMEMultipart  # 用于构建邮件附件
from email.header import Header  # 用于构建邮件头
from tkinter import *
import time
from tkinter import filedialog
from os.path import *
from email.header import make_header
from email.mime.application import MIMEApplication


def run1(sender, password, receivers, sname, rname, subject, content, filenames):
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header(sname, 'utf-8')  # 发送方
    message['To'] = Header(rname, 'utf-8')  # 收件人
    #    subject = 'Python SMTP 邮件测试'    #标题
    message['Subject'] = Header(subject, 'utf-8')

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    message.attach(MIMEText(content, 'plain', 'utf-8'))
    if filenames:
        for file in filenames:
            with open(file, 'rb') as f:
                attachfile = MIMEApplication(f.read())
                attachfile.add_header('Content-Disposition', 'attachment', filename=basename(file))
                message.attach(attachfile)

    try:
        smtpObj = smtplib.SMTP_SSL()  # 开启发信服务，这里使用的是加密传输
        smtpObj.connect('smtp.qq.com', 465)
        smtpObj.login(sender, password)  # 登录发信邮箱
        for i in range(1):
            smtpObj.sendmail(sender, receivers, message.as_string())  # 发送邮件
            time.sleep(1)
            txt1.insert(END, '邮件发送成功\n')
        # 关闭服务器
        smtpObj.quit()
    except smtplib.SMTPException:
        txt1.insert(END, 'Error: 无法发送邮件\n')


def file_name():
    global y
    y = filedialog.askopenfilenames()
    y = list(y)
    txt3.insert(END, y)
    return y


if __name__ == '__main__':
    root = Tk()
    root.title('发送邮件 By:Ybx')
    root.geometry('460x300')
    y = 0
    # 输入
    inp1 = Entry(root)
    inp2 = Entry(root)
    inp3 = Entry(root)
    inp1.place(relx=0.15, rely=0.05, relwidth=0.3, relheight=0.05)
    inp2.place(relx=0.15, rely=0.15, relwidth=0.3, relheight=0.05)
    inp3.place(relx=0.15, rely=0.25, relwidth=0.3, relheight=0.05)
    # 文字
    lb1 = Label(root, text='邮箱')
    lb1.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.1)
    lb2 = Label(root, text='STMP码')
    lb2.place(relx=0.05, rely=0.15, relwidth=0.1, relheight=0.1)
    lb3 = Label(root, text='发送到')
    lb3.place(relx=0.05, rely=0.25, relwidth=0.1, relheight=0.1)
    txt3 = Text(root)
    txt3.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.1)
    btn2 = Button(root, text='选择发送文件', command=lambda: file_name())
    btn2.place(relx=0.7, rely=0.25, relwidth=0.3, relheight=0.1)
    # 发送方 收件方 标题 内容
    lb4 = Label(root, text='From:')
    lb4.place(relx=0.05, rely=0.4, relwidth=0.1, relheight=0.1)
    inp4 = Entry(root)
    inp4.place(relx=0.15, rely=0.4, relwidth=0.15, relheight=0.05)
    lb5 = Label(root, text='To:')
    lb5.place(relx=0.3, rely=0.4, relwidth=0.1, relheight=0.1)
    inp5 = Entry(root)
    inp5.place(relx=0.4, rely=0.4, relwidth=0.15, relheight=0.05)

    lb6 = Label(root, text='Subject:')
    lb6.place(relx=0.6, rely=0.4, relwidth=0.1, relheight=0.1)
    inp6 = Entry(root)
    inp6.place(relx=0.75, rely=0.4, relwidth=0.2, relheight=0.05)

    txt2 = Text(root)
    txt2.place(rely=0.5, relheight=0.2)
    btn1 = Button(root, text='提交',
                  command=lambda: run1(inp1.get(), inp2.get(), [inp3.get()], inp4.get(), inp5.get(), inp6.get(),
                                       txt2.get('0.0', 'end'), y))
    btn1.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.1)
    txt1 = Text(root)
    txt1.place(rely=0.8, relheight=0.2)
    root.mainloop()