#I am so lost
#do I need to have VS Code or just VS?

import streamlit as st
import emoji

st.set_page_config(page_title="All About Me", page_icon=":sneezing_face:", layout="wide")

# ----HEADER SECTION----
with st.container():
    st.subheader("Hi, I am Duke :wave:")
    st.title("A Struggling College Computer Science Major at UVU")
    st.write("I am making this website to learn about the way I can use Python to make websites for an E2i Project in School", ":sunglasses:")
    st.write("[Learn More >](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Because I basically have zero technical skills to show off here are random ones:
            - I can juggle up to 4 items :clown_face:
            - I benchpress 225 lb :muscle:
            - I cook often (not just ramen)
            - I enjoy coding, even though I ask Copilot for help
            
            Now you might think I am the whole package right now, but just wait till I can make this without a youtube tutorial
            """
        )