from dataclasses import dataclass
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
from collections import defaultdict
import os
import sys
from numpy import full
import win32file
import win32con
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time

l1 = [
    ('三公司', '3@qq.com'),
    ('二公司', '2@qq.com'),
    ('一公司', '1@qq.com'),
    ('件', '1@qq.com'),
]

l2 = '件'

from collections import defaultdict
d3 = defaultdict(str)
s2 = set(l2)
for t in l1:
    if t[0] in s2:
        d3 = t[1]
        d3=[t[1]]
        print(d3)
 
#l3 = list(d3.items())
#print(l3)
print(type(d3))


ACTIONS = {
  1: "Created",
  2: "Deleted",
  3: "Updated",
  4: "Renamed from something",
  5: "Renamed to something"
}

FILE_LIST_DIRECTORY = 0x0001

path_to_watch = 'C:/Users/98/Desktop/监控文件项目'
#print("Watching changes in", path_to_watch)
hDir = win32file.CreateFile(
  path_to_watch,
  FILE_LIST_DIRECTORY,
  win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
  None,
  win32con.OPEN_EXISTING,
  win32con.FILE_FLAG_BACKUP_SEMANTICS,
  None
)
while 1:

    results = win32file.ReadDirectoryChangesW(
        hDir,
        1024,
        True,
        win32con.FILE_NOTIFY_CHANGE_FILE_NAME,
        #win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
        #win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
        #win32con.FILE_NOTIFY_CHANGE_SIZE |
        #win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
        #win32con.FILE_NOTIFY_CHANGE_SECURITY,
        None,
        None)
    for action, filename in results:
        #full_filename = os.path.join(path_to_watch, filename)
        full_filename = os.path.join(filename)#邮件发送当前文件下的文件名
        #print(full_filename)
        #os.unlink(full_filename)
        #full_filename = eval(repr(full_filename).replace('\\', '/'))
        #full_filename = eval(repr(full_filename).replace('//', '/'))
        #os.remove(full_filename) 
        #print(full_filename, ACTIONS.get(action, "Unknown"))
        fromaddr = 'xxx@163.com'
        password = 'xxx'
        #content = 'hello, this is email content.'
        content = str(full_filename)
        textApart = MIMEText(content)
        pdfFile = str(full_filename)#接入监控参数  full_filename !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        time.sleep(10)
        pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        m = MIMEMultipart()
        m.attach(textApart)
        m.attach(pdfApart)
        m['Subject'] = 'title'
        server = smtplib.SMTP('smtp.163.com')
        server.login(fromaddr,password)
        toaddrs = d3
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
        print(full_filename)
