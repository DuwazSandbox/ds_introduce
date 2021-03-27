from matplotlib import pyplot as plt
def plti(im, h=6, **kwargs):
    """
    Helper function to plot an image.
    """
    y = im.shape[0]
    x = im.shape[1]
    w = (y/x) * h
    plt.figure(figsize=(w,h))
    plt.imshow(im, interpolation="nearest", **kwargs)
    plt.axis('off')
    plt.show()