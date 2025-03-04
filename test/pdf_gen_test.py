import sys
import os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..'))
from backend.pdf_gen import *
from backend.brcode_container import *
from backend.backend import Database
from backend.vars import Vars
db = Database(Vars.json_path)
container = BRCodeContainer()
container(db)
opts = {
    "text_x_pos":30,
    "text_y_pos":60,
}


pdfgen = PDFGenerator(container)
pdfgen.generate_pdf_file(**opts)
os.system("start output.pdf")