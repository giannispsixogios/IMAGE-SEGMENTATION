# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:26:42 2023

@author: giannisps
"""

import rasterio
from rasterio.windows import Window
from skimage.segmentation import slic
from skimage.color import label2rgb
import matplotlib.pyplot as plt

# Load Sentinel-2 image
image_file = r'C:\Users\GNR\Desktop\download.jpg'
with rasterio.open(image_file) as src:
    image = src.read()

# Extract one of the bands (e.g., red, green, blue) for image segmentation
band_number = 2  # Change this to the band number you want to use
image = image[band_number, :, :]

# Perform image segmentation using SLIC
segments = slic(image, n_segments=9000, compactness=0.08)

# Color the segments for visualization
segmented_image = label2rgb(segments, image, kind='avg')

# Save the segmented image on the desktop
output_file = r"C:\Users\GNR\Desktop\final_image9.tif"
with rasterio.open(output_file, 'w', driver='GTiff', width=image.shape[1], height=image.shape[0],
                   count=3, dtype=segmented_image.dtype) as dst:
    dst.write(segmented_image.transpose(2, 0, 1))

print(f"Segmented image saved at {output_file}")