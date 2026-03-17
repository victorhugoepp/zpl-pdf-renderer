import re

def split_labels(zpl_text: str):
    """
    Divide o ZPL em múltiplas etiquetas.
    Cada etiqueta começa com ^XA e termina com ^XZ
    """
    return re.findall(r'\^XA.*?\^XZ', zpl_text, flags=re.S)
