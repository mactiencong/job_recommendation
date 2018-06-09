import pandas as pd
from scipy.spatial.distance import cosine
if __name__== '__main__':
    data = pd.read_csv('jobs.csv')
    print(data.head(11).ix[:,0:10])
    data = data.drop('info', 1)
    job_based_data_frame = pd.DataFrame(index=data.columns, columns=data.columns)
    print(job_based_data_frame.head(10).ix[:,0:10])

    len_job_based_data_frame = len(job_based_data_frame.columns)

    for i in range(0, len_job_based_data_frame):
        for j in range(0, len_job_based_data_frame):
            job_based_data_frame.ix[i,j] = 1 - cosine(data.ix[:,i], data.ix[:,j])

    print(job_based_data_frame.head(10).ix[:,0:10])
    job_related = pd.DataFrame(index=job_based_data_frame.columns, columns = range(0, 5))
    for i in range(0, len_job_based_data_frame):
        job_related.ix[i, :5] = job_based_data_frame.ix[0:, i].sort_values(ascending=False)[:5].index

    print(job_related)
    print(job_related.ix['job1', 0])