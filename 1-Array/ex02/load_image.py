
import cv2
import os
# conda install opencv
# conda install -c conda-forge libstdcxx-ng
# BGR != RBG pillow


def ft_load(path: str):
    """function that loads an image, prints its format, and its pixels
    content in RGB format."""
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(": file not found")
        if not os.access(path, os.R_OK):
            raise PermissionError(": Permission denied")
    except FileNotFoundError as error:
        print(FileNotFoundError.__name__, error)
    except PermissionError as error:
        print(PermissionError.__name__, error)
    else:
        image = cv2.imread(path)  # load
        cv2.imshow("landscape", image)  # display
        print("The shape of the image is: ", image.shape)
        im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return im_rgb


if __name__ == "__main__":
    # chmod 000 landscape_denied.jpeg
    print(".jpg")
    print(ft_load("landscape.jpg"))
    print()
    print(".png")
    print(ft_load("landscape.png"))
    print()
    print(".jpeg")
    print(ft_load("landscape.jpeg"))

    print()
    print("not exist")
    print(ft_load("landscape"))
    print()
    print("permision")
    print(ft_load("landscape_denied.jpeg"))
