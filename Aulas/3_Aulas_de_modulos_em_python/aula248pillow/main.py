# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from pathlib import Path
from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / "original.JPG"
NEW_IMAGE = ROOT_FOLDER / "new.JPG"

pil_image = Image.open(ORIGINAL)
print(pil_image.size)  # Tamanho da foto (widthxheight) -> tupla
width, height = pil_image.size
exif = pil_image.info["exif"]  # exif(chave) da info(dict) da foto
# lembrando que essas info pesa

# Para ficar proporcional, se darmos um valor qualquer para a width,
# fazendo regra de 3 descobrimos height
# width     new_width
# height    ??
new_width = 640
new_height = round(height * new_width / width)  # round arredonda valor
new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,  # otimizar -> comprime a image
    quality=70,  # qualidade -> 70%
    # exif=exif,
)
