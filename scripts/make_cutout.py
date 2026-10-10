import cv2
import numpy as np

img_path = r"C:\Users\Admin\Downloads\WhatsApp Image 2026-10-10 at 19.02.09.jpeg"
out_path = r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets\wasif_cutout.png"
preview_path = r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets\wasif_cutout_preview.png"

img = cv2.imread(img_path)
h, w = img.shape[:2]

mask = np.zeros((h, w), np.uint8)

# 1. Definite Background everywhere initially
mask[:, :] = cv2.GC_BGD

# 2. Transition zone / probable foreground for head & shoulders
# Head bounding box: y from 35 to 500, x from 180 to 535
mask[35:500, 180:535] = cv2.GC_PR_FGD

# Definite Foreground for core face & head:
mask[70:460, 240:480] = cv2.GC_FGD

# 3. Torso polygon (shoulders, shirt, tie)
# Points:
# Top neck: (240, 500) -> (160, 530) -> (90, 560) -> (50, 590) -> (40, 719)
# Bottom: (40, 719) -> (675, 719)
# Right: (675, 719) -> (675, 590) -> (655, 560) -> (580, 530) -> (510, 500)
torso_poly = np.array([
    [240, 500],
    [160, 530],
    [90, 560],
    [50, 590],
    [40, 719],
    [675, 719],
    [675, 590],
    [655, 560],
    [580, 530],
    [510, 500],
    [375, 530]
], dtype=np.int32)

# Fill torso as DEFINITE FOREGROUND
cv2.fillPoly(mask, [torso_poly], cv2.GC_FGD)

# Boundary margin marked as GC_PR_FGD
torso_boundary_mask = np.zeros((h, w), np.uint8)
cv2.polylines(torso_boundary_mask, [torso_poly[:5]], False, 255, 12)
cv2.polylines(torso_boundary_mask, [torso_poly[5:10]], False, 255, 12)
mask[torso_boundary_mask > 0] = cv2.GC_PR_FGD

# Definite foreground for tie and neck
mask[460:719, 260:480] = cv2.GC_FGD

# Explicitly ensure the space to the left of the jaw (x < 185, y < 490) is GC_BGD
mask[0:490, 0:185] = cv2.GC_BGD
# Explicitly ensure the space to the right of the head (x > 535, y < 500) is GC_BGD
mask[0:500, 535:w] = cv2.GC_BGD

# Run GrabCut
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

cv2.grabCut(img, mask, None, bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_MASK)

# Create binary mask
bin_mask = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

# Ensure interior of torso & neck is solid
cv2.fillPoly(bin_mask, [torso_poly], 255)
bin_mask[460:719, 260:480] = 255

# Clean outside regions
bin_mask[0:490, 0:185] = 0
bin_mask[0:500, 535:w] = 0

# Slight blur for smooth antialiasing
bin_mask = cv2.GaussianBlur(bin_mask, (3, 3), 0)

# RGBA
b, g, r = cv2.split(img)
rgba = cv2.merge([b, g, r, bin_mask])
cv2.imwrite(out_path, rgba)
print("Saved cutout to:", out_path)

# Dark theme preview
bg_dark = np.zeros((h, w, 3), dtype=np.uint8)
bg_dark[:] = (22, 11, 7) # #070b16
alpha_norm = (bin_mask.astype(float) / 255.0)[:, :, None]
composited = (img * alpha_norm + bg_dark * (1.0 - alpha_norm)).astype(np.uint8)
cv2.imwrite(preview_path, composited)
print("Saved preview to:", preview_path)
