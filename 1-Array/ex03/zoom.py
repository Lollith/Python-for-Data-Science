'''program that should load the image "animal.jpeg", print some information
about it and display it after "zooming"'''
# import os
from load_image import ft_load
from matplotlib import pyplot as plt


def main():
    img = ft_load("animal.jpeg")
    print(img)
    slice_image = img[100: 500, 450:850, 1:2]
    plt.imshow(slice_image, cmap="gray")
    print("New shape after slicing: ", end="")
    print(f"{slice_image.shape} or {slice_image.shape[:2]}")
    print(slice_image)
    plt.show()


if __name__ == "__main__":
    main()
