import os
import numpy as np
import json
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt

def create_density_map(points, img_shape, sigma=5):
    density_map = np.zeros(img_shape)
    for point in points:
        x, y = point
        x = int(round(x))
        y = int(round(y))
        if x < img_shape[1] and y < img_shape[0]:
            density_map[y, x] += 1  # Corrected indexing: (row, column)
    density_map = gaussian_filter(density_map, sigma)
    return density_map

def generate_density_maps(annotation_file, image_name):
    with open(annotation_file) as f:
        annotations = json.load(f)
    

    for img_name, annotation in annotations.items():
        if(img_name == image_name):
            points = annotation['points']
            img_shape = (annotation['H'], annotation['W'])
            density_map = create_density_map(points, img_shape)
            density_map_path = "density_maps/"

            img = plt.imread(img_name)
            # Plot the image
            plt.imshow(img)

            # Plot the density map overlay
            plt.imshow(density_map, cmap='jet', alpha=0.5, extent=[0, img_shape[1], img_shape[0], 0])

            plt.show()

            # Get the base name of the image file without the extension
            base_name = os.path.splitext(img_name)[0]
            density_map_file = os.path.join(density_map_path, base_name + ".npy")
            
            np.save(density_map_file, density_map)
            print(f"Density map saved: {density_map_file}")

if __name__ == "__main__":
    annotation_file = "annotation_FSC147_384.json"  # Replace with the path to your annotation JSON file
    # image_dir = ""  # Replace with the directory containing the images
    image_files = ['8006','8008','8011','8012','8015','8016','8017','8018','8019','8020','8021','8022','8023','8024']
    image_file_list = [x+".jpg" for x in image_files ]
    for image_name in image_file_list:
        generate_density_maps(annotation_file, image_name)
