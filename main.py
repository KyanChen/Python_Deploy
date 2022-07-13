from tools import resize_img
import torch
from skimage import io,transform
import argparse

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--path', default='', type=str)
    args = args.parse_args()
    img = io.imread(args.path)
    img = torch.from_numpy(img)
    img = img.numpy()
    img = resize_img(img)
    io.imsave('test_out.jpg', img)


# pyinstaller -F main.py
# pyinstaller main.py