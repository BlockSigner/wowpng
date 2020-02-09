import ctypes
import sys

from PIL import Image

import pdfium as PDFIUM
#import PDFIUMv8 as PDFIUM


PDFIUM.FPDF_InitLibraryWithConfig(PDFIUM.FPDF_LIBRARY_CONFIG(2, None, None, 0))

scale = 2
flags = 0x01 | 0x02

doc = PDFIUM.FPDF_LoadDocument(sys.argv[1], None)

form_config = PDFIUM.FPDF_FORMFILLINFO(1)
form_config.xfa_disabled = 1

form_fill = PDFIUM.FPDFDOC_InitFormFillEnvironment(doc, form_config)

n_pages = PDFIUM.FPDF_GetPageCount(doc)
image_fname = "page-%%0%ii.png" % len(str(n_pages))

for i in range(n_pages):
    page = PDFIUM.FPDF_LoadPage(doc, i)

    # XXX Not needed to render form content?
    #PDFIUM.FORM_OnAfterLoadPage(page, form_fill)

    # XXX extract chacters on the page as unicode, useful for full text search?
    if False:
        text = PDFIUM.FPDFText_LoadPage(page)
        text_ = ''.join(chr(PDFIUM.FPDFText_GetUnicode(text, c))
                        for c in range(PDFIUM.FPDFText_CountChars(text)))

    width = int(PDFIUM.FPDF_GetPageWidthF(page)) * scale
    height = int(PDFIUM.FPDF_GetPageHeightF(page)) * scale

    bitmap = PDFIUM.FPDFBitmap_Create(width, height, 1)

    PDFIUM.FPDFBitmap_FillRect(bitmap, 0, 0, width, height, 0xFFFFFFFF)

    PDFIUM.FPDF_RenderPageBitmap(bitmap, page, 0, 0, width, height, 0, flags)
    PDFIUM.FPDF_FFLDraw(form_fill, bitmap, page, 0, 0, width, height, 0, flags)

    buffer = PDFIUM.FPDFBitmap_GetBuffer(bitmap)
    buffer_ = ctypes.cast(buffer, ctypes.POINTER(ctypes.c_ubyte * (width * height * 4)))

    img = Image.frombuffer("RGBA", (width, height), buffer_.contents, "raw", "BGRA", 0, 1)

    img.save(image_fname % i)

    PDFIUM.FPDFBitmap_Destroy(bitmap)
    PDFIUM.FPDF_ClosePage(page)
