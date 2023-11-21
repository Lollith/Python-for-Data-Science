'''program that should load the image "animal.jpeg", print some information
about it and display it after "zooming"'''
# Matplotlib convertit le tableau Numpy en une représentation interne
# propre à Matplotlib pour l'affichage. => sauvegarder avec cv2 pour avoir
# le format np; attention channel fantomes avec cv2 => va en afficher 3

from load_image import ft_load
from matplotlib import pyplot as plt
import cv2


def main():
    img = ft_load("animal.jpeg")
    print(img)
    slice_image = img[100: 500, 450:850, 1:2]
    plt.imshow(slice_image, cmap="gray")
    plt.show()  # affiche sous forme de plt, avec l echelle de plt
    print("New shape after slicing: ", end="")
    print(f"{slice_image.shape} or {slice_image.shape[:2]}")

    cv2.imwrite("slice_np.jpeg", slice_image)
    print(slice_image)


if __name__ == "__main__":
    main()
