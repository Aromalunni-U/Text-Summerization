import streamlit as st
from streamlit_option_menu import option_menu
import second
import third
import base64


def get_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

image = get_image("img1.jpg")

def main():

    st.markdown(
        f"""<style>
    .stApp {{
        background-image: url("data:image/png;base64,{image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>""", unsafe_allow_html=True
    )

    st.markdown("""
    <style>
               .st-emotion-cache-13ln4jf {
                background-color: rgba(0, 0, 87, 0.7)!important;
                padding-top:50px !important;
                padding-left:40px !important;
                padding-right:40px !important;
                } 
    </style>
                """,unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;color:white; text-shadow:7px 7px 7px black;'>Text Summarization App</h1>",unsafe_allow_html=True)
    st.markdown("---")

    with st.sidebar:
        selected = option_menu("Navigation", ["Introduction", "Summarization"],
            icons=['house', 'book'], 
            menu_icon="cast", 
            default_index=0, 
            styles={
                "container": {"padding": "5!important", "background-color": "black"},
                "icon": {"color": "white", "font-size": "25px"},
                "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px"},
                "nav-link-selected": {"background-color": "blue"},
            }
        )

    if selected == "Introduction":
        st.header("Introduction")
        st.write("""
            The app allows you to summarize large blocks of text by analyzing the most important sentences and providing a concise summary.""")
        st.write("### Key Features")
        st.write("""
            - Automatically generates summaries from input text.
            - Lets you customize the number of sentences in the summary.
                 """)
        
        st.write("""
    In this project, users can choose between two different text summarization techniques:
    
    1. **:green[Frequency-based summarization]**: This method selects sentences based on the frequency of important words within the text. Sentences containing frequently occurring words are highlighted in the summary.
    
    2. **:green[TextRank algorithm]**: This graph-based approach ranks sentences by their similarity to other sentences, selecting those with the highest centrality for the summary.
    
    You can select either of these summarization methods based on your preference and see how each one performs on the given text.
    """)

        st.write("**Please navigate to the **Summarization** section to try it out!**")
    
    elif selected =="Summarization":
           summarize_option = st.selectbox("Choose a method:", ["Frequency-Based Text Summarization", "TextRank: Graph-Based Extractive Summarization"])
           if summarize_option == "Frequency-Based Text Summarization":
               second.summarize()
           else:
               third.summerize()
  
         
               


main()