from matplotlib.pyplot import imread
from matplotlib.pyplot import imsave
from scipy import misc
from scipy import ndimage

from skimage import io, color
from skimage.transform import resize

def blur_image(image, sigma):
    blurred=ndimage.gaussian_filter(image,sigma=sigma)
    imsave('blurred.png', blurred)

def resize_image(image, new_height):
    resolution = list(image.shape) # height is [0], width is [1]
    ratio = resolution[1] / resolution[0]
    new_width = int(new_height * ratio)
    resized = resize(image, (new_height,new_width))
    imsave('resized.png', resized)
