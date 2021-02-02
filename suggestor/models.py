import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors



def song_model(input):
    df = pd.read_csv('edited_data.csv')
    # adding direct url to data set by adding url prefix and id
    url = 'http://open.spotify.com/track/' + df['id']
    df['url'] = url
    
    # reordering columns, leaving out ID and release date
    df = df[['artists',  'name', 'url', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy',
       'explicit', 'instrumentalness', 'key', 'liveness', 'loudness',
       'mode', 'popularity', 'speechiness', 'tempo', 'valence']]
    
   # target set will be both artist and name
    y_set = ['artists', 'name', 'url']

    # droping target from data matrix
    df_data = df.drop(y_set, axis=1)

    # set target
    df_target = df[y_set]

    # fit on data, 12 neighbors
    nn = NearestNeighbors(algorithm='brute', leaf_size =15, n_neighbors=12, n_jobs=-1)
    nn.fit(df_data)

    # sample a song(index) from df_data to use as our query point 
    input_index=input

    # vectorize 
    data_vect = [df_data.iloc[input_index].values]
    neigh_dist, neigh_indices = nn.kneighbors(data_vect)
    indexs = neigh_indices.flat[0:12].tolist()

    #adding url to each track
    output = df_target.iloc[indexs]
    return (output)
