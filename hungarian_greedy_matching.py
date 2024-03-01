import sys
import os
import pathlib
import numpy as np
import matplotlib
import mne
from mne.minimum_norm import make_inverse_operator, apply_inverse
from mne.coreg import Coregistration
from mne.io import read_info
import zickle as zkl
from ica import pca_whiten, ica1
import copy
import matplotlib.pyplot as plt
from scipy.optimize import linear_sum_assignment

path1="/data/.../M87160608+Study20151230+eyesclosedopen_session1_raw_EC_segment_new_raw.stc-lh.stc"
stc1 = mne.read_source_estimate(path1)
s1=stc1.data

path2="/data/.../M87155237+Study20160408+eyesclosedopen_session1_raw_EC_segment_new_raw.stc-rh.stc"
stc2 = mne.read_source_estimate(path2)
s2=stc2.data


path3="/data/.../M87196316+Study20180629+eyesclosedopen_session3_raw_EC_segment_raw.zkl"
stc3 = zkl.load(path3)
s3=stc3.data

#hungarian algo
def apply_hungarian_algorithm(correlation_matrix, name):
    # Perform the Hungarian algorithm to find the optimal assignment
    row_indices, col_indices = linear_sum_assignment(correlation_matrix)

    # Create the Hungarian similarity matrix based on the optimal assignment
    hungarian_similarity_matrix = np.zeros_like(correlation_matrix)
    for row, col in zip(row_indices, col_indices):
        hungarian_similarity_matrix[row, col] = 1 - correlation_matrix[row, col]

    # Print the column index of the largest similarity for each row
    largest_similarity_indices = np.argmax(hungarian_similarity_matrix, axis=1)
    print(f"Column index of the largest similarity for each row in {name}:")
    
    # Modifying this part to print as requested
    output_pairs = [(i, largest_similarity_indices[i]) for i in range(len(largest_similarity_indices))]
    print(output_pairs)

    # Save the results
    np.save(f'ix_{name}.npy', largest_similarity_indices)
    np.save(f'hungarian_similarity_matrix_{name}.npy', hungarian_similarity_matrix)
    plt.imsave(f'{name}.png', hungarian_similarity_matrix)

corr_s1_s2 = np.corrcoef(s1.T, s2.T)[:s1.shape[1], s1.shape[1]:]
abs_corr_s1_s2 = np.abs(corr_s1_s2)

# Calculate the cross-correlation matrix between s1 and s3
corr_s1_s3 = np.corrcoef(s1.T, s3.T)[:s1.shape[1], s1.shape[1]:]
# Calculate the absolute values of the cross-correlation coefficients
abs_corr_s1_s3 = np.abs(corr_s1_s3)

# Apply the Hungarian algorithm to each pair of component sets
apply_hungarian_algorithm(abs_corr_s1_s2, 's1_s2')
apply_hungarian_algorithm(abs_corr_s1_s3, 's1_s3')


###greedy algo
def apply_greedy_algorithm(correlation_matrix, name):
    # Copy the correlation matrix to avoid modifying the original
    corr_matrix = correlation_matrix.copy()

    # Initialize the matrix to store the matches (1 for match, 0 otherwise)
    greedy_similarity_matrix = np.zeros_like(corr_matrix)

    # List to store the index of the largest similarity for each row
    largest_similarity_indices = []

    # Greedy algorithm: Iteratively select the highest correlation pair
    while np.any(corr_matrix):
        # Find the indices of the maximum value in the correlation matrix
        row_idx, col_idx = np.unravel_index(corr_matrix.argmax(), corr_matrix.shape)
        max_value = corr_matrix[row_idx, col_idx]

        # If the maximum value is 0, break the loop (no more matches)
        if max_value == 0:
            break

        # Store the match in the similarity matrix and the index list
        greedy_similarity_matrix[row_idx, col_idx] = max_value
        largest_similarity_indices.append(col_idx)

        # Set the entire row and column for the chosen match to 0
        corr_matrix[row_idx, :] = 0
        corr_matrix[:, col_idx] = 0

    # Print the column index of the largest similarity for each row
    print(f"Column index of the largest similarity for each row in {name}:")

        # Modifying this part to print as requested
    output_pairs = [(i, largest_similarity_indices[i]) for i in range(len(largest_similarity_indices))]
    print(output_pairs)

    # Save the results
    np.save(f'ix_{name}_greedy.npy', largest_similarity_indices)
    np.save(f'greedy_similarity_matrix_{name}.npy', greedy_similarity_matrix)
    plt.imsave(f'{name}_greedy.png', greedy_similarity_matrix)

# Apply the greedy algorithm to each pair of component sets
apply_greedy_algorithm(abs_corr_s1_s2, 's1_s2')
apply_greedy_algorithm(abs_corr_s1_s3, 's1_s3')
