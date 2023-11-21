''' program which must load the image "animal.jpeg", cut a square part from it
and transpose it to produce the image below. It should display it, print the
new shape and the data of the image after the transpose.'''

#  opencv, by default it reads the image with 3 channels, and in the case it
# is grayscale it copies its layer three times.

from load_image import ft_load
from matplotlib import pyplot as plt
import numpy as np


def ft_transpose(array):
    """transpose a 2D array"""
    (height, weight) = array.shape[:2]
    # creer un tableau vide avec les meme dimensions et meme typeque l original
    transposed_array = np.empty_like(array)
    for h in range(height):
        for w in range(weight):
            transposed_array[w, h] = array[h, w]
    # reconfigurer la disposition des éléments du tableau pour refléter une
    # structure bidimensionnelle avec les dimensions spécifiées.
    transposed_array = transposed_array.reshape(weight, height)
    return transposed_array


def main():
    try:
        img = ft_load("slice_np.jpeg")
        slice_image = img[:, :, 1:2]
    except TypeError as error:
        print(TypeError.__name__, error)
    else:
        # supprimer le chan 3 (ghost a cause d openCV)
        print(slice_image)
        array = ft_transpose(np.array(slice_image))
        plt.imshow(array, cmap="gray")
        plt.show()
        print("New shape after Transpose: ", array.shape[:2])
        print(array)


if __name__ == "__main__":
    main()
