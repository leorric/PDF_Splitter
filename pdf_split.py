from PyPDF2 import PdfReader, PdfWriter

def split_pages(input_pdf_path, output_pdf_path):
    reader = PdfReader(input_pdf_path)
    writer_left = PdfWriter()
    writer_right = PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        # 假设页面是A4大小，宽度大约为595点
        left_page = page.cropBox.getLowerLeft() + (page.cropBox.getUpperRight()[0] /2, page.cropBox.getUpperRight()[1])
        right_page = (page.cropBox.getLowerLeft()[0] + page.cropBox.getUpperRight()[0] /2, page.cropBox.getLowerLeft()[1]) + page.cropBox.getUpperRight()

        # 创建新页面并设置裁剪框
        new_left_page = page.createBlankPage(width=left_page[2 ] -left_page[0], height=left_page[3] -left_page[1])
        new_left_page.mergeScaledTranslatedPage(page, scale=1, tx=-left_page[0], ty=-left_page[1])
        writer_left.add_page(new_left_page)

        new_right_page = page.createBlankPage(width=right_page[2 ] -right_page[0], height=right_page[3] -right_page[1])
        new_right_page.mergeScaledTranslatedPage(page, scale=1, tx=-right_page[0], ty=-right_page[1])
        writer_right.add_page(new_right_page)

    with open(output_pdf_path +"_left.pdf", "wb") as fp:
        writer_left.write(fp)
    with open(output_pdf_path +"_right.pdf", "wb") as fp:
        writer_right.write(fp)

# 调用函数
split_pages("your_input_file.pdf", "output_file")