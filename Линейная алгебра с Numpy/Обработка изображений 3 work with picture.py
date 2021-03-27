from plti import plti
import numpy as np
from matplotlib import pyplot as plt

im = plt.imread("lenna.png")
plti(im)

# remove transparence
im_without_transparence = im[:,:,:3]
plti(im_without_transparence[20:200, 0:100, :]) #show just part

# negative
plti(1 - im_without_transparence)

# black and white
plti(np.mean(im, axis=2), cmap='gist_gray') # why axis=2 and mean???

# set yellow square
im_stub = im_without_transparence
im_stub[:100, :100, :] = [1, 1, 0]
plti(im_stub)