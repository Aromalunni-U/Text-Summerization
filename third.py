import spacy
import networkx as nx
import numpy as np
import streamlit as st
from spacy.cli import download



def summerize():

    st.markdown("""
    <style>
    .stTextArea textarea {
        background-color:  rgba(0, 0, 87, 0.7)!important;  
        color: white;
        font-size: 16px;
        border:2px solid white;
        border-radius:8px;
    }
    </style>
    """, unsafe_allow_html=True)

  
    st.header("Text Summarization")
    st.write("Enter the text you want to summarize below:")

    text = st.text_area("", height=300,placeholder="Enter your text here and press Ctrl + Enter to generate summary.")

    if text:

        try:
            nlp = spacy.load("en_core_web_md")
        except OSError:
            download("en_core_web_md")
            nlp = spacy.load("en_core_web_md")
            
        doc = nlp(text)
        sentences = list(doc.sents)
        total_sentences = len(list(doc.sents))
        num_sentences = st.number_input("Number of sentences in summary", min_value=1, max_value=total_sentences,value=min(3, total_sentences) )


        if st.button("Generate Summary"):
            cleaned_sentences = []
            for sent in sentences:
                word = [token.lower_ for token in sent if not token.is_stop and token.is_alpha]
                cleaned_sentences.append(" ".join(word))

            similarity_matrix = np.zeros((len(sentences),len(sentences)))

            for i,sent1 in enumerate(sentences):
                for j,sent2 in enumerate(sentences):
                    if i != j:
                        similarity_matrix[i][j] = sent1.similarity(sent2)

            graph = nx.from_numpy_array(similarity_matrix)

            
            scores = nx.pagerank(graph)

            ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

            summary = [sentence.text.strip() for score, sentence in ranked_sentences[:num_sentences]]

            st.markdown("<h2 style='text-align:center;text-shadow:7px 7px 7px black;'>Summary</h2>",unsafe_allow_html=True)
            st.markdown("---")

            for sent in summary:
                st.write(sent)
    else:
        st.write("Please enter some text to summarize.")




