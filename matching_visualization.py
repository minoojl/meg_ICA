import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import re

def load_and_sort_images(directory_path):
    """Load and return a sorted list of image filenames from a directory, sorted by the numerical part in their names."""
    files = os.listdir(directory_path)
    image_files = [f for f in files if f.endswith('.jpg') or f.endswith('.png')]
    def sort_key(x):
        numbers = re.findall(r"(\d+\.\d+|\d+)", x)
        return float(numbers[0]) if numbers else float('inf')
    sorted_files = sorted(image_files, key=sort_key)
    return sorted_files

def display_comparisons_by_pairs(directory_path1, directory_path2, greedy_matching):
    sorted_files1 = load_and_sort_images(directory_path1)
    sorted_files2 = load_and_sort_images(directory_path2)

    # Three pairs per row, so six images per row.
    pairs_per_row = 3
    num_rows = np.ceil(len(greedy_matching) / pairs_per_row).astype(int)
    num_cols = pairs_per_row * 2  # Two images (original and match) per pair

    # Assuming all images have the same size, get the size of the first image to compute figure size
    example_image = Image.open(os.path.join(directory_path1, sorted_files1[0]))
    image_width, image_height = example_image.size
    # Set up figure size based on the number of images and their size
    fig_width = image_width * num_cols / 100  # Convert pixels to inches for figure size
    fig_height = image_height * num_rows / 100

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(fig_width, fig_height))

    if num_rows == 1:
        axes = np.expand_dims(axes, 0)  # Ensure axes is always a 2D array for consistency

    for idx, (orig_index, match_index) in enumerate(greedy_matching):
        row = idx // pairs_per_row
        col = (idx % pairs_per_row) * 2  # Column index for the original image

        if orig_index < len(sorted_files1):
            original_img = Image.open(os.path.join(directory_path1, sorted_files1[orig_index]))
            axes[row, col].imshow(original_img)
            axes[row, col].axis('off')

        if match_index < len(sorted_files2):
            matched_img = Image.open(os.path.join(directory_path2, sorted_files2[match_index]))
            axes[row, col + 1].imshow(matched_img)
            axes[row, col + 1].axis('off')

    # Hide any unused subplots
    for ax in axes.flat[idx * 2 + 2:]:
        ax.axis('off')

    # Adjust subplots to remove whitespace
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    plt.show()

directory_path1 = "/Users/minoolou/Desktop/1/A00063430"
directory_path2 = "/Users/minoolou/Desktop/1/A00066226"
greedy_matching = [(92, 16), (65, 9), (2, 78), (66, 34), (42, 74), (77, 75), (39, 76), (54, 55), (82, 94), (50, 40), (88, 26), (34, 67), (4, 11), (15, 49), (67, 62), (41, 7), (60, 38), (17, 71), (49, 37), (91, 10), (85, 41), (90, 5), (25, 58), (98, 99), (36, 6), (79, 21), (28, 35), (70, 88), (46, 29), (48, 17), (53, 24), (94, 18), (86, 46), (58, 86), (18, 77), (96, 23), (40, 72), (52, 96), (61, 61), (89, 1), (31, 85), (62, 14), (78, 50), (33, 89), (69, 13), (72, 0), (14, 93), (37, 42), (11, 73), (93, 22), (21, 90), (56, 28), (10, 32), (38, 20), (8, 15), (20, 64), (24, 59), (3, 80), (84, 87), (16, 97), (13, 79), (95, 92), (47, 91), (97, 39), (30, 98), (55, 8), (12, 31), (63, 2), (75, 57), (7, 47), (5, 68), (43, 25), (87, 53), (74, 95), (76, 19), (19, 27), (27, 82), (44, 69), (51, 51), (83, 33), (80, 84), (68, 48), (22, 45), (29, 36), (6, 70), (23, 81), (71, 3), (1, 44), (26, 43), (45, 56), (64, 30), (73, 65), (9, 63), (59, 54), (32, 66), (0, 12), (57, 83), (81, 60), (35, 52)]

#isplay_comparisons_close(directory_path1, directory_path2, greedy_matching)
display_comparisons_by_pairs(directory_path1, directory_path2, greedy_matching)

