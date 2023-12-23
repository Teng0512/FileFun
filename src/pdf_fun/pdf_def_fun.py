"""
-*- coding utf-8 -*-
@Time    : 2023/12/23 10:31
@Author  : mila Administrator
@File    : pdf_def_fun.py
@Software: PyCharm
"""
import PyPDF2,os,natsort,glob
"""
natsort.natsorted()
由于文件名是字符串，会按照字符的ASCII值进行排序（1 10 11……18 19 2 20 21……），会导致数字顺序不正确。
natsorted() 函数会根据数字的大小进行正确的排序，将文件名中的数字视为整体进行比较，而不是单个字符的ASCII值。
import os,glob
os.chdir(r'F:\Download\code_edit\FileFun\src\pdf_fun\pdf_file\data')
print(glob.glob('*.pdf'))
————————————————————————————————————————————————

['1.pdf', '10.pdf', '15.pdf', '20.pdf', '30.pdf', '40.pdf', '45.pdf', '5.pdf']

import os,glob
os.chdir(r'F:\Download\code_edit\FileFun\src\pdf_fun\pdf_file\data')
print(natsort.natsorted(glob.glob('*.pdf')))
————————————————————————————————————————————————

['1.pdf', '5.pdf', '10.pdf', '15.pdf', '20.pdf', '30.pdf', '40.pdf', '45.pdf']
参考地址：https://www.bilibili.com/read/cv24043851/
"""

def read_page(path, page):
    reader = PyPDF2.PdfReader(path)
    number_of_pages = len(reader.pages)
    try:
        print(f"该文件共有{number_of_pages}页")
        read_page_content = reader.pages[page]
        print(f"第{page}页内容如下：")
        text = read_page_content.extract_text()
        print(text)
    except IndexError:
        print(f"该文件共有{number_of_pages}页，您输入{page}页不存在，超出了文档范围")


def read_pdf_all(path):
    # 读取pdf文件所有内容
    reader = PyPDF2.PdfReader(path)
    number_of_pages = len(reader.pages)
    for i in range(number_of_pages):
        print(f"第{i+1}页内容如下：")
        read_page_content = reader.pages[i]
        text = read_page_content.extract_text()
        print(text)


def write_pdf_new(old_path, new_path, not_read_pages:list):
    # 将源文件拆分为两个文件
    pdfFile = open(old_path, 'rb')
    # 创建读取器对象
    pdfReader = PyPDF2.PdfReader(pdfFile)
    # 获取源文件页数
    all_pages = len(pdfReader.pages)
    # 创建写入器对象
    pdfWriter1 = PyPDF2.PdfWriter()
    pdfWriter2 = PyPDF2.PdfWriter()
    for page in range(all_pages):
        # 去除不想要的页面
        if page in not_read_pages:
            continue
        # 获取中间页码值
        middle_num = all_pages // 2
        # 提取一页数据
        pageObj = pdfReader.pages[page]
        if page <= middle_num:
            pdfWriter1.add_page(pageObj)
        else:
            pdfWriter2.add_page(pageObj)
    f1 = open(new_path+"/new_pdf1.pdf", 'wb')
    f2 = open(new_path+"/new_pdf2.pdf", 'wb')
    pdfWriter1.write(f1)
    pdfWriter2.write(f2)

    pdfFile.close()
    f1.close()
    f2.close()

def PDF_split(pdf_path,output_file,page_split_list):
    '''
    :param pdf_path: 需要拆分的PDF文件路径
    :param output_file: 拆分后的PDF文件的输出路径文件夹
    :param page_split_list: 需要拆分的页码的列表
    :return:
    '''
    #打开PDF文件
    pdf_reader=PyPDF2.PdfReader(pdf_path)
    #将最后一页加入到页码列表，用于拆分
    page_split_list.append(len(pdf_reader.pages))
    #遍历页码列表，拆分
    end_page=0
    for page_split in page_split_list:
        start_page=end_page
        end_page=page_split
        #创建PdfWriter
        pdf_writer=PyPDF2.PdfWriter()
        #遍历起止页之间的页码
        for page_num in range(start_page,end_page):
            page=pdf_reader.pages[page_num]
            #add_page()将页面添加到PdfWriter
            pdf_writer.add_page(page)
        #输出（保存）PdfWriter到指定文件夹，拆分后的文件命名为 原文件名 + 下划线 + 拆分页码
        pdf_writer.write(f'{output_file}\\{os.path.splitext(pdf_path)[0]}_{end_page}.pdf')


