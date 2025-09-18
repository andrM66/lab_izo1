import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


MAX = 255
MIN = 0


def task2(img: np.ndarray, save_file: str = "no_image") -> np.ndarray:
    copy = img.copy()
    max = copy.max()
    min = copy.min()
    a = (MAX - MIN) / (max - min)
    b = (MAX * max - MAX * min)/(max - min)
    copy = copy * a + b
    copy = copy.astype(np.uint8)
    img_bin = Image.fromarray(copy)
    if save_file is not None and (save_file.endswith(".jpg") or save_file.endswith(".png")):
        img_bin.save(save_file)
    return copy
