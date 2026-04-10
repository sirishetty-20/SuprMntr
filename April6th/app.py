import cv2

# Load image
img = cv2.imread("Dog.jpg")

# Print shape
print("Shape of image:", img.shape)

# Print pixel values (first 5 rows)
print("\nPixel values (sample):")
print(img[:5])

# Print number of channels
print("\nNumber of channels:", img.shape[2])