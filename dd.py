import streamlit as st
from streamlit_option_menu import option_menu


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

st.title("Movie Recommender System")
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",  # required
        options=["Home","Harvest", "About"],  # required
        icons=["house","arrows-move","envelope"],  # optional
        default_index=0,  # optional
        styles={"nav-link": {"--hover-color": "red"}},
        orientation="vertical",

    )





