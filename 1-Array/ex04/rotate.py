''' program which must load the image "animal.jpeg", cut a square part from it
and transpose it to produce the image below. It should display it, print the
new shape and the data of the image after the transpose.'''

#  opencv, by default it reads the image with 3 channels, and in the case it 
# is grayscale it copies its layer three times.

from load_image import ft_load
from matplotlib import pyplot as plt
import numpy as np
# import cv2


def ft_transpose(array):
    (height, width) = array.shape[:2]
    for h in range(height):
        for w in range(width):
            if w > h:
                temp = array[h, w].copy()
                array[h, w] = array[w, h]
                array[w, h] = temp
    return array


def main():
    img = ft_load("slice_np.jpeg")
    # supprimer le chan 3 (ghost a cause d openCV)
    slice_image = img[:, :, 1:2]
    print(slice_image)
    # print("New shape after Transpose: ", simage.shape[:2])
    array = ft_transpose(np.array(slice_image))
    print("-----------------------")
    print(array)
    plt.imshow(array, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
