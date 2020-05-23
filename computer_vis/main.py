from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt

from scipy import ndimage

image = plt.imread('1.jpeg')
image.shape
plt.imshow(image)