# Lab 1, variant 3
# Maxim Pupykin, group 6312

from PIL import Image
from matplotlib import pyplot
import numpy
import os

path = input("Enter path to the image: ")
while not(os.path.exists(path)):
    path = input("Error: invalid path. Enter valid path to the image: ")

img = Image.open(path)
R, G, B = img.split()
r = numpy.array(R)
print("For R band:\nmax value = " + str(r.max()) + "\nmin value = " + str(r.min()) + "\naverage value = " +
      str(r.mean()))
g = numpy.array(G)
print("For G band:\nmax value = " + str(g.max()) + "\nmin value = " + str(g.min()) + "\naverage value = " +
      str(g.mean()))
b = numpy.array(B)
print("For B band:\nmax value = " + str(b.max()) + "\nmin value = " + str(b.min()) + "\naverage value = " +
      str(b.mean()))

arr = numpy.array(img)
for line in arr:
    for pixel in line:
        val = pixel[0] * 0.299 + pixel[1] * 0.587 + pixel[2] * 0.114
        pixel[0] = pixel[1] = pixel[2] = val
img_gs = Image.fromarray(arr)
img_gs.save("Lena_grayscaled.png")

x = numpy.arange(0, 256)
y = numpy.zeros(256)
for line in arr:
    for pixel in line:
        if pixel[0] < 50:
            pixel[0] = pixel[1] = pixel[2] = 0
        y[pixel[0]] += 1
img_th = Image.fromarray(arr)
img_th.save("Lena_thresholded.png")

pyplot.figure(figsize=(12, 6))
pyplot.bar(x, y)
pyplot.show()
