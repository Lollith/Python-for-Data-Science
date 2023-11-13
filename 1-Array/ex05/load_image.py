
import cv2
import os
# opencv
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
        image = cv2.imread(path)
        cv2.imshow("image", image)
        print("The shape of the image is: ", image.shape)
        im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(im_rgb)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return im_rgb


if __name__ == "__main__":
    print(ft_load("landscape.jpg"))
    print()
    print(ft_load("landscape.png"))

    print()
    print(ft_load("landscape"))
    print()
    print(ft_load("landscape_denied.jpeg"))
