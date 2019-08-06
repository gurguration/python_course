# from abc import ABC, abstractmethod


# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError('File Stream already opened')
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError('File Stream already closed')
#         self.opened = False


# class FileStream(Stream):
#     def read(self):
#         print("reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("reading data from network")


# class MemoryStream(Stream):
#     def read(self):
#         print("Reading data from a memory stream.")


# mem = MemoryStream()
# net = NetworkStream()
# fil = FileStream()

# net.read()
# fil.read()
# mem.read()


# class UIControl(ABC):
#     def draw(self):
#         print("TextBox")


# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")


# def draw(controls):
#     for control in controls:
#         control.draw()


# textbox = UIControl()
# ddl = DropDownList()
# draw([ddl, textbox])


# print(isinstance(ddl, UIControl))

# class Text(str):
#     def duplicate(self):
#         return self + self


# text = Text("Python")
# print(text.duplicate())


# class TrackableList(list):
#     def append(self, object):
#         print("append called ")
#         super().append(object)


# xlist = TrackableList()
# xlist.append('x')
# print(xlist)


# from collections import namedtuple

# Point = namedtuple("Point", ["x", "y"])
# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)
# print(p1.x, p2.y)
# from time import ctime
# import sys
# from pathlib import Path

# path = Path(r"C:\Users\g\Desktop\python_course")

# print(path.is_file())

# print(path.exists())
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# print(path.absolute())

# for p in path.iterdir():
#     print(p)

# print(ctime(path.stat().st_ctime))

# from zipfile import ZipFile
# zip = ZipFile('./Files.zip', 'w')


# for p in Path('c:/Users/g/Desktop/python_course').rglob("*.*"):
#     zip.write(p)
# zip.close()


# with ZipFile(r'c:/Users/g/Desktop/python_course/Files.zip') as zip:
#     print(zip.namelist())
# info = zip.getinfo('Files')
# print(info.file_size)
# print(info.compress_size)
# import csv

# with open("datacsv.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1001, 2, 15])


# with open('datacsv.csv', 'r') as file:
#     reader = csv.reader(file)
#     print(list(reader))

# import json
# from pathlib import Path

# movies = [
#     {"id": 1, "title": "terminator", "year": 1989},
#     {"id": 1, "title": "terminator", "year": 1989}
# ]
# data = json.dumps(movies)

# Path("movies.json").write_text(data)

# from json import loads
# from pathlib import Path

# data = Path('movies.json').read_text()
# movies = loads(data)
# print(movies)

# import sqlite3
# import json
# from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())
# print(movies)
# with sqlite3.connect('db.sqlite3') as conn:
#     command = "INSERT INTO Movies VALUES(?,?,?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#         break
#     conn.commit()


# with sqlite3.connect('db.sqlite3') as conn:
#     command = 'SELECT * FROM Movies'
#     cursor = conn.execute(command)
#     for row in cursor:
#         print(row)
#     conn.commit()


# import time
# print(time.time())
# def send_emails():
#     for i in range(100000000):
#         pass
# start = time.time()
# send_emails()
# end = time.time()
# print('Duration: ', start - end)

# import webbrowser
# from random import randint, choice, choices, random, shuffle
# from datetime import datetime, timedelta
# import time
# import string

# dt = datetime(2018, 1, 1)
# dt = datetime.now()
# dt2 = datetime.strptime("2018/01/01", "%Y/%m/%d")
# print(dt.month)

# diff = (dt-dt2)
# print("days", diff)
# print("seconds", diff.total_seconds())
# dt = datetime.fromtimestamp(time.time())
# print(dt.day)
# print(f'{dt.year, dt.hour}')


# print(choices((1, 2, 3, 4, 5, 6), k=2))
# print(random())

# # generate random passsowrd
# dictionary = 'abcdevfghighlkmopqrstuvxyz123456789'


# def generate_password(klen=6):
#     return ''.join(choices(dictionary, k=klen))


# def generate_password2(klen=6):
#     return ''.join(choices(string.ascii_letters + string.digits, k=klen))


# def random_shuffle():
#     shuffled = list([string.digits+string.ascii_letters][0])

#     shuffle(shuffled)
#     return ''.join(shuffled)


# print(generate_password())

# print(generate_password2())

# print(random_shuffle())

# webbrowser.open('google.com')


# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib

# message = MIMEMultipart()
# message['from'] = "Gentoer"
# message['to'] = 'testuser@gmail.com'
# message['subject'] = 'This is a test'
# message.attach(MIMEText('Body', 'plain'))

# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("testuser@codewithme.com", 'todayskyisblue1234')
#     smtp.send_message(message)
#     print('Sent...')


# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# from string import Template
# import smtplib

# template = Template(Path("template.html").read_text())
# message = MIMEMultipart()
# message['from'] = "Gentoer"
# message['to'] = 'testuser@gmail.com'
# message['subject'] = 'This is a test'
# body = template.substitute({'name': "John"})
# message.attach(MIMEText(body, 'html'))
# message.attach(Path("testimage.png").read_bytes())

# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("testuser@codewithme.com", 'todayskyisblue1234')
#     smtp.send_message(message)
#     print('Sent...')

# import sys

# print(sys.argv)

# if len(sys.argv) == 1:
#     print("USAGE: python3 classses.py <password>")
# else:
#     password = sys.argv[1]
#     print("Password: ", password)


# import requests
# import subprocess
# import platform

