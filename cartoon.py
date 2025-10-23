# ----------------------------------------------------------
# Project Title  : Cartooning an Image using OpenCV
# Author         : [Your Name]
# Course         : B.Sc. (Artificial Intelligence)
# Tool Used      : Python (VS Code)
# Libraries Used : OpenCV, NumPy
# ----------------------------------------------------------

# Import required libraries
import cv2
import numpy as np

# ----------------------------------------------------------
# Step 1: Read the Image
# ----------------------------------------------------------
img = cv2.imread("amma nanna.jpg")

# Resize the image for uniform processing
img = cv2.resize(img, (800, 800))

# ----------------------------------------------------------
# Step 2: Convert to Grayscale
# ----------------------------------------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ----------------------------------------------------------
# Step 3: Apply Median Blur to Reduce Noise
# ----------------------------------------------------------
gray_blur = cv2.medianBlur(gray, 7)

# ----------------------------------------------------------
# Step 4: Detect Edges (Refined)
# ----------------------------------------------------------
edges = cv2.adaptiveThreshold(gray_blur, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY,
                              9, 9)

# ----------------------------------------------------------
# Step 5: Smoothen Colors using Bilateral Filter
# ----------------------------------------------------------
# Increase diameter and sigma values for smoother colors
color = cv2.bilateralFilter(img, d=9, sigmaColor=250, sigmaSpace=250)

# ----------------------------------------------------------
# Step 6: Combine Edges with the Smoothed Color Image
# ----------------------------------------------------------
# Convert edges to color for blending
edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Blend the smoothed color image and edges for clarity
cartoon = cv2.bitwise_and(color, edges_colored)

# ----------------------------------------------------------
# Step 7: Enhance Brightness (Optional)
# ----------------------------------------------------------
# This step makes the cartoon appear more vivid
cartoon = cv2.convertScaleAbs(cartoon, alpha=1.2, beta=15)

# ----------------------------------------------------------
# Step 8: Display All Results
# ----------------------------------------------------------
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Edge Mask", edges)
cv2.imshow("Cartoon Image", cartoon)

# Wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional: Save the cartoon image
cv2.imwrite("cartoon_output_clear.jpg", cartoon)
print("Cartoon image saved successfully as 'cartoon_output_clear.jpg'")

