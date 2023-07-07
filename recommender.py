import streamlit as st;
import pickle
import pandas as pd
import requests
import base64
import joblib

primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#FFFFFF"
font="sans serif"
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('background.jpg')

movie_list=pickle.load(open("model/movies_list1.pkl","rb"))
movies=pd.DataFrame(movie_list) 
similar_movies=joblib.load(open("model/similar_movies_list4.pkl","rb"))
def getposter(movie_id): 
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d6b9a2389ebe2de75856f91564967590&language=en-U'.format(movie_id))
    data=response.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path  
def getoverview(movie_id): 
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d6b9a2389ebe2de75856f91564967590&language=en-U'.format(movie_id))
    data=response.json()
    overview=data['overview']
   
    return overview 

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similar_movies[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x: x[1])[1:6]
    recommmended_movies=[]
    movie_posters=[]
    overview=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        movie_posters.append(getposter(movie_id))
        overview.append(getoverview(movie_id))
        recommmended_movies.append(movies.iloc[i[0]].title)
    return recommmended_movies ,movie_posters ,overview  

st.title("5 New Recommendation  Movies You Would not Miss")
st.write("Don't have the time to decide which movie to watch next? Use these movie recommendation sites as a shortcut.")
st.header("select a movie you would like")
options=st.selectbox("movies list",movies['title'].values)
if st.button("recommend"):
    recommendations,movie_poster,overviews=recommend(options)
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.write(recommendations[0])
        st.image(movie_poster[0])
        
        st.write(overviews[0])
        
    with col2:
        st.write(recommendations[1])
        st.image(movie_poster[1])
        st.write(overviews[1])
    with col3:
        st.write(recommendations[2])
        st.image(movie_poster[2]) 
        st.write(overviews[2])  
    with col4:
        st.write(recommendations[3])
        st.image(movie_poster[3])
        st.write(overviews[3])
    with col5:
        st.write(recommendations[4])
        st.image(movie_poster[4])
        st.write(overviews[4])
import streamlit as st

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>© 2023 Movie Recommender App. All rights reserved</p>
<div>
</div >
<p><span style='color:red;'>Disclaimer:</span> The movie recommendations provided by this app are generated using advanced machine learning algorithms.
<br/> 
While we strive to provide accurate and personalized recommendations, please note that the final decision to watch a movie should be based on your own preferences and discretion.
<br/>
We aim to provide the best possible movie suggestions, but we cannot guarantee the availability or quality of the recommended movies.
</p>
<div>
<span style='colur:blue; font-weight:400;'> Contact Us:</span><a  href="https://github.com/srihari-swain" target="_blank">GitHub</a><span>,</span><a  href="https://www.linkedin.com/in/srihari-swain" target="_blank">Linkedin</a>
</div>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)



    


          


            
      
        
    
            

    

