import time
import PIL
from PIL import Image, ImageOps

import os


def path_cheker(dir):
    paths = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            print(os.path.join(root, file))
            paths.append(os.path.join(root, file))
    return paths

def crop_image(name_of_file: str, path: str):
    im = Image.open(name_of_file)
    width, height = im.width, im.height
    pixels = im.load()
    all_pixels_tuple = []
    # start_time = time.time()
    for i in range(width):
        string_of_pixel = []
        all_pixels_tuple.append(string_of_pixel)
        for j in range(height):
            string_of_pixel.append(pixels[i, j])
    height, width = height - 1, width - 1
    # Верхний край
    tops = []
    for x in range(width // 2 - 10, width // 2 + 10):
        for y in range(height // 2):
            if sum(all_pixels_tuple[x][y]) > 600:
                tops.append(y)
                break
    top = min(tops)
    # Нижний край
    bottoms = []
    for x in range(width // 2 - 10, width // 2 + 10):
        for y in range(height, height // 2, -1):
            if sum(all_pixels_tuple[x][y]) > 600:
                bottoms.append(y)
                break
    bottom = max(bottoms)
    # Левый край
    lefts = []
    for y in range(height // 2 - 10, height // 2 + 10):
        BLACK_MEETED = False
        for x in range(width // 8):
            if sum(all_pixels_tuple[x][y]) > 600:
                if BLACK_MEETED:
                    lefts.append(x)
                    break
            else:
                BLACK_MEETED = True
    left = max(lefts)
    # Правый край
    rights = []
    for y in range(height // 2 - 10, height // 2 + 10):
        BLACK_MEETED = False
        for x in range(width, width - width // 8, -1):
            if sum(all_pixels_tuple[x][y]) > 600:
                if BLACK_MEETED:
                    rights.append(x)
                    break
            else:
                BLACK_MEETED = True
    right = min(rights)
    # Обрезаем
    im1 = im.crop((left, top, right, bottom))
    final_path = path + '/' + name_of_file
    for i in range(1, len(final_path.split('/'))):
        if not os.path.isdir("/".join(final_path.split('/')[:i])):
            print(final_path)
            os.mkdir("/".join(final_path.split('/')[:i]))
    im1.save(final_path)



if __name__ == "__main__":
    root = str(input("Папка с файлами путь :"))
    # size = tuple([int(elem) for elem in str(input("Размеры, к которому необходимо привести изображения через запятую :")).split(',')])
    save_root = str(input("Папка, в которую надо сохранить папку с изображениями :"))
    sp_of_files = path_cheker(root)
    for elem in sp_of_files:
        crop_image(elem, save_root)
