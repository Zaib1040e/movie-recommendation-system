import pandas as pd
import numpy as np
import ast 



'''Importing The Data To Our Program'''
movies_data=pd.read_csv(r"data/raw/tmdb_5000_movies.csv")
credits_data=pd.read_csv(r"data/raw/tmdb_5000_credits.csv")


'''Selecting The Required Columns '''
movies_data=movies_data[['genres','id','keywords','overview','title','tagline']]

credits_data=credits_data[['title','cast','crew']]

movies=movies_data.merge(credits_data,on="title")

'''Checking The Null Rows'''
movies.isna().sum()
movies.duplicated().sum()

'''Converting The Dictionary Into A List Of The Items We Require'''
def convert(obj):
    if isinstance(obj, str):   # only convert if string
        obj = ast.literal_eval(obj)
    l=[]
    for item in obj:
        l.append(item['name'])
    return l

movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)

'''Selectin Top 3 Actors'''
def main_person(obj):
    l=[]
    count=0
    for item in ast.literal_eval(obj):
        if count!=3:
            l.append(item['name'])
            count+=1
        else:
            break
    return l

movies['cast']=movies['cast'].apply(main_person)

''''Fetching The Director Name'''
def director(obj):
    for i in ast.literal_eval(obj):
        if (i['job']=="Director"):
            return [i['name']]
        
movies['crew']=movies['crew'].apply(director)

'''Converting The Statements Into List To Join'''

movies['overview'] = movies['overview'].fillna('')
movies['overview']=movies['overview'].apply(lambda x: x.split( ) )

movies['tagline'] = movies['tagline'].fillna('')
movies['tagline']=movies['tagline'].apply(lambda x: x.split( ) )

movies['tags']=movies['overview']+movies['genres']*4+movies['keywords']*2+movies['cast']*3+movies['crew']*3+movies['tagline']

movies=movies[["id",'title','tags']]

movies['tags'] = movies['tags'].apply(lambda x: x if isinstance(x, list) else [])

movies['tags']=movies['tags'].apply(lambda x: [i.replace(" ","") for i in x])

'''Again The Whole List Into Strings For Vectorization'''
movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))

movies['tags']=movies['tags'].apply(lambda x: x.lower())



movies.to_csv("data/processed/clean_movie_data.csv")

