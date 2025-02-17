from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('/home/slaing/ML/2nd_year/sem2/xai/tiger.png')
img = img.resize((28,28))
img_array = np.array(img)
np.save('tiger.npy', img_array)
