import os
import sys
from barcode import ITF
from barcode.writer import ImageWriter
from tempfile import  TemporaryDirectory
tempdir = TemporaryDirectory()


path = os.path.dirname(__file__)
print(os.listdir(path))


