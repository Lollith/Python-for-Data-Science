'''program that should load the image "animal.jpeg", print some information
about it and display it after "zooming"'''

from load_image import ft_load
from matplotlib import pyplot as plt


def main():
    img = ft_load("animal.jpeg")
    # img = ft_load("notExist.jpeg")
    print(img)
    try:
        slice_image = img[100: 500, 450:850, 1:2]
    except TypeError as error:
        print(TypeError.__name__, error)
    else:
        plt.imshow(slice_image, cmap="gray")
        print("New shape after slicing: ", end="")
        print(f"{slice_image.shape} or {slice_image.shape[:2]}")
        plt.savefig('slice_image.jpeg')
        print(slice_image)
        plt.show()  # affiche sous forme de plt, avec l echelle de plt


if __name__ == "__main__":
    main()
