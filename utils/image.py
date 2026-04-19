from PIL import Image
from urllib.request import urlopen
import io

def load_and_process(uri):
    cover = Image.open(urlopen(uri))
    if cover.size != (100, 100):
        cover = cover.resize((100, 100))
    cover = cover.convert('RGBA')
    bufer = io.BytesIO()
    cover.save(bufer, format='PNG')
    return bufer.getvalue()

def process_buf(buf):
    cover = Image.open(buf)
    if cover.size != (100, 100):
        cover = cover.resize((100, 100))
    cover = cover.convert('RGBA')
    bufer = io.BytesIO()
    cover.save(bufer, format='PNG')
    return bufer.getvalue()