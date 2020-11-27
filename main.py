# Lab 2, variant 1
# Maxim Pupykin, group 6312

from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import os

path = input("Enter path to the image: ")
while not(os.path.exists(path) and os.path.splitext(path)[1].lower() == ".png"):
    path = input("Error: invalid path. Enter valid path to the image: ")

img = Image.open(path)
R, G, B = img.split()
r = np.array(R)
print("For R band:\nmax value = " + str(r.max()) + "\nmin value = " + str(r.min()) + "\naverage value = " + str(r.mean()))
g = np.array(G)
print("For G band:\nmax value = " + str(g.max()) + "\nmin value = " + str(g.min()) + "\naverage value = " + str(g.mean()))
b = np.array(B)
print("For B band:\nmax value = " + str(b.max()) + "\nmin value = " + str(b.min()) + "\naverage value = " + str(b.mean()))

cfs = np.array([0.299, 0.587, 0.114])
arr = np.array(img)
arr = arr * cfs
arr_out = np.uint8(arr[:, :, 0] + arr[:, :, 1] + arr[:, :, 2])
img_gs = Image.fromarray(arr_out, 'L')
img_gs.save("Lena_grayscaled.png")

x = np.arange(0, 256)
y = np.zeros(256)
ind = arr_out < 100
arr_out[ind] = 0
cnt = np.unique(arr_out, return_counts=True)
y[cnt[0]] = cnt[1]
img_th = Image.fromarray(arr_out, 'L')
img_th.save("Lena_thresholded.png")

plt.hist(x, weights=y, bins=20, color='g')
plt.title("Brightness distribution histogram")
plt.show()
