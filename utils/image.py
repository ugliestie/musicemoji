from PIL import Image
from urllib.request import urlopen
import io

def load_and_process(uri):
    cover = Image.open(urlopen(uri))
    if cover.size != (100, 100):
        cover = cover.resize((100, 100))
    cover = cover.convert('RGBA')
    buf = io.BytesIO()
    cover.save(buf, format='PNG')
    return buf.getvalue()