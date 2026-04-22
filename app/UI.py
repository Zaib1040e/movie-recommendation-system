import streamlit as st
import pickle
import pandas as pd
from  srccode.recommend import recommend
from api.routes import fetch_poster


st.set_page_config(
    page_title="Movie Recommender",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def run_app():
    st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

h1 {
    text-align: center;
    font-size: 3rem;
    font-weight: 700;
}

.stButton>button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: #262730;
    color: white;
}

img {
    border-radius: 12px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
img:hover {
    transform: scale(1.08);
    box-shadow: 0px 0px 25px rgba(255,255,255,0.3);
}
</style>
""", unsafe_allow_html=True)
    
    # 🔹 3. Sidebar (ADD HERE ✅)
    with st.sidebar:
        st.title("⚙️ Settings")
        st.write("Movie Recommender App")
        st.write("Made By- ZAIB ALI KHAN")
    
    st.set_page_config(page_title="Movie Recommender", layout="wide")
    
    
    st.markdown("<h1>🎥 Movie Recommender</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:gray;'>Discover movies you’ll love instantly</p>", unsafe_allow_html=True)

    # Load data
    movies_dict = pickle.load(open('srccode/movies.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    selected_movie = st.selectbox(
        "SELECT A MOVIE",
        movies['title'].values
    )

    if st.button("✨ Recommend"):
        with st.spinner("Finding best movies for you..."):
            names, ids = recommend(selected_movie)
        
        st.subheader("Top Recommendations")
        

        '''ROW-1'''
        cols = st.columns(5)

        for i in range(5):
            with cols[i]:
                st.image(fetch_poster(ids[i]))
                st.markdown(
                f"<p style='text-align:center; font-weight:600;'>{names[i]}</p>",
                unsafe_allow_html=True
            )
                

        '''ROW-2'''
        cols2 = st.columns(5)

        for i in range(5,10):
            with cols2[i-5]:
                st.image(fetch_poster(ids[i]))
                st.markdown(
                f"<p style='text-align:center; font-weight:600;'>{names[i]}</p>",
                unsafe_allow_html=True
            )
    
    st.markdown("""
<hr style="border: 1px solid #222;">
<p style='text-align:center; color:#aaa; font-size:13px;'>
    ✨ Created by Zaib |
    <a href="https://instagram.com/zaib_3.14" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" 
             width="20" style="vertical-align:middle; margin-left:5px;">
    </a>
</p>
""", unsafe_allow_html=True)
