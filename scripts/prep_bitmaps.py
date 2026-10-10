import cv2
import numpy as np
from PIL import Image

# Open wasif_cutout.png
img = Image.open(r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets\wasif_cutout.png")
w, h = img.size
print("Cutout size:", w, h)

# We want target size 461 x 541
# In UG0510's hero card:
# The photo has head at the top and shoulders sloping down towards bottom
# Let's crop/resize:
# In wasif_cutout:
# Head top is around y=35.
# Torso bottom is at y=719.
# Center x is 360.
# If we crop from y=25 to 719 (height 694) and x from 75 to 645 (width 570)
# and resize to (461, 541)
crop_box = (65, 20, 655, 715)
cropped = img.crop(crop_box)
resized_hero = cropped.resize((461, 541), Image.Resampling.LANCZOS)
resized_hero.save(r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets\wasif_hero_461x541.png")
print("Saved wasif_hero_461x541.png")

# Also for connect.svg: target is 408 x 612
# Aspect ratio is 408 / 612 = 0.667
# Let's crop and resize for connect:
crop_box_connect = (85, 20, 635, 715)
cropped_conn = img.crop(crop_box_connect)
resized_conn = cropped_conn.resize((408, 612), Image.Resampling.LANCZOS)
resized_conn.save(r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets\wasif_connect_408x612.png")
print("Saved wasif_connect_408x612.png")
