import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Admin\Downloads\WhatsApp Image 2026-10-10 at 19.02.09.jpeg")
for x in range(0, 300, 15):
    print(f"y=500, x={x:3d}: BGR={img[500, x]}")
print("---")
for x in range(0, 300, 15):
    print(f"y=580, x={x:3d}: BGR={img[580, x]}")
