from parser import split_labels

def main():

    with open("sample.zpl", "r", encoding="utf-8") as f:
        zpl = f.read()

    labels = split_labels(zpl)

    print("Total de etiquetas:", len(labels))

    for i, label in enumerate(labels):
        print(f"Etiqueta {i+1} tamanho:", len(label))


if __name__ == "__main__":
    main()
