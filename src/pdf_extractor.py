import io
import sys
import pdfminer3.settings
pdfminer3.settings.STRICT = False
import pdfminer3.high_level
import pdfminer3.layout
from pdfminer3.image import ImageWriter

def extract_pdfs(files):
    laparams = pdfminer3.layout.LAParams()
    for param in ("all_texts", "detect_vertical", "word_margin", "char_margin", "line_margin", "boxes_flow"):
        paramv = locals().get(param, None)
        if paramv is not None:
            setattr(laparams, param, paramv)

    extracted = []
    for fname in files:
        outfp = io.StringIO()
        with open(fname, "rb") as fp:
            pdfminer3.high_level.extract_text_to_fp(fp, outfp, laparams=laparams)

        extracted.append((fname, outfp.getvalue()))
        outfp.close()

    return extracted