#合并PDF
def PDF_join(files_path, output_path):
    '''
    :param files_path: 需要合并的PDF文件所在的路径（文件夹）
    :param output_path: 输出路径
    :return:
    '''
    #获取路径中的PDF文件路径，并进行自然排序
    pdf_files=natsort.natsorted(glob.glob(f'{files_path}\\*.pdf'))
    #创建PdfWriter
    pdf_writer = PyPDF2.PdfWriter()
    #遍历文件
    for pdf_file in pdf_files:
        #读取每个PDF文件
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        #将页面添加到PdfWriter
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    #输出
    pdf_writer.write(output_path)

def pdf_rotate(file_path, new_file_path, page=1):
    # 翻转某一页,默认第一页
    minutesFile = open(file_path, 'rb')
    pdfReader = PyPDF2.PdfReader(minutesFile)
    page = pdfReader.pages[page-1]
    page.rotate(90)

    # 创建写入器，将翻转的第一张页面添加到写入器中
    pdfWriter = PyPDF2.PdfWriter()
    pdfWriter.add_page(page)

    resultPdfFile = open(new_file_path, 'wb')
    pdfWriter.write(resultPdfFile)
    resultPdfFile.close()
    minutesFile.close()

def pdf_merge_page(old_file, picture_file, new_file):
    #  给pdf每一页添加水印
    # 打开需要添加水印的pdf
    pythonFile = open(old_file, 'rb')
    # 对需要添加水印的pdf生成器读取器
    pdfReader = PyPDF2.PdfReader(pythonFile)
    # 生成水印pdf的读取器
    pdfWatermarkReader = PyPDF2.PdfReader(open(picture_file, 'rb'))
    pdfWriter = PyPDF2.PdfWriter()
    # 遍历需要添加水印pdf的每一页
    for pageNum in range(0, len(pdfReader.pages)):
        # 获取页面对象
        pageObj = pdfReader.pages[pageNum]
        # 添加水印（叠加两张页面）
        pageObj.merge_page(pdfWatermarkReader.pages[0])
        # 添加到写入器中（注意：写入器中已经添加了水印）
        pdfWriter.add_page(pageObj)
    resultPdfFile = open(new_file, 'wb')
    pdfWriter.write(resultPdfFile)
    pythonFile.close()
    resultPdfFile.close()

def pdf_password(file_path, new_file_path, password):
    # 给pdf文件设置密码
    pdfFile = open(file_path, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    pdfWriter = PyPDF2.PdfWriter()
    for pageNum in range(len(pdfReader.pages)):
        pdfWriter.add_page(pdfReader.pages[pageNum])
    pdfWriter.encrypt(password)
    resultPdf = open(new_file_path, 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()


if __name__ == '__main__':
    # pdf_path = r'\pdf_file\02_dockerfile实践.pdf'
    # read_page(path=pdf_path, page=20)
    # read_pdf_all(path=pdf_path)
    new_path = 'data'

    # write_pdf_new(old_path=pdf_path, new_path=new_path, not_read_pages=[])
    # os.chdir(r'F:\Download\code_edit\FileFun\src\pdf_fun\pdf_file')
    # pdf_path = '02_dockerfile实践.pdf'
    # PDF_split(pdf_path, new_path, [2,4,6,8,10])
    # os.chdir(r'F:\Download\code_edit\FileFun\src\pdf_fun\pdf_file')
    # pdf_path = 'data'
    # PDF_join(pdf_path, "docker资料合并.pdf")
    # 翻转某页
    # file_path = r".\pdf_file\02_dockerfile实践.pdf"
    # new_file_path = r"./data/rote/new_rote.pdf"
    # # pdf_rotate(file_path=file_path, new_file_path= new_file_path)
    # pdf_rotate(file_path=file_path, new_file_path=new_file_path, page=19)
    # 添加水印
    old_file = r".\pdf_file\02_dockerfile实践.pdf"
    picture_file = r".\data\merge\a.pdf"
    new_file = r".\data\merge\b.pdf"
    # pdf_merge_page(old_file=old_file,picture_file=picture_file,new_file=new_file)
    # 给文件添加密码
    pdf_password(old_file, new_file, "abcd")