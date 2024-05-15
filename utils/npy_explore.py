import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Define the paths to the files
npy_file_path = "8007.npy"
jpg_file_path = "8007.jpg"

# Load the .npy file
data = np.load(npy_file_path)

# Load the .jpg image
image = Image.open(jpg_file_path)

# Print properties of the files
print("Properties of the .npy file:")
print("Shape:", data.shape)
print("Data type:", data.dtype)

print("\nProperties of the .jpg file:")
print("Size:", image.size)
print("Mode:", image.mode)
print("Format:", image.format)

# Plot the .npy data
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(data, cmap='viridis')
plt.title("Numpy Data")

# Plot the .jpg image
plt.subplot(1, 2, 2)
plt.imshow(image)
plt.title("JPG Image")

plt.show()