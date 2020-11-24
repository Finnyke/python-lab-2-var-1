# Lab 2, variant 1
# Maxim Pupykin, group 6312

from PIL import Image
from matplotlib import pyplot
import numpy
import os

path = input("Enter path to the image: ")
while not(os.path.exists(path) and os.path.splitext(path)[1].lower() == ".png"):
    path = input("Error: invalid path. Enter valid path to the image: ")

img = Image.open(path)
R, G, B = img.split()
r = numpy.array(R)
print("For R band:\nmax value = " + str(r.max()) + "\nmin value = " + str(r.min()) + "\naverage value = " + str(r.mean()))
g = numpy.array(G)
print("For G band:\nmax value = " + str(g.max()) + "\nmin value = " + str(g.min()) + "\naverage value = " + str(g.mean()))
b = numpy.array(B)
print("For B band:\nmax value = " + str(b.max()) + "\nmin value = " + str(b.min()) + "\naverage value = " + str(b.mean()))

cfs = numpy.array([0.299, 0.587, 0.114])
arr = numpy.array(img)
arr_L = numpy.zeros((arr.shape[0], arr.shape[1]), dtype=numpy.uint8)
arr_L[0:, 0:] = numpy.uint8(arr[0:, 0:, 0] * cfs[0] + arr[0:, 0:, 1] * cfs[1] + arr[0:, 0:, 2] * cfs[2])
img_gs = Image.fromarray(arr_L, 'L')
img_gs.save("Lena_grayscaled.png")

x = numpy.arange(0, 256)
y = numpy.zeros(256)
ind = arr_L < 50
arr_L[ind] = 0
cnt = numpy.unique(arr_L, return_counts=True)
y[cnt[0]] = cnt[1]
img_th = Image.fromarray(arr_L, 'L')
img_th.save("Lena_thresholded.png")

pyplot.figure(figsize=(12, 6))
pyplot.bar(x, y)
pyplot.show()
