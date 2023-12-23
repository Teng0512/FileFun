"""
-*- coding utf-8 -*-
@Time    : 2023/12/23 9:51
@Author  : mila Administrator
@File    : read_pdf_study.py
@Software: PyCharm
"""
import PyPDF2
minutesFile = open('./data/new_pdf1.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(minutesFile)
page = pdfReader.pages[0]
page.rotate(90)

#创建写入器，将翻转的第一张页面添加到写入器中
pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(page)

resultPdfFile = open('./data/rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()