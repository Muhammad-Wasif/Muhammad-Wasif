import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Admin\Downloads\WhatsApp Image 2026-10-10 at 19.02.09.jpeg")
h, w = img.shape[:2]

# Let's inspect where the collar is:
# The tie is at y=600..719, x=340..420
# What about the collar lapels?
# The left collar point is around y=680, x=270
# The right collar point is around y=680, x=480
# The shoulder lines:
# Left shoulder goes from (x=240, y=520) down to (x=45, y=600) down to (x=45, y=719)
# Right shoulder goes from (x=500, y=520) down to (x=675, y=600) down to (x=675, y=719)

# Let's check the pixels inside the shirt:
print("Collar tips and tie:")
print("y=600, x=380 (tie):", img[600, 380])
print("y=680, x=270 (collar left tip):", img[680, 270])
print("y=680, x=480 (collar right tip):", img[680, 480])
print("y=650, x=200 (left shoulder/shirt):", img[650, 200])
print("y=650, x=550 (right shoulder/shirt):", img[650, 550])
