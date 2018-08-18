from skimage import io, color, exposure, img_as_float
import matplotlib.pyplot as plt

image = img_as_float(io.imread('..\circulos.1.jpg'))
 
fig, ax = plt.subplots()
ax.imshow(image)

plt.show()