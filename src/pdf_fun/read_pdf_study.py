"""
-*- coding utf-8 -*-
@Time    : 2023/12/23 9:51
@Author  : mila Administrator
@File    : read_pdf_study.py
@Software: PyCharm
"""
from pathlib import Path
from typing import Union, Literal, List
from pypdf import PdfWriter, PdfReader, Transformation


#from PyPDF2 import PdfWriter, PdfReader

def stamp(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(stamp_pdf)
    image_page = reader.pages[0]

    writer = PdfWriter()

    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox
        content_page.merge_page(image_page)
        content_page.mediabox = mediabox
        writer.add_page(content_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)


def watermark(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader(stamp_pdf)
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)

def stamp_pypdf(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    stamp_page = PdfReader(stamp_pdf).pages[0]

    writer = PdfWriter()
    # page_indices can be a List(array) of page, tuples are for range definition
    writer.append(content_pdf, pages=None if page_indices == "ALL" else page_indices)

    for content_page in writer.pages:
        content_page.merge_transformed_page(
            stamp_page,
            Transformation().scale(0.5),
        )

    writer.write(pdf_result)
def write_pypdf(old_file, picture_file, new_file):
    stamp = PdfReader(picture_file).pages[0]
    writer = PdfWriter(clone_from=old_file)
    for page in writer.pages:
        page.merge_page(stamp, over=False)  # here set to False for watermarking

    writer.write(new_file)

if __name__ == '__main__':
    old_file = r".\pdf_file\02_dockerfile实践.pdf"
    picture_file = r".\data\merge\a.pdf"
    new_file = r".\data\merge\b.pdf"
    write_pypdf(old_file, picture_file, new_file)