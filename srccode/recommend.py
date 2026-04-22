# from model import similarity
import pandas as pd 
import pickle


movies = pickle.load(open('data/processed/movies.pkl', 'rb'))
similarity = pickle.load(open('data/processed/similarity.pkl', 'rb'))

# movies=pd.read_csv(r"data/processed/clean_movie_data.csv",encoding="latin1")

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    
    recommended_movies=[]
    recommended_ids=[]

    for i in movies_list:
       recommended_movies.append(movies.iloc[i[0]].title)
       recommended_ids.append(movies.iloc[i[0]].id)
    return recommended_movies,recommended_ids 



# print(recommend("Interstellar"))