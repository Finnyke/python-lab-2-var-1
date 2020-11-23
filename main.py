# Lab 2, variant 1
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
print("For R band:\nmax value = " + str(r.max()) + "\nmin value = " + str(r.min()) + "\naverage value = " + str(r.mean()))
g = numpy.array(G)
print("For G band:\nmax value = " + str(g.max()) + "\nmin value = " + str(g.min()) + "\naverage value = " + str(g.mean()))
b = numpy.array(B)
print("For B band:\nmax value = " + str(b.max()) + "\nmin value = " + str(b.min()) + "\naverage value = " + str(b.mean()))

arr = numpy.array(img)
arr_L = numpy.zeros((arr.shape[0], arr.shape[1]), dtype=numpy.uint8)
for i in range(0, arr.shape[0]):
    for j in range(0, arr.shape[1]):
        arr_L[i][j] += arr[i][j][0] * 0.299 + arr[i][j][1] * 0.587 + arr[i][j][2] * 0.114
img_gs = Image.fromarray(arr_L, 'L')
img_gs.save("Lena_grayscaled.png")

x = numpy.arange(0, 256)
y = numpy.zeros(256)
for i in range(0, arr_L.shape[0]):
    for j in range(0, arr_L.shape[1]):
        if arr_L[i][j] < 50:
            arr_L[i][j] = 0
        y[arr_L[i][j]] += 1
img_th = Image.fromarray(arr_L, 'L')
img_th.save("Lena_thresholded.png")

pyplot.figure(figsize=(12, 6))
pyplot.bar(x, y)
pyplot.show()
