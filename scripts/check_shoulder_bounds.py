import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Admin\Downloads\WhatsApp Image 2026-10-10 at 19.02.09.jpeg")
h, w = img.shape[:2]

# Let's inspect the left boundary on rows 500 to 719:
# Where does the shoulder start from the left edge (x=0)?
print("Left shoulder boundary:")
for y in range(500, 720, 20):
    row = img[y]
    # Find first pixel from x=0 going right where pixel != [255, 255, 255]
    diff = np.sum(np.abs(row.astype(int) - 255), axis=-1)
    # Background is <= 1 diff
    non_bg = np.where(diff > 2)[0]
    if len(non_bg) > 0:
        print(f"y={y}: left x={non_bg[0]} (diff={diff[non_bg[0]]}), right x={non_bg[-1]} (diff={diff[non_bg[-1]]})")
