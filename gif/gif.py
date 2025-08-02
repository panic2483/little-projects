import imageio.v3 as iio

filenames = ["gif/chicklet1.png", "gif/chicklet2.png", "gif/chicklet3.png", "gif/chicklet4.png"]
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("gif/chicken.gif", images, duration=500, loop = 0)