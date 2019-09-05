from matplotlib.pyplot import imread
from matplotlib.pyplot import imsave
from scipy import misc
from scipy import ndimage

f = misc.face()
blurred=ndimage.gaussian_filter(f,sigma=(10, 10, 0))
imsave('blurred.png',blurred)
