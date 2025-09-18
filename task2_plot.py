import numpy as np
import matplotlib.pyplot as plt


MAX = 255
MIN = 0


def make_task2_elem_plot(img: np.ndarray) -> None:
    copy = img.copy()
    max = copy.max()
    min = copy.min()
    a = (MAX - MIN) / (max - min)
    b = (MAX * max - MAX * min) / (max - min)

    x = np.linspace(-5, 260, 200)
    y = np.where(x < MIN, a * MIN + b, np.where(x > MAX, a * MAX + b, a * x + b))
    plt.plot(x, y)
    plt.title(f'y = {a}x + b')
    plt.show()