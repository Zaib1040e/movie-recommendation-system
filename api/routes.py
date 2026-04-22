import requests

def fetch_poster(movie_id):
    api_key = "7a5aea9266025f6735e9fa18461f4a54"   
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    
    data = requests.get(url).json()
    
    poster_path = data.get('poster_path')
    
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"