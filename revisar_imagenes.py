from PIL import Image, ImageDraw, ImageFont
import sys
import os
import random

lista_carpetas = os.listdir('./Carpetas a revisar')

path = 'C:/Users/Al_la/OneDrive/Escritorio/revision/Carpetas a revisar'

if not os.path.exists('Carpetas REVISADAS'):
    os.makedirs('Carpetas REVISADAS')

path_revisadas = './Carpetas REVISADAS'

for carpeta in lista_carpetas:
    lista_img = os.listdir(path + '/' + carpeta)
    path_imagen = path + '/' + carpeta

    if not os.path.exists(f'Carpetas REVISADAS/{carpeta}_Revisada'):
        os.makedirs(f'./Carpetas REVISADAS/{carpeta}_Revisada')

    for imagen in lista_img:
        im = Image.open(f'{path_imagen}/{imagen}')

        clean_name = os.path.splitext(imagen)[0]

        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("arial.ttf", 65)
        texto = draw.textsize('Revisado', font=font)

        x = random.randint(50, im.size[0]-texto[0])
        y = random.randint(100, im.size[1]-texto[1])
        draw.text((x, y), 'Revisado', fill=128, font=font)

        draw.line([x, y - 20, x + 80, y - 100, x, y - 20, x -
                   30, y - 50], fill=128, width=10, joint='curve')

        im.save(
            f'{path_revisadas}/{carpeta}_Revisada/{clean_name}_Revisada.jpeg', 'jpeg')

print('COMPLETADO')
