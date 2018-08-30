import cv2
import skimage
from skimage import exposure
import matplotlib.pyplot as plt


def main():
    img_path = input("Path to image: ")
    show_img(fix_img(open_img(img_path)))


def fix_img(img):
    equ_img = skimage.exposure.equalize_hist(img, nbins=256, mask=None)
    log_correct = skimage.exposure.adjust_log(equ_img, 1)
    return log_correct


def show_img(img):
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()


def open_img(url):
    bgr_img = cv2.imread(url)
    b, g, r = cv2.split(bgr_img)
    rgb_img = cv2.merge([r, g, b])
    return rgb_img


if __name__ == "__main__":
    main()


"""
    TODO:
        1) Better adjust photos to allow underexposed and more overexposed photos to be fixed
        2) Show side by side of the original to the adjusted version
        3) Show histogram of image to show what was changed and how
        4) Better UX
        5) GUI interface instead of CLI
"""
