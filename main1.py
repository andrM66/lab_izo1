from task1 import task1
from hist import make_hist
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


IMG1 = "01_apc.tif"


def plot_f(f: int):
    x = np.arange(256)
    y = np.where(x < f, 0, 255)
    plt.plot(x, y)
    plt.show()



if __name__ == '__main__':
    image = Image.open(IMG1)
    img_arr = np.array(image)
    img_new = task1(img_arr, 120, "task1.png")
    make_hist(img_arr, img_new)
    plot_f(120)