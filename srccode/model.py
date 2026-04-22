import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer
import pickle

movies=pd.read_csv(r"data/processed/clean_movie_data.csv",encoding="latin1")

movies['tags'] = movies['tags'].fillna('')
movies = movies[movies['tags'].str.strip() != ""]

'''This is To Make All PLural and Singular of a word into a 
common word like 
[love,loved,loving]--> [love,love,love]'''
ps=PorterStemmer()

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y) 
movies['tags']=movies['tags'].apply(stem)

cv=CountVectorizer(max_features=8000,stop_words='english')

vectors=cv.fit_transform(movies['tags']).toarray()

'''You Can Check All The Words That Have Been Selected'''
# print(cv.get_feature_names_out())

'''Here The Logic Is to Find the Closness between every movie to the selected one using cosine angle  '''
similarity=cosine_similarity(vectors)

similarity = similarity.astype(np.float32)

'''Pickle Helps The Data To Just Load Once And Give Results Fast Every Time'''
pickle.dump(movies, open('data/processed/movies.pkl', 'wb'))
pickle.dump(similarity, open('data/processed/similarity.pkl', 'wb'))