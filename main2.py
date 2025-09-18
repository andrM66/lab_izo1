from hist import make_hist
from task2 import task2
from task2_plot import make_task2_elem_plot
from PIL import Image
import numpy as np


IMG1 = "01_apc.tif"


if __name__ == '__main__':
    image = Image.open(IMG1)
    img_arr = np.array(image)
    img_new = task2(img_arr, "task2.png")
    make_hist(img_arr, img_new)
    make_task2_elem_plot(img_arr)
