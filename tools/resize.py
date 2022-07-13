from skimage import transform

def resize_img(img):
    return transform.resize(img, (112, 112))