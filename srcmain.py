from parser import split_labels, decode_fh_text


def main():
    texto1 = "Endereco_3A Rua Santa Luzia 15_2C Escorrega"
    texto2 = "Jo_C3_A3o"
    texto3 = "Cidade de destino_3A Goi_C3_A2nia"

    print(decode_fh_text(texto1))
    print(decode_fh_text(texto2))
    print(decode_fh_text(texto3))

    with open("sample.zpl", "r", encoding="utf-8") as f:
        zpl = f.read()

    labels = split_labels(zpl)
    print("Total de etiquetas:", len(labels))


if __name__ == "__main__":
    main()
