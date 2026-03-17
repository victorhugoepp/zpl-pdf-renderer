import re


def split_labels(zpl_text: str):
    """
    Divide o ZPL em múltiplas etiquetas.
    Cada etiqueta começa com ^XA e termina com ^XZ.
    """
    return re.findall(r"\^XA.*?\^XZ", zpl_text, flags=re.S)


def decode_fh_text(text: str, indicator: str = "_") -> str:
    """
    Decodifica sequências hexadecimais usadas com ^FH.
    Exemplo:
        'Endereco_3A Rua A_2C 10' -> 'Endereco: Rua A, 10'
        'Jo_C3_A3o' -> 'João'

    O padrão do indicador é '_' mas o ZPL pode mudar isso.
    """
    out = bytearray()
    i = 0

    while i < len(text):
        if text[i] == indicator and i + 2 < len(text):
            hexpair = text[i + 1:i + 3]

            if re.fullmatch(r"[0-9A-Fa-f]{2}", hexpair):
                out.append(int(hexpair, 16))
                i += 3
                continue

        out.extend(text[i].encode("utf-8", errors="ignore"))
        i += 1

    return out.decode("utf-8", errors="ignore")
