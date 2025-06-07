from PIL import Image
import random
import glob
import numpy as np
import matplotlib.pyplot as plt
import os

image_list = []
rows = []

# Load images into image_list
# Use raw string to avoid escape character issues
for filename in glob.glob(r'C:\Users\aryan\Desktop\New folder\archive\images\*.jpg'):
    try:
        im = Image.open(filename)
        rows.append([filename])
        image_list.append(filename)
    except Exception as e:
        print(f"Error loading image {filename}: {e}")

print(f"Number of images loaded: {len(image_list)}")

# Check if images were loaded
if not image_list:
    raise ValueError("No images found in the specified directory.")

def gallery(array, ncols=8):
    nindex, height, width, intensity = array.shape
    nrows = nindex // ncols
    assert nindex == nrows * ncols
    result = (array.reshape(nrows, ncols, height, width, intensity)
              .swapaxes(1, 2)
              .reshape(height * nrows, width * ncols, intensity))
    return result

def make_array():
    arr = []
    # Randomly select 64 images to visualize
    for i in range(64):
        random_image = random.choice(image_list)
        arr.append(np.asarray(Image.open(random_image).convert('RGB')))
    return np.array(arr)

# Only run if there are enough images
if len(image_list) >= 64:
    array = make_array()
    result = gallery(array)
    plt.figure(figsize=(8, 8))
    plt.imshow(result)
    plt.axis('off')
    plt.show()
else:
    print("Not enough images to fill the gallery. At least 64 images are needed.")

















