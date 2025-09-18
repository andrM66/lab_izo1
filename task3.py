import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from hist import make_hist


IMG1 = "01_apc.tif"


def equalize_image(img1: np.ndarray, save_file: str="None") -> np.ndarray:


    img = img1.copy()

    hist = np.histogram(img, bins=256, range=[0, 256])[0]
    cdf = np.cumsum(hist)


    cdf_normalized = ((cdf - cdf.min()) * 255 /
                      (cdf.max() - cdf.min())).astype(np.uint8)

    equalized_array = cdf_normalized[img]
    equalized_img = Image.fromarray(equalized_array)

    hist_eq = np.histogram(equalized_array, bins=256, range=[0, 256])[0]
    eq_cdf = np.cumsum(hist_eq)
    fig, axes = plt.subplots(2, 2, figsize=(15,10))
    axes[0, 0].bar(range(256), hist, color="blue", alpha=0.7, width=1)
    axes[0, 0].set_title("Исходник")

    axes[0, 1].plot(cdf, color="red")
    axes[0, 1].set_title("Исходник")

    axes[1, 0].bar(range(256), hist_eq, color="green", alpha=0.7, width=1)
    axes[1, 0].set_title("Эквализация")

    axes[1, 1].plot(eq_cdf, color="yellow")
    axes[1, 1].set_title("Эквализация")
    plt.show()


    if save_file is not None and (save_file.endswith(".jpg") or save_file.endswith(".png")):
        equalized_img.save(save_file)

    return equalized_array


def plot_func(img:np.ndarray):
    copy = img.copy()
    hist = np.histogram(copy, bins=256, range=[0, 256])[0]
    cdf = np.cumsum(hist)


    cdf_normalized = ((cdf - cdf.min()) * 255 /
                      (cdf.max() - cdf.min())).astype(np.uint8)


    plt.plot(np.arange(256), cdf_normalized, label="Функция преобразования")
    plt.show()



if __name__ == '__main__':
    image = Image.open(IMG1)
    img_arr = np.array(image)
    eq = equalize_image(img_arr, "task3.png")
    eq_standard = ImageOps.equalize(image)
    eq_standard.save("test2.png")
    eq_standard_array = np.array(eq_standard)
    make_hist(eq_standard_array, eq)
    plot_func(img_arr)