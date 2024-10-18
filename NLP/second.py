import spacy
from collections import Counter
import heapq
import streamlit as st


def summarize():

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
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        total_sentences = len(list(doc.sents))
        num_sentences = st.number_input("Number of sentences in summary", min_value=1, max_value=total_sentences,value=min(3, total_sentences) )


        if st.button("Generate Summary"):
            if text:
                
                filtered_text = [i.text.lower() for i in doc if not i.is_stop and not i.is_punct and not i.is_space]
                word_freq = Counter(filtered_text)
                max_freq = max(word_freq.values())
                for word in word_freq:
                    word_freq[word] = word_freq[word] / max_freq
                sentence = [i for i in doc.sents] 

                sent_score = {}

                for sent in sentence:
                    for word in sent:
                        word_lower = word.text.lower()
                        if word_lower in word_freq:
                            if sent not in sent_score:
                                sent_score[sent] = word_freq[word_lower]
                            else:
                                sent_score[sent] += word_freq[word_lower]


                summary_sentences = heapq.nlargest(num_sentences, sent_score, key=sent_score.get)
                summary = ' '.join([sent.text for sent in summary_sentences])

                st.markdown("<h2 style='text-align:center;text-shadow:7px 7px 7px black;'>Summary</h2>",unsafe_allow_html=True)
                st.markdown("---")
                st.write(summary)
    else:
        st.write("Please enter some text to summarize.")

