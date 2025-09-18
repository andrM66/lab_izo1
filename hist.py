import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import seaborn as sns


IMG1 = "01_apc.tif"


def make_hist(img1: np.ndarray, img2: np.ndarray):
    fg, axes = plt.subplots(1, 2, figsize=(15,10))
    hist1 = np.histogram(img1, bins=256, range=[0, 256])[0]
    hist2 = np.histogram(img2, bins=256, range=[0, 256])[0]

    axes[0].bar(range(256), hist1, color="blue", alpha=0.7, width=1)
    axes[1].bar(range(256), hist2, color="red", alpha=0.7, width=1)
    plt.show()


if __name__ == '__main__':
    image = Image.open(IMG1)
    img_arr = np.array(image)
    make_hist(img_arr)
    make_hist()
