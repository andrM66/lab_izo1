from PIL import Image
import numpy as np


IMG1 = "01_apc.tif"


def task1(img: np.ndarray, f: int, save_file: str="no_image") -> np.ndarray:
    copy = img.copy()
    copy //= f
    copy *= 255
    img_bin = Image.fromarray(copy)
    if save_file is not None and (save_file.endswith(".jpg") or save_file.endswith(".png")):
        img_bin.save(save_file)
    return copy


if __name__ == '__main__':
    image = Image.open(IMG1)
    img_arr = np.array(image)
    img_new = task1(img_arr, 120, "sf")
