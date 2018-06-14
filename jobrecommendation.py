import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.model_selection import train_test_split

if __name__== '__main__':
    data = pd.read_csv('data.csv')

    def values_to_map_index(values):
        map_index, idx = {}, 0
        for val in values:
            map_index[val] = idx
            idx += 1
        return map_index

    user_idx = values_to_map_index(data.user.unique())
    job_idx = values_to_map_index(data.job.unique())

    data_matrix = np.zeros((len(user_idx), len(job_idx)))

    for line in data.itertuples():
        user, job, view = line[1], line[2], line[3]
        data_matrix[user_idx[user], job_idx[job]] = view

    user_similarity = pairwise_distances(data_matrix, metric='cosine', n_jobs=-1)
    job_similarity = pairwise_distances(data_matrix.T, metric='cosine', n_jobs=-1)

    # print(data_matrix)
    # print(user_similarity)

    u, s, vt = svds(data_matrix, len(data_matrix))
    print(u, s, vt)