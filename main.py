import PyPDF2
import os


def mark():
    # provide pdf file names seperated by comma
    pdf_list = input('What PDFs you want to watermark?\n').split(sep=', ')
    # watermark must be in pdf format
    wm_pdf = input('What watermark you want to use\n')

    output_folder = 'output\\' # watermarked pdf will be in output folder
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    pdf_writer = PyPDF2.PdfFileWriter()  # Write object
    watermark = PyPDF2.PdfFileReader(open(wm_pdf, 'rb'))  # Watermark object

    for file in pdf_list:
        with open(f'{file}', 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)  # Read object
            for page_num in range(pdf_reader.getNumPages()):
                pdf_page = pdf_reader.getPage(page_num)  # reads page
                pdf_page.mergePage(watermark.getPage(0))  # applies watermark
                pdf_writer.addPage(pdf_page)  # saves watermarked page
            with open(output_folder + 'WATERMARKED_' + file, 'wb') as wmf:
                pdf_writer.write(wmf)  # saves watermarked pdf
    print('Watermarking ended with success!')


mark()
