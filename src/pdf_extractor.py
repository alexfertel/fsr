import io
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator, TextConverter


def extract_pdfs(files):
    extracted = []
    for f in files:
        resource_manager = PDFResourceManager()
        fake_file_handle = io.BytesIO()
        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)

        with open(f, 'rb') as fd:
            for page in PDFPage.get_pages(fd, caching=True, check_extractable=True):
                page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()
            # print(text)
            extracted.append((f, text))
        
        converter.close()
        fake_file_handle.close()
    
    return extracted




