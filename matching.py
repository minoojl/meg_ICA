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
directory_path1 = "/Users/.../1/A00063430"
directory_path2 = "/Users/.../1/A00066226"
Hungarian_matching = [(0, 82), (1, 25), (2, 68), (3, 35), (4, 75), (5, 42), (6, 65), (7, 73), (8, 34), (9, 36), (10, 81), (11, 32), (12, 63), (13, 20), (14, 49), (15, 18), (16, 98), (17, 4), (18, 94), (19, 2), (20, 16), (21, 45), (22, 96), (23, 26), (24, 59), (25, 58), (26, 5), (27, 40), (28, 70), (29, 85), (30, 76), (31, 67), (32, 97), (33, 57), (34, 17), (35, 23), (36, 22), (37, 43), (38, 27), (39, 0), (40, 3), (41, 84), (42, 52), (43, 56), (44, 50), (45, 24), (46, 29), (47, 62), (48, 89), (49, 14), (50, 38), (51, 74), (52, 77), (53, 10), (54, 41), (55, 66), (56, 1), (57, 39), (58, 37), (59, 33), (60, 55), (61, 9), (62, 30), (63, 13), (64, 99), (65, 21), (66, 28), (67, 15), (68, 78), (69, 47), (70, 83), (71, 53), (72, 11), (73, 71), (74, 19), (75, 72), (76, 88), (77, 6), (78, 61), (79, 51), (80, 90), (81, 64), (82, 44), (83, 31), (84, 91), (85, 8), (86, 46), (87, 86), (88, 69), (89, 60), (90, 79), (91, 92), (92, 48), (93, 12), (94, 95), (95, 54), (96, 93), (97, 80), (98, 87), (99, 7)]
greedy_matching = [(0, 27), (1, 99), (2, 32), (3, 23), (4, 29), (5, 8), (6, 77), (7, 19), (8, 95), (9, 51), (10, 39), (11, 57), (12, 18), (13, 12), (14, 22), (15, 79), (16, 63), (17, 10), (18, 78), (19, 52), (20, 36), (21, 80), (22, 11), (23, 89), (24, 24), (25, 6), (26, 76), (27, 30), (28, 9), (29, 61), (30, 21), (31, 81), (32, 73), (33, 53), (34, 45), (35, 66), (36, 86), (37, 17), (38, 43), (39, 50), (40, 69), (41, 82), (42, 54), (43, 65), (44, 72), (45, 68), (46, 2), (47, 7), (48, 1), (49, 15), (50, 74), (51, 25), (52, 70), (53, 14), (54, 35), (55, 5), (56, 83), (57, 4), (58, 46), (59, 26), (60, 28), (61, 59), (62, 49), (63, 44), (64, 87), (65, 93), (66, 3), (67, 31), (68, 13), (69, 97), (70, 62), (71, 33), (72, 91), (73, 16), (74, 58), (75, 67), (76, 55), (77, 56), (78, 71), (79, 40), (80, 90), (81, 75), (82, 37), (83, 20), (84, 60), (85, 48), (86, 98), (87, 38), (88, 94), (89, 64), (90, 34), (91, 85), (92, 47), (93, 42), (94, 0), (95, 84), (96, 96), (97, 41), (98, 88), (99, 92)]

display_comparisons(directory_path1, directory_path2, Hungarian_matching, greedy_matching)
