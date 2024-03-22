import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import requests


import pickle

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data ['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.set_page_config(page_title="Movie Recommender system", page_icon="",layout="wide", initial_sidebar_state="expanded")
st.markdown(
    """
    <style>
    .main {
        padding: 0rem 0rem;
    }
    .sidebar .sidebar-content {
        width: 300px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title ("Movies Recommender System")
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",  # required
        options=["Home","Harvest", "About"],  # required
        icons=["house","arrows-move","envelope"],  # optional
        default_index=0,  # optional
        styles={"nav-link": {"--hover-color": "red"}},
        orientation="vertical",

    )
if selected =="Home":
    st.markdown(
        '__<p style="font-family: verdana; text-align:left; font-size: 20px; color: #008FFF">This project is focused on recommending movies of a similar genre or with related stories to the selected movie.</P>__',
        unsafe_allow_html=True)

    st.markdown("""
    
    For this project :
    
        * First, we downloaded a dataset, and then we imported to python. 

        * Then EDA, has been done to the dataset  and all other essential steps are undertaken.
        
        * Lastly, streamlit is used to create the dashboard.

    """)

if selected == "Harvest":
    selected_movie_name = st.selectbox(
        'Select a movie of your interest',
        movies['title'].values
    )

    if st.button("Recommend"):
        st.write ("Here are the recommended movies based on the selected film.")
        names, posters = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])
        with col2:
            st.text(names[1])
            st.image(posters[1])

        with col3:
            st.text(names[2])
            st.image(posters[2])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])


if selected =="About":
    st.write(" ")
    st.write(" ")
    st.markdown("### :red[Movie Recommendation System:] ")

    st.write("**:violet[My Project GitHub link - https://github.com/sheik-muzzammil/Movie-Recommendation-App]** ⬇️")
