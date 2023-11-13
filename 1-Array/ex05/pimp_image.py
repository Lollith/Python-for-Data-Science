from load_image import ft_load
import cv2
# BGR != RBG pillow


def ft_invert(array):
    """Inverts the colors of the image received"""
    invert = cv2.bitwise_not(array)
    cv2.imwrite("invert.jpeg", invert)
    return invert


# set blue and green channels to 0
def ft_red(array):
    """Apply a red filter to the image received"""
    r = array.copy()
    r[:, :, 0] = 0
    r[:, :, 1] = 0
    cv2.imwrite("red.jpeg", r)
    print("red shape is the same: ", r.shape)
    return r


def ft_green(array):
    """Apply a green filter to the image received"""
    g = array.copy()
    g[:, :, 0] = 0
    g[:, :, 2] = 0
    cv2.imwrite("green.jpeg", g)
    return g


def ft_blue(array):
    """Apply a blue filter to the image received"""
    b = array.copy()
    b[:, :, 1] = 0
    b[:, :, 2] = 0
    cv2.imwrite("blue.jpeg", b)
    return b


def ft_grey(array):
    """Converting the image received to gray scale """
    grey = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grey.jpeg", grey)
    return grey


if __name__ == "__main__":
    array = ft_load("landscape.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)