# if platform.system() in 'Windows':
#     result = subprocess.run(['explorer', 'C:'], capture_output=False)
#     print('args: ', result.args)
#     print('returncode: ', result.returncode)
#     print('stderr: ', result.stderr)
#     print('stdout: ', result.stdout)
#     print(type(result))
# elif platform.system() in 'Linux':
#     result = subprocess.run(['ls', '-l'], capture_output=True,
#                             text=True)
#     print('args: ', result.args)
#     print('returncode: ', result.returncode)
#     print('stderr: ', result.stderr)
#     print('stdout: ', result.stdout)
#     print(type(result))


# IF CHECK=TRUE THAN SUBPROCCESS.RUN WILL AUTOMATICALLY WILL RISE AN EXCEPTION!

# if platform.system() in 'Windows':
#     result = subprocess.run(
#         ['python',
#          '-u',
#          r'c:\Users\g\Desktop\python_course\other.py'],
#         text=True,
#         capture_output=True)
#     print('args: ', result.args)
#     print('returncode: ', result.returncode)
#     print('stderr: ', result.stderr)
#     print('stdout: ', result.stdout)
#     print(type(result))
# elif platform.system() in 'Linux':
#     result = subprocess.run(['ls', '-l'], capture_output=True,
#                             text=True)
#     print('args: ', result.args)
#     print('returncode: ', result.returncode)
#     print('stderr: ', result.stderr)
#     print('stdout: ', result.stdout)
#     print(type(result))


# if platform.system() in 'Windows':
#     try:
#         result = subprocess.run(
#             ['python',
#              '-u',
#              r'c:\Users\g\Desktop\python_course\other.py'],
#             text=True,
#             check=True,
#             capture_output=True)
#         print('args: ',         result.args)
#         print('returncode: ',   result.returncode)
#         print('stderr: ',       result.stderr)
#         print('stdout: ',       result.stdout)
#         print(type(result))
#     except subprocess.CalledProcessError as e:
#         print('Called proccess exited with error')
#         print(e)
# elif platform.system() in 'Linux':
#     try:
#         result = subprocess.run(['ls', '-l'], capture_output=True,
#                                 text=True,
#                                 check=True)
#         print('args: ',         result.args)
#         print('returncode: ',   result.returncode)
#         print('stderr: ',       result.stderr)
#         print('stdout: ',       result.stdout)
#         print(type(result))
#     except subprocess.CalledProcessError as e:
#         print('Called proccess exited with error')
#         print(e)


# import requests

# # print(response)

# url = 'https://api.yelp.com/v3/businesses/search'

# response = requests.get(url)

# print(response.text)
# from bs4 import BeautifulSoup
# import requests

# url = 'https://stackoverflow.com/questions'

# response = requests.get(url)
# soup = BeautifulSoup(response.text, features='html.parser')
# questions = soup.select('.question-summary')
# print(questions[0].get('id', 0))
# cls_selected = questions[0].select_one('.question-hyperlink')
# # print(cls_selected.getText())
# for question in questions:
#     print(question.select_one('.question-hyperlink').getText())
#     print(question.select_one('.vote-count-post').getText())


# import bs4
# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('https://github.com/login')
# signin_link = browser.find_element_by_id('login_field')


# username_box = browser.find_element_by_id("login_field")
# username_box.send_keys("gurguration")
# password_box = browser.find_element_by_id("password")
# password_box.send_keys("yourpassword")

# password_box.submit()
# profile_link = browser.find_element_by_class_name('user-profile-link')
# link_label = profile_link.get_attribute('innerHTML')
# assert 'gurguration' in link_label
# browser.quit()
# import PyPDF2

# with open('test.pdf', 'rb') as pdffile:
#     reader = PyPDF2.PdfFileReader(pdffile)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("rotated.pdf", "wb") as output:
#         writer.write(output)


# import PyPDF2

# merger = PyPDF2.PdfFileMerger()
# file_names = ["first.pdf", "second.pdf"]

# for file_name in file_names:
#     merger.append(file_name)
# merger.write('combined.pdf')
# import openpyxl

# # wb = openpyxl.Workbook()
# wb = openpyxl.load_workbook("configuration.xlsx")
# print(wb.sheetnames)
# sheet = wb["Sheet1"]
# # wb.create_chartsheet("Sheet2", 0)
# cell = sheet['a1']
# cell_value = cell.value
# print(cell_value)
# print(cell.coordinate)
# sheet.cell

# import openpyxl

# wb = openpyxl.load_workbook('configuration.xlsx')
# sheet = wb['Sheet1']
# sheet.cell(row=1, column=1)
# print(sheet.max_column)


# wb = openpyxl.load_workbook('configuration.xlsx')
# sheet = wb['Sheet1']
# sheet.cell(row=1, column=1)

# for row in range(1, sheet.max_row + 1):
#     print(sheet.cell(row, 1).value)

# sheeta = sheet['a']
# sheetac = sheet['a:c']
# print(sheeta)
# print(sheetac)
# sheet.append([1, 2, 3, 4])
# sheet.insert_rows(16, 3)
# wb.save('configurations2.xlsx')


# import numpy as np
# array = np.array([[1, 2, 3], [4, 5, 6]])
# print(array)
# print(type(array))
# print(array.shape)

# zeros = np.zeros((3, 3), dtype=int)
# print(zeros)
# print(zeros[0, 2])
# print(zeros == 0)
# print(zeros[zeros == 0])
# print(np.sum(zeros))
# print(np.floor(zeros))

# dimensions_inch = np.array([1, 2, 3])
# dimensions_cm = dimensions_inch * 2.54
# print(dimensions_cm)
