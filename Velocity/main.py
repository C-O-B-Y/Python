import numpy as np
import cv2
import skimage
from skimage import exposure
import matplotlib.pyplot as plt


def main():
    img_path = input("Path to image: ")
    # image = open_img(input("What is the path to your image: "))
    show_histogram(img_path)
    show_img(fix_img(open_img(img_path)))


def fix_img(img):
    equ_img = skimage.exposure.equalize_hist(img, nbins=256, mask=None)
    log_correct = skimage.exposure.adjust_log(equ_img, 1)
    return log_correct


def show_histogram(img):
    image = cv2.imread(img, 0)

    hist, bins = np.histogram(image.flatten(), 256, [0, 256])

    cdf = hist.cumsum()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0)

    image2 = cdf[image]

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    plt.plot(cdf_normalized, color='b')
    plt.hist(image2.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()


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

