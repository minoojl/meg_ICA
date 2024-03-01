import os
from PIL import Image
import matplotlib.pyplot as plt


# display images side by side: original, Hungarian match, and greedy match
def display_comparisons(directory_path1, directory_path2, Hungarian_matching, greedy_matching):
    sorted_files1 = load_and_sort_images(directory_path1)
    sorted_files2 = load_and_sort_images(directory_path2)

    # Determine the maximum number of rows
    num_rows = max(len(Hungarian_matching), len(greedy_matching))

    # Start plotting
    fig, axes = plt.subplots(num_rows, 3, figsize=(15, 5 * num_rows))  # 3 columns for original, Hungarian, and greedy

    for i in range(num_rows):
        # Original image from directory 1
        original_img_index = i
        if original_img_index < len(sorted_files1):
            original_img = Image.open(os.path.join(directory_path1, sorted_files1[original_img_index]))
            axes[i, 0].imshow(original_img)
            axes[i, 0].set_title(f"Original {i}")
            axes[i, 0].axis('off')

        # Hungarian match from directory 2
        hungarian_match_index = [pair[1] for pair in Hungarian_matching if pair[0] == i]
        if hungarian_match_index:
            hungarian_img = Image.open(os.path.join(directory_path2, sorted_files2[hungarian_match_index[0]]))
            axes[i, 1].imshow(hungarian_img)
            axes[i, 1].set_title(f"Hungarian Match {i}")
            axes[i, 1].axis('off')

        # Greedy match from directory 2
        greedy_match_index = [pair[1] for pair in greedy_matching if pair[0] == i]
        if greedy_match_index:
            greedy_img = Image.open(os.path.join(directory_path2, sorted_files2[greedy_match_index[0]]))
            axes[i, 2].imshow(greedy_img)
            axes[i, 2].set_title(f"Greedy Match {i}")
            axes[i, 2].axis('off')

    plt.tight_layout()
    plt.show()

# Use the function with specified directory paths and matching lists
directory_path1 = "/Users/minoolou/Desktop/1/A00063430"
directory_path2 = "/Users/minoolou/Desktop/1/A00066226"
Hungarian_matching = [(0, 2), (1, 8), (2, 1),(3,6)]
greedy_matching = [(0, 7), (1, 2), (2, 5),(3,9)]

display_comparisons(directory_path1, directory_path2, Hungarian_matching, greedy_matching)
