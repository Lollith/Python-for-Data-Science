''' program which must load the image "animal.jpeg", cut a square part from it
and transpose it to produce the image below. It should display it, print the
new shape and the data of the image after the transpose.'''


from load_image import ft_load
from matplotlib import pyplot as plt


def main():
    img = ft_load("animal.jpeg")
    print(img)
    slice_image = img[100: 500, 450:850, 1:2]
    plt.imshow(slice_image, cmap="gray")
    print("New shape after slicing: ", end="")
    print(f"{slice_image.shape} or {slice_image.shape[:2]}")
    plt.savefig('slice_image.jpeg')
    print(slice_image)
    plt.show()

if __name__ == "__main__":
    main()
