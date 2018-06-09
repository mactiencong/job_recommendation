import pandas as pd
from scipy.spatial.distance import cosine
data = pd.read_csv('data.csv')
data_item_base = data.drop('user', 1)
data_sims = pd.DataFrame(index=data.index,columns=data.columns)

data_sims.ix[:,:1] = data.ix[:,:1]
# print data_item_base.head(8).ix[:,0:6]
# store DataFrame
data_item_base_frame = pd.DataFrame(index=data_item_base.columns, columns=data_item_base.columns)
# print data_item_base_frame.head(6).ix[:,0:6]
# Calculate similarily
for i in range(0, len(data_item_base_frame.columns)):
    # Loop through the columns for each column
    for j in range(0, len(data_item_base_frame.columns)):
        # Calculate similarity
        data_item_base_frame.ix[i, j] = 1 - cosine(data.ix[:, i], data.ix[:, j])

data_item_base_frame.to_csv('data_item_base_frame.csv', sep=',', encoding='utf-8')
# data_item_base_frame = pd.read_csv('data_item_base_frame.csv')

# Initial a frame for save closes neighbors to an item
data_neighbors = pd.DataFrame(index=data_item_base_frame.columns, columns = range(1, 3))

# Order by similarity
for i in range(0, len(data_item_base_frame.columns)):
    data_neighbors.ix[i,:5] = data_item_base_frame.ix[0:, i].sort_values(ascending=False)[:5].index

def similarity_score(history, similarities):
    return sum(history*similarities) / sum(similarities)

data_sims = pd.DataFrame(index=data.index,columns=data.columns)
data_sims.ix[:,:1] = data.ix[:,:1]
# print(data_sims)
for i in range(0, len(data_sims.index)):
    for j in range(1, len(data_sims.columns)):
        user = data_sims.index[i]
        product = data_sims.columns[j]
        if data.ix[i][j] == 1:
            data_sims.ix[i][j] = 1
        else:
            product_top_names = data_neighbors.ix[product][1:10]
            product_top_sims = data_item_base_frame.ix[product].sort_values(ascending=False)[1:10]
            user_histories = data_item_base.ix[user, product_top_names]
            data_sims.ix[i][j] = similarity_score(user_histories, product_top_sims)
            exit()

data_recommend = pd.DataFrame(index=data_sims.index, columns=['user','1','2'])

data_recommend.ix[0:,0] = data_sims.ix[:,0]
print(data_sims)