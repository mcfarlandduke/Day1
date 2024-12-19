#I am so lost
#do I need to have VS Code or just VS?

from PIL import Image
import streamlit as st

st.set_page_config(page_title="All About Me", page_icon="##", layout="wide")

img_monkey = Image.open("images/monkey.png")
img_headshot = Image.open("images/smaller_headshot.png")

# ----HEADER SECTION----
with st.container():
    st.subheader("Hi, I am Duke")
    st.title("A Struggling College Computer Science Major at UVU")
    st.write("I am making this website to learn about the way I can use Python to make websites for an E2i Project in School")
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
            - I can juggle up to 4 items 
            - I benchpress 225 lb 
            - I cook often (not just ramen)
            - I enjoy coding, even though I ask Copilot for help
            
            Now you might think I am the whole package right now, but just wait till I can make this without a youtube tutorial
            """
        )
    
    with right_column: 
        st.header("My Best Photo")
        st.image(img_headshot)



with st.container(): 
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Monkey")
        st.write("Because I think its funny")
        st.image(img_monkey)