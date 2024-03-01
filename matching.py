import os
from PIL import Image
import matplotlib.pyplot as plt
import re

def load_and_sort_images(directory_path):
    """Load and return a sorted list of image filenames from a directory, sorted by the numerical part in their names."""
    files = os.listdir(directory_path)
    image_files = [f for f in files if f.endswith('.jpg') or f.endswith('.png')]
    sorted_files = sorted(image_files, key=lambda x: float(re.findall(r"(\d+\.\d+)", x)[0]))
    return sorted_files

def display_comparisons(directory_path1, directory_path2, Hungarian_matching, greedy_matching):
    sorted_files1 = load_and_sort_images(directory_path1)
    sorted_files2 = load_and_sort_images(directory_path2)

    num_rows = max(len(Hungarian_matching), len(greedy_matching))
    fig, axes = plt.subplots(num_rows, 3, figsize=(15, 5 * num_rows))
    if num_rows == 1:
        axes = np.expand_dims(axes, 0)  

    for i in range(num_rows):
        if i < len(sorted_files1):
            original_img = Image.open(os.path.join(directory_path1, sorted_files1[i]))
            axes[i, 0].imshow(original_img)
            axes[i, 0].set_title(f"Original {i}")
            axes[i, 0].axis('off')

        hungarian_match_index = next((pair[1] for pair in Hungarian_matching if pair[0] == i), None)
        if hungarian_match_index is not None and hungarian_match_index < len(sorted_files2):
            hungarian_img = Image.open(os.path.join(directory_path2, sorted_files2[hungarian_match_index]))
            axes[i, 1].imshow(hungarian_img)
            axes[i, 1].set_title(f"Hungarian Match {i}")
            axes[i, 1].axis('off')

        greedy_match_index = next((pair[1] for pair in greedy_matching if pair[0] == i), None)
        if greedy_match_index is not None and greedy_match_index < len(sorted_files2):
            greedy_img = Image.open(os.path.join(directory_path2, sorted_files2[greedy_match_index]))
            axes[i, 2].imshow(greedy_img)
            axes[i, 2].set_title(f"Greedy Match {i}")
            axes[i, 2].axis('off')

    plt.tight_layout()
    plt.show()

# specified directory paths and matching lists
directory_path1 = "/Users/.../A00063430"
directory_path2 = "/Users/.../A00066226"
Hungarian_matching = [(0, 22), (1, 30), (2, 41), (3, 13)]
greedy_matching = [(0, 7), (1, 2), (2, 5), (3, 9)]

display_comparisons(directory_path1, directory_path2, Hungarian_matching, greedy_matching)
