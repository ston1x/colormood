def blur_image():
    from matplotlib.pyplot import imread
    from matplotlib.pyplot import imsave
    from scipy import misc
    from scipy import ndimage
    # f = misc.face()
    f = imread('demo.png')
    blurred=ndimage.gaussian_filter(f,sigma=(10, 10, 0))
    imsave('blurred.png',blurred)
