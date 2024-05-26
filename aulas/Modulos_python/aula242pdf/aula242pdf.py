# PyPDF2 para manipular arquivos PDF (Instalação)
# Ative seu ambiente virtual
# python -m pip install pypdf2
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# PyPDF2 para manipular arquivos PDF (PdfReader, PdfWriter, PdfMerger)
# pdf de exemplo "relatoriobbfocus.pdf"

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / "pdfs_originais"
PASTA_NOVA = PASTA_RAIZ / "arquivos_novos"
RELATORIO_BACEN = PASTA_ORIGINAIS / "20240510_MACRO_BRAZIL_IPCA.pdf"

PASTA_NOVA.mkdir(exist_ok=True)


# PdfReader
reader = PdfReader(RELATORIO_BACEN)
# print(len(reader.pages)) #nº de páginas
# for page in reader.pages: #códigos de cada página
#     print(page)
#     print()

page1 = reader.pages[0]
imagem1 = page1.images[0]
# print(page1.extract_text()) #extrai os textos da página 1
# print(page1.images)  # lista de todas as imagens da página 1
# print(len(page1.images))  # quant das imagens da página 1

# Criando a primeira imagem da página 1:
with open(PASTA_NOVA / imagem1.name, "wb") as fp:
    fp.write(imagem1.data)
# wb -> write bytes
# image1.name -> pega o nome da prórpia imagem
# imagem1.data -> pega a "data" da imagem


# PdfWriter

# Criando uma página de um pdf
# writer = PdfWriter()
# page1 = reader.pages[0]
# writer.add_page(page1)
# with open(PASTA_NOVA / "PAGE1_.pdf", "wb") as file:
#     writer.write(file)

# Criando três páginas seguidas de um pdf
# writer = PdfWriter()
# with open(PASTA_NOVA / "PAGE123.pdf", "wb") as file2:
#     for i in range(3):  # Isso vai adicionar as páginas 0, 1 e 2
#         writer.add_page(reader.pages[i])
#     writer.write(file2)

# Criando um pdf para cada página
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f"page{i}.pdf", "wb") as file3:
        writer.add_page(page)
        writer.write(file3)

# PdfMerger
# Criando um pdf a patir de outros
# files ordenado de trás pra frente
files = [
    PASTA_NOVA / "page4.pdf",
    PASTA_NOVA / "page3.pdf",
    PASTA_NOVA / "page2.pdf",
    PASTA_NOVA / "page1.pdf",
    PASTA_NOVA / "page0.pdf",
]

merger = PdfMerger()
for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / "MERGED.pdf")
merger.close()